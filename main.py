"""Pick the strongest one-line cat joke and publish it as the entry.

The brief asks for a single line about cats, under 200 characters, that
lands as a joke on first reading. Twelve lines were drafted by hand and
marked against the brief's own order of importance: on-subject with a
setup and a turn, funny out loud, surprising rather than a tired pun,
tight with no padding, and retellable to a friend the same day. The
highest total wins; a tie goes to the shorter line, then to the earlier
draft. The winning text is pinned by its SHA-256 fingerprint so an
accidental edit can never change the entry silently.
"""

import hashlib
import sys
from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 199
DIGEST_PARTS = (
    "9c60cfd055e6bb5f",
    "88873717a3f6cf31",
    "5986000599e6ef14",
    "95e5979b6a9c8fcc",
)
CRITERIA = ("subject", "laugh", "surprise", "tight", "retell")


def total_marks(marks):
    return sum(marks[criterion] for criterion in CRITERIA)


DRAFTS = [
    {
        "line": (
            "My cat wakes me at 5 a.m. every day "
            "to check his bowl. It has never once been empty — "
            "he just likes the meeting."
        ),
        "marks": {"subject": 10, "laugh": 10, "surprise": 10, "tight": 10, "retell": 9},
        "note": "The 5 a.m. bowl check is the most familiar cat ritual there is, and the last word turns it into office bureaucracy.",
    },
    {
        "line": (
            "I bought my cat a heated bed for winter. He sleeps on the cold "
            "tile next to it, supervising the waste of money."
        ),
        "marks": {"subject": 10, "laugh": 9, "surprise": 9, "tight": 9, "retell": 9},
        "note": "The expensive bed loses to cold tile, and the cat supervises the bad purchase like a manager.",
    },
    {
        "line": (
            "My cat knocked my phone off the counter and watched it fall. "
            "He was not being bad — he was testing the warranty."
        ),
        "marks": {"subject": 10, "laugh": 9, "surprise": 9, "tight": 9, "retell": 8},
        "note": "The falling phone becomes a product test, which gives the destruction a deadpan excuse.",
    },
    {
        "line": (
            "My cat sits on my laptop every time I open it. He has never "
            "read a single email, but he approves all of them."
        ),
        "marks": {"subject": 10, "laugh": 9, "surprise": 9, "tight": 8, "retell": 9},
        "note": "Sitting on the keyboard becomes middle management: zero reading, total approval.",
    },
    {
        "line": (
            "I told my cat he is adopted. He yawned, which I choose to "
            "believe means he already knew and kept the secret."
        ),
        "marks": {"subject": 10, "laugh": 9, "surprise": 8, "tight": 9, "retell": 8},
        "note": "The yawn reads as a secret kept, which flips who is in on the joke.",
    },
    {
        "line": (
            "My cat brings me dead bugs as gifts. I smile and say thank you, "
            "because nobody else in this house works this hard."
        ),
        "marks": {"subject": 10, "laugh": 8, "surprise": 9, "tight": 9, "retell": 8},
        "note": "A grim gift becomes the hardest work in the house, and gratitude is the only polite response.",
    },
    {
        "line": (
            "My cat drinks from the tap and ignores his fountain. The "
            "fountain cost $40; the tap cost him nothing."
        ),
        "marks": {"subject": 10, "laugh": 8, "surprise": 9, "tight": 8, "retell": 8},
        "note": "$40 of pet engineering loses to a free tap, priced out in the second sentence.",
    },
    {
        "line": (
            "I hid my cat's treats on the top shelf. He found them in four "
            "minutes, and now I hide my snacks from him instead."
        ),
        "marks": {"subject": 10, "laugh": 8, "surprise": 8, "tight": 9, "retell": 8},
        "note": "Four minutes of searching reverses the hiding: now the owner hides from the cat.",
    },
    {
        "line": (
            "My cat sleeps twenty hours a day and still acts exhausted. "
            "I respect the commitment to doing absolutely nothing."
        ),
        "marks": {"subject": 10, "laugh": 9, "surprise": 8, "tight": 8, "retell": 8},
        "note": "Twenty hours of sleep plus exhaustion is a work ethic in reverse, admired rather than scolded.",
    },
    {
        "line": (
            "My cat watches me cook with total focus. He has never once "
            "offered to help, but his supervision is relentless."
        ),
        "marks": {"subject": 10, "laugh": 8, "surprise": 8, "tight": 8, "retell": 9},
        "note": "Total focus with zero help is the purest form of supervision, and every cook knows it.",
    },
    {
        "line": (
            "I bought my cat a toy mouse that squeaks. He plays with the "
            "receipt instead, because the receipt was free."
        ),
        "marks": {"subject": 10, "laugh": 8, "surprise": 8, "tight": 8, "retell": 8},
        "note": "The toy loses to its own receipt, and free beats squeaky as a cat's whole value system.",
    },
    {
        "line": (
            "My cat waits by the door when I come home. Not because he "
            "missed me — because I am late with dinner again."
        ),
        "marks": {"subject": 10, "laugh": 8, "surprise": 8, "tight": 8, "retell": 8},
        "note": "The welcome home is really a dinner complaint, which punctures the sentimental reading.",
    }]


def guard_draft(draft):
    line = draft["line"]
    if not line or not line.strip():
        raise ValueError("draft is blank")
    if line != line.strip():
        raise ValueError("draft carries leading or trailing space")
    if "\n" in line or "\r" in line:
        raise ValueError("draft must stay on one line")
    if len(line) > CHAR_LIMIT:
        raise ValueError(f"draft runs {len(line)} characters, over the {CHAR_LIMIT} limit")
    if "  " in line:
        raise ValueError("draft carries a double space")
    if "\t" in line:
        raise ValueError("draft carries a tab")
    if "cat" not in line.lower():
        raise ValueError("draft is not about a cat")
    if not line.endswith("."):
        raise ValueError("draft does not end on a full stop")
    if tuple(draft["marks"]) != CRITERIA:
        raise ValueError("draft is missing a marking criterion")
    for value in draft["marks"].values():
        if not 0 <= value <= 10:
            raise ValueError("a mark sits outside 0-10")


def best_draft(drafts):
    ranked = []
    for position, draft in enumerate(drafts):
        guard_draft(draft)
        ranked.append(
            (-total_marks(draft["marks"]), len(draft["line"]), position, draft["line"])
        )
    ranked.sort()
    return ranked[0][3]


def fingerprint(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def publish(text):
    wanted = "".join(DIGEST_PARTS)
    if fingerprint(text) != wanted:
        raise ValueError(f"winning line fingerprint moved: {fingerprint(text)}")
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_bytes(text.encode("utf-8"))
    ENTRY_PATH.chmod(0o644)
    on_disk = ENTRY_PATH.read_bytes().decode("utf-8")
    if on_disk != text:
        raise ValueError("entry.txt on disk differs from the winning line")
    if fingerprint(on_disk) != wanted:
        raise ValueError("entry.txt fingerprint moved after writing")
    sys.stdout.write(text + "\n")


def run():
    publish(best_draft(DRAFTS))
    return 0


if __name__.endswith("__main__"):
    raise SystemExit(run())
