#!/usr/bin/env python3
"""Build a Face-Off acronym pool from an acronym repo's data/acronyms.json.

The Face-Off pages load plain <script> files and never fetch(), because they
have to work from file:// on a classroom laptop with no server. So the JSON
becomes a JS file that sets a global, exactly the way questions-*.js does.

This is a THIRD copy of that acronym data, and the program's own CLAUDE.md
already flags two-copy drift as a live risk. That is why this script exists
and is committed: the copy is regenerated, never hand-edited.
"""
import io, json, re, sys, os

SRC, OUT, GLOBAL, TITLE, EXAM = sys.argv[1:6]

items = json.load(io.open(SRC, encoding="utf-8"))
if isinstance(items, dict):
    items = items.get("acronyms") or items.get("data") or []

# Group by the category the bank already carries. Categories are the board's
# columns, so their names go up in the header and get uppercased to match the
# question bank's house style.
cats = {}
order = []
for it in items:
    ac = (it.get("acronym") or "").strip()
    ex = (it.get("expansion") or "").strip()
    df = (it.get("definition") or "").strip()
    cat = (it.get("category") or "General").strip()
    if not ac or not ex or not df:
        sys.exit('acronym "%s" is missing an expansion or a definition; '
                 "every entry needs both or the clue forms cannot be built." % (ac or "?"))
    if cat not in cats:
        cats[cat] = []
        order.append(cat)
    cats[cat].append({"ac": ac, "ex": ex, "df": df, "cat": cat})

# Biggest categories first: a board asks for N categories and skips any that
# cannot fill a column, so putting the deep ones first makes short boards work
# without special-casing.
order.sort(key=lambda c: -len(cats[c]))

def js(s):
    return json.dumps(s, ensure_ascii=False)

# AN ACRONYM CAN LEGITIMATELY MEAN TWO THINGS. Network+ has STP for both
# Spanning Tree Protocol and Shielded Twisted Pair, and a student ought to
# meet both. But "Expand this acronym: STP" then has two right answers and
# a team giving the other one would be marked wrong, so any acronym with
# more than one expansion carries the field it belongs to and the clue says
# which one it wants.
seen_ex = {}
for c in order:
    for it in cats[c]:
        seen_ex.setdefault(it["ac"], set()).add(it["ex"])
ambiguous = {a for a, ex in seen_ex.items() if len(ex) > 1}
for c in order:
    for it in cats[c]:
        if it["ac"] in ambiguous:
            it["amb"] = it["cat"]

total = sum(len(cats[c]) for c in order)
small = [c for c in order if len(cats[c]) < 5]

out = []
out.append("/* =====================================================================")
out.append("   FACE-OFF: %s  —  ACRONYM POOL" % TITLE)
out.append("   Exam: %s" % EXAM)
out.append("   ---------------------------------------------------------------------")
out.append("   GENERATED FILE — do not hand-edit.")
out.append("   Rebuild with:  python3 tools/build-acronyms.py")
out.append("   Source of truth: the %s acronym repo's data/acronyms.json." % TITLE)
out.append("")
out.append("   %d acronyms in %d categories." % (total, len(order)))
out.append("")
out.append("   THERE IS NO DIFFICULTY RAMP IN AN ACRONYM. Nothing makes MAC a 100")
out.append("   and SD-WAN a 500, which is a problem on a board whose whole shape is")
out.append("   a column climbing 100 to 500. So the ramp is the TASK, not the item:")
out.append("   the cheap rows ask you to expand the letters, the middle rows give")
out.append("   you a description and ask which acronym it is, and the dear rows")
out.append("   give you the acronym and ask what it actually does. Same acronym,")
out.append("   three difficulties — which is also why %d acronyms go a long way." % total)
out.append("")
out.append("   The clue text is built at draw time from these three fields, so")
out.append("   there is no answer bank to memorise and editing an acronym here")
out.append("   changes every form of it at once.")
out.append("")
out.append("     ac = the acronym          ex = what the letters stand for")
out.append("     df = what it actually does")
out.append("     amb = set only when this acronym means something else somewhere")
out.append("           in the bank; the clue names this field so the team is not")
out.append("           marked wrong for giving the other correct expansion.")
if small:
    out.append("")
    out.append("   Categories with fewer than 5 entries cannot fill a five-row column")
    out.append("   and are skipped on the largest boards. They still play on shorter")
    out.append("   boards and in the Lightning Final. Currently: %s." % ", ".join(small))
out.append("   ===================================================================== */")
out.append("")
out.append("window.%s = {" % GLOBAL)
out.append("  categories: [")
for ci, c in enumerate(order):
    out.append("    { name: %s," % js(c.upper()))
    out.append("      items: [")
    for it in cats[c]:
        out.append("      { ac: %s," % js(it["ac"]))
        out.append("        ex: %s," % js(it["ex"]))
        if it.get("amb"):
            out.append("        amb: %s," % js(it["amb"]))
        out.append("        df: %s }," % js(it["df"]))
    out.append("      ] },")
out.append("  ]")
out.append("};")
out.append("")

io.open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("%s: %d acronyms, %d categories -> %s" % (TITLE, total, len(order), OUT))
if ambiguous:
    print("  more than one meaning (clue will say which field): %s" % ", ".join(sorted(ambiguous)))
if small:
    print("  under 5 entries (skipped on 5-row boards): %s" % ", ".join(small))
