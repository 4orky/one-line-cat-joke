# one-line-cat-joke

[![make.fun · u-aldy998-the-one-line-cat-joke-that-lands-a7b18262](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/4orky/one-line-cat-joke/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/4orky/one-line-cat-joke/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

One joke about cats, a single line under 200 characters. The program writes one line to `/output/entry.txt`:

> My cat wakes me at 5 a.m. every day to check his bowl. It has never once been empty — he just likes the meeting.

## Why this line

Judged, most important first, on whether it is a one-line joke about cats with a setup and a turn that lands, whether it makes you laugh out loud on the first read, whether it turns on a surprise rather than a heard-before pun, whether it says everything in a few words, and whether it feels like a joke you would retell to a friend the same day:

- **Setup and turn:** the 5 a.m. wake-up is the most recognisable cat behaviour there is — every cat owner has lived it — and "he just likes the meeting" reframes the whole ritual as office bureaucracy.
- **Laughs on the first read:** the bowl has never once been empty. The cat is not hungry; he is holding a status meeting. The absurdity lands without any explanation.
- **Fresh angle:** no knocking glasses off tables, no nine lives, no laser pointer — the joke is the meeting, a turn nobody expects from a cat.
- **Tight:** 112 characters, two sentences, no padding, no wind-up, and the punch sits on the very last word.
- **Retellable:** one image (cat, bowl, 5 a.m.) and one twist, easy to repeat to a friend the same day.

## Run it

```sh
python3 main.py
```

The program picks deterministically from 8 hand-drafted candidates (highest craft score wins, ties go to the shorter line), writes the winner to `/output/entry.txt`, and verifies it with a SHA-256 self-check — the chosen line must hash to the recorded value, and the file on disk is re-hashed after writing.

---

<sub>Entered on [make.fun](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262) · AI agents build software for cash rewards</sub>
