# ⚔ FACE-OFF: Network+

An elimination **tournament** for **CompTIA Network+ (N10-009)** — Family Feud
buzzers, a Jeopardy point board, hidden Daily Doubles, teams knocked out each
round, and a head-to-head Lightning Final. Built for the Cyber Warrior Program.

Students join by scanning a QR code or clicking a link. They pick their own team
name and color, type their own names, buzz in from their phone or laptop, and
type their team's answer for you to judge.

Runs entirely in the browser. No install, no accounts for students, no app.

---

## Quick start

**Just want to see it?** Open `demo.html` — it shows the host screen and two
student devices side by side in one window.

**Running it in class:**

1. Open `index.html` on the projector → **Host a Game**.
2. Students scan the QR or go to the link and enter the 4-letter room code.
3. You tell each student which team they're on. They tap that team, type their
   name, and the first one in becomes captain (picks the team name and color).
4. Click **Start Game →**. The bracket builds itself from your team count.

## How the tournament works

It's a bracket. Teams get knocked out until two are left, and those two settle
it head to head.

```
   8 teams  →  Round 1  →  cut bottom 2  →  6 teams
                          Round 2  →  cut bottom 2  →  4 teams
                          Round 3  →  cut bottom 2  →  2 teams
                                   ⚡ LIGHTNING FINAL ⚡
```

Scores **carry over** the whole way, so a strong early round still counts in the
final. Point values **grow each round** — Round 1 tops out at 500, Round 2 at
1,000, Round 3 at 1,500 — so a team behind early can still climb back.

### Playing a board

| Step | What happens |
|---|---|
| You click a point value | The question goes up on the projector and on every student device |
| Any team hits **BUZZ** | First buzz wins. That team gets **15 seconds** |
| The team types an answer | *Anyone* on the team can type — they talk it out, one types |
| You click **✓ Correct** | They score, and they pick the next clue |
| You click **✕ Incorrect** (or time runs out) | That team is locked out and the board **reopens to every other team still in the bracket** |
| All teams miss | You reveal the answer and move on |

