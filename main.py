# The One-Line Cat Joke That Lands — make.fun bounty
# u-aldy998-the-one-line-cat-joke-that-lands-a7b18262
#
# The program writes one joke about cats, a single line under 200
# characters and nothing else, to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. is a one-line joke about cats, with a setup and a turn that lands
#   2. makes you laugh out loud on the first read, not merely smile
#   3. turns on a surprise, a misdirection or a fresh angle on cats
#      rather than a pun heard many times before
#   4. says everything it needs in a few words, no padding, no wind-up,
#      no explanation after the punchline
#   5. feels like a joke a person would actually retell to a friend
#      the same day
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: on-subject 10, laugh 10, surprise 10, tight 10,
    #   retellable 9 = 49. The 5 a.m. wake-up is the most recognisable
    #   cat behaviour there is; "he just likes the meeting" reframes
    #   the whole ritual as office bureaucracy, and the punch lands
    #   on the very last word.
    ("My cat wakes me at 5 a.m. every day to check his bowl. "
     "It has never once been empty \u2014 he just likes the meeting.",
     49),
    # score: on-subject 10, laugh 9, surprise 9, tight 9,
    #   retellable 9 = 46. The expensive-bed-in-the-box trope is
    #   familiar, but sleeping on the receipt so the owner never
    #   forgets the bad investment is the fresh turn.
    ("I bought my cat a $200 bed. He sleeps in the box it came in "
     "\u2014 on the receipt \u2014 so I never forget what a bad "
     "investment I am.",
     46),
    # score: on-subject 10, laugh 9, surprise 9, tight 9,
    #   retellable 9 = 46. The wall-staring mystery resolves into
    #   the cat rewatching the owner's life choices; the ghost
    #   setup makes the second clause land harder.
    ("My cat stares at the wall for an hour every night. Either "
     "he's seen a ghost, or he's rewatching my life choices.",
     46),
    # score: on-subject 10, laugh 9, surprise 8, tight 9,
    #   retellable 8 = 44. The 3 a.m. zoomies, reframed as the cat
    #   paying rent back in unwanted cardio.
    ("My cat does parkour at 3 a.m. every night. I pay the rent; "
     "he pays me back in cardio I never asked for.",
     44),
    # score: on-subject 10, laugh 8, surprise 8, tight 9,
    #   retellable 8 = 43. The cat out-writes the owner; the
    #   publisher's only note is about meetings, not the novel.
    ("My cat sat on my keyboard and typed a better novel than mine. "
     "The publisher only asked that he stop walking on it during "
     "meetings.",
     43),
    # score: on-subject 10, laugh 8, surprise 8, tight 9,
    #   retellable 8 = 43. The paperwork says Muffin; the crown
    #   says otherwise.
    ("The vet asked my cat's name. He looked at her like she should "
     "already know: the paperwork says Muffin, but the crown says "
     "otherwise.",
     43),
    # score: on-subject 10, laugh 8, surprise 8, tight 9,
    #   retellable 8 = 43. The slow blink means "I love you" on the
    #   internet; in this house it is a food review.
    ("My cat slow-blinks at me, which the internet says means "
     "'I love you.' In his case it means 'the food better be "
     "better next time.'",
     43),
    # score: on-subject 10, laugh 8, surprise 8, tight 8,
    #   retellable 8 = 42. Eye contact while the glass falls; the
    #   pet is a tiny manager testing gravity on company time.
    ("My cat pushed my glass off the table while holding eye "
     "contact. I don't own a pet \u2014 I live with a tiny manager "
     "testing gravity on company time.",
     42),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text, and
# the brief asks for under 200 characters, so every candidate is kept
# below 200.
MAX_CHARS = 199


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= MAX_CHARS, \
            f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import hashlib
    import os
    # SHA-256 self-check: the chosen line must hash to the value recorded
    # when the candidates were drafted, so a silent edit to the winning
    # text (or to the file on disk) is caught instead of shipped.
    expected_sha256 = (
        "9c60cfd055e6bb5f88873717a3f6cf315986000599e6ef1495e5979b6a9c8fcc"
    )
    actual_sha256 = hashlib.sha256(line.encode("utf-8")).hexdigest()
    assert actual_sha256 == expected_sha256, \
        f"chosen line hash changed: {actual_sha256}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= MAX_CHARS, \
        "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    assert "\n" not in written.strip(), "entry.txt must be one line"
    # Re-hash what is on disk: the file the gate reads must match the
    # chosen line byte for byte, not just in length.
    written_sha256 = hashlib.sha256(written.encode("utf-8")).hexdigest()
    assert written_sha256 == expected_sha256, \
        f"entry.txt hash changed on disk: {written_sha256}"
    print(line)


if __name__ == "__main__":
    main()