Buzz order is shown on screen (#1, #2, #3…) so nobody argues about who was first.

### Eliminations

When the board is cleared — or whenever you click **End this round early** — you
get a standings screen with the bottom two already marked for elimination.

- **Click any team to change who goes out.** You have the final say.
- If teams are **tied at the cut line**, the screen says so in yellow and waits
  for you to pick. It will not guess.
- It won't let you continue until exactly the right number are selected.

Eliminated teams keep their device. Questions and answers still appear on it so
they can keep reviewing and follow the standings — they just can't buzz.

### ⚡ The Lightning Final

The last two teams go head to head. No board — just rapid-fire questions worth
**500 each**, 10 seconds apiece, fastest buzz takes it. Miss, and the other team
gets the rest of the clock. If they're tied when the questions run out, it goes
to **sudden death**.

### Daily Doubles

Hidden randomly on every board — **you never know where they are either**. Never
in the cheapest rows. The team that uncovers one wagers up to their own score,
answers alone, and there's **no steal**. Bigger boards hide two.

## Class vs Class

Turn on **Class vs Class** in Settings and the teams split into two classes —
name them whatever you like (`PERIOD 2` / `PERIOD 4`, etc.).

**Each class runs its own bracket.** Everyone plays the same board and buzzes on
the same questions, but eliminations happen *within* each class: the bottom two
of Class A go out, and the bottom two of Class B go out. That continues until
each class has exactly **one champion left**, and those two meet in the
Lightning Final. The final is guaranteed to be one class against the other.

```
CLASS A: 8 → 6 → 4 → 2 → 1 ┐
                            ├─ ⚡ LIGHTNING FINAL ⚡
CLASS B: 8 → 6 → 4 → 2 → 1 ┘
```

A **class scoreboard** runs across the top of the board the whole game — every
team's points feed their class total, including teams already eliminated. So
there are two things to win: the team trophy and the class trophy.

Teams are split down the middle automatically (first half Class A, second half
Class B). On the join screen each team card has a small **A / B badge — click it
to move that team to the other class** before you start.

## Class size and running time

Set **number of teams** (2–16), **students per team** (2–8), and **tournament
length** in Settings. The panel shows your exact bracket as you change them.

| Setup | Teams | Students |
|---|---|---|
| One class of 40 | 8 × 5 (default) | 40 |
| One class of 80 | 10 × 8 | 80 |
| **Two classes of 40** | **16 × 5** — 8 teams per class | **80** |

**Tournament length** scales the boards so the whole bracket fits your period:

| Length | Each board | Lightning Final |
|---|---|---|
| 30 min | 3 categories × 3 | 8 questions |
| 45 min | 4 × 3 | 10 |
| 60 min | 4 × 4 | 10 |
| 90 min | 5 × 5 | 12 |
| 120 min | 6 × 5 | 15 |

With 8 teams per class the bracket is **4 rounds** (8→6→4→2→1). At the 60-minute
preset that's four 4×4 boards plus the final.

**One caution above ~90 students:** Firebase's free plan allows 100 devices
connected at once. 80 students plus the host is 81, comfortably inside it.

## Other settings (⚙ in the top bar)

Seconds to answer, Lightning Final seconds, minimum Daily Double wager, sound
on/off, and whether a wrong answer **deducts** points (off by default — with
open steals, deducting punishes the teams brave enough to buzz).

You can also nudge any score by hovering a team card and clicking **+ / −**, and
click any team card to hand them board control.

Shrinking the roster settings never strands a student: the game refuses to set
students-per-team below a roster that's already fuller than that, and asks for
confirmation before removing teams that already have students on them.

---

## Local Mode vs Live Mode

| | Local Mode (default) | Live Mode |
|---|---|---|
| Setup | none | one free Firebase project, ~10 min |
| Students join from | another tab on the host computer only | any phone or laptop |
| Use it for | testing, single-screen play with keyboard buzzers | actual class |

**To go live, follow [`FIREBASE-SETUP.md`](FIREBASE-SETUP.md).** The home screen
tells you which mode you're in.

## Deploying to GitHub Pages

Push these files to the repo root, then **Settings → Pages → Source: Deploy from
a branch → `main` / `(root)`**. Give it a minute and it's live at
`https://rafikiscyent888.github.io/Face-off-Networking/`.

### GitHub or GitLab?

**GitHub, and it isn't close for you.** Your other course material already lives
there, GitHub Pages is one dropdown to turn on, and you already know the
workflow from VS Code. GitLab Pages needs a `.gitlab-ci.yml` build file to do
the same job. There's no feature here you'd gain by switching.

---

## Editing the questions

Everything lives in **`questions-network.js`** — plain text, no code knowledge
needed. It's a **pool**, not fixed rounds: the game draws unused clues each
round, so no question ever repeats inside one tournament.

```js
{ q: "The question students see.",
  a: "The answer only you see",
  alt: ["another phrasing you'd accept"],   // optional
  obj: "1.2" }                              // CompTIA objective, shown on the host screen
```

Each category's clues run **easiest first, hardest last** — that ordering is
what becomes the 100 → 500 rows on the board, so keep it if you add clues.

### What's in there now

**120 board questions** — 12 categories × 10 clues — plus **30 Lightning Final
questions**. Every N10-009 objective from 1.1 to 5.5 is covered:

| Category | Objectives | Domain |
|---|---|---|
| OSI Model | 1.1 | Networking Concepts |
| Ports & Protocols | 1.4 | Networking Concepts |
| IPv4 & Subnetting | 1.7 | Networking Concepts |
| Cloud & Topologies | 1.3, 1.6, 1.8 | Networking Concepts |
| Cables & Media | 1.5 | Networking Concepts |
| Routing & Switching | 2.1, 2.2 | Network Implementation |
| Wireless | 2.3 | Network Implementation |
| Network Services | 1.2, 3.4 | Concepts / Operations |
| Operations & Docs | 3.1, 3.2, 3.3, 3.5 | Network Operations |
| Network Security | 4.1, 4.3 | Network Security |
| Attacks & Threats | 4.2 | Network Security |
| Troubleshooting | 5.1–5.5 | Network Troubleshooting |

Subnetting questions include real calculations — network and broadcast
addresses, CIDR conversions, and "how many subnets and hosts" — not just
definitions.

That's enough for a **4-board tournament with zero repeats**. If a game ever
runs the pool dry, it recycles rather than breaking.

## Three kinds of game

Open **⚙ Game settings** and pick under **What are we playing?**

| Style | The board | The Lightning Final |
|---|---|---|
| **Normal** | The Network+ question bank, as always | Question bank |
| **Acronyms** | Every column is acronyms | Acronyms |
| **Mixed** | Whole acronym columns sitting among normal ones | Question bank |

All three work exactly the same in **Class vs Class** — the style and the
class split are independent settings.

### There is no difficulty ramp in an acronym

The question bank is authored easiest-first, and that ordering *is* the
100 → 500 climb down a column. Nothing equivalent exists for acronyms —
nothing makes MAC a 100 and SD-WAN a 500. So on an acronym column the ramp
is the **task**, not the item:

| Row | What the team is asked | Example |
|---|---|---|
| Cheap | Expand the letters | "Expand this acronym: *TCP*" |
| Middle | Name it from a description | "Reliable, ordered delivery — which acronym?" |
| Dear | Say what it actually does | "*TCP* — what does it actually do?" |

Same acronym, three difficulties. That is also why 135 acronyms go a long
way: an acronym is only ever served **once** per pool cycle, but which of
the three forms it arrives as depends on where it lands on the board.

The Lightning Final uses the hardest form throughout — by the final,
expanding letters is not a championship question.

### Mixed boards

Roughly a third of the columns are acronyms, never fewer than one and never
the whole board. They are **shuffled in among the question columns**, not
bolted onto the end, so a team cannot quietly steer around them.

### Acronyms that mean two things

Network+ has **STP** twice — Spanning Tree Protocol *and* Shielded Twisted
Pair. Both belong in the game. But "expand STP" would then have two right
answers, so the clue names the field it wants ("as used in Hardware &
Cabling") and the host screen carries a note that the other reading exists.
This is automatic: the builder finds any acronym with more than one
expansion and marks it.

### The Lightning Final remembers too

It did not used to. The board deck has carried its used clues across
tournaments from the start, but the Lightning Final reshuffled the whole
pool every game — so a class playing two or three games in an afternoon met
the same championship questions each time, while the board in front of them
never repeated.

It now works the same way as everything else: used final questions are
remembered, carried between tournaments, and recycled only once the pool is
genuinely spent. **Reset pool** clears them along with the board clues,
because it is the same bank. Game settings shows how many are left.

### The acronym pool remembers, same as the question pool

Used acronyms carry over between tournaments and survive a page reload, so
back-to-back games don't repeat. **Acronyms and Mixed games share one
memory** — an acronym seen on a mixed board won't come back in an acronym
game either.

Game settings shows how much is left and gives you a **Reset acronyms**
button beside the existing **Reset pool**. The two are separate: resetting
acronyms does not put already-seen questions back, and vice versa.

The pool empties to within one board of exhaustion before it recycles. (A
board needs 16 clues, so a remainder smaller than that can never be dealt —
measured, it serves 128 of 135 before recycling.)

## Editing the acronyms

**Don't edit `acronyms-network.js` by hand.** It's generated from the
Network-Acronyms repo, which is the source of truth:

```
python3 tools/build-acronyms.py \
  ../network-acronyms/data/acronyms.json \
  acronyms-network.js FACEOFF_ACRONYMS "NETWORK+" "CompTIA Network+ N10-009"
```

It reports how many acronyms and categories it wrote, which acronyms have
more than one meaning, and which categories are too small to fill a five-row
column. Categories with fewer than 5 entries can't fill the tallest boards
and sit those out — they still play on shorter boards and in the Lightning
Final.

Editing the file by hand works until somebody regenerates it, at which point
the edit is gone. Change the acronym repo instead and rebuild.

## Files

| File | What it is |
|---|---|
| `index.html` | The game — all markup and styling |
| `app.js` | Game engine: host console, student device, networking |
| `questions-network.js` | **The question bank — this is the file you'll edit** |
| `acronyms-network.js` | The acronym bank — **generated**, see above |
| `tools/build-acronyms.py` | Rebuilds `acronyms-network.js` from the acronym repo |
| `firebase-config.js` | Paste your Firebase keys here to go live |
| `qr.js` | Self-contained QR generator (no CDN, works offline) |
| `demo.html` | Host + 2 student devices side by side, for testing alone |
| `FIREBASE-SETUP.md` | Step-by-step guide to enabling phone join |
| `.nojekyll` | Empty file — tells GitHub Pages to skip Jekyll processing |

There are **no external dependencies**. Nothing is fetched from a CDN, so it
works on a locked-down school network and even fully offline in Local Mode.

## Browser support

Any current Chrome, Edge, Firefox, or Safari, desktop or mobile. Sound uses the
Web Audio API — on some phones the first tap unlocks it, which the join button
handles.

## Troubleshooting

**Students stuck on "Looking for room…"** — you're in Local Mode. See
`FIREBASE-SETUP.md`. If you're already in Live Mode, the school network is
probably blocking `*.firebaseio.com`.

**A student refreshed and lost their spot** — they just rejoin with the same
name on the same team and reclaim their seat.

**Two students on one laptop** — add a seat number to the link:
`…#/play/ABCD/1` and `…#/play/ABCD/2` are two separate players.

**Everything died mid-game** — scores live on the host screen. Don't reload the
host tab; if you must, use the keyboard buzzers (`1`–`9`, `0`, `-`, `=`, `q`,
`w`, `e`, `r`) and adjust scores with the +/− buttons.

---

Color scheme inherited from
[Cyber Warrior Command Center 2.0](https://rafikiscyent888.github.io/Cyber-Warrior-Command-Center-2.0/).
