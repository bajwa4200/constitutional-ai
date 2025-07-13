from dataclasses import dataclass

RULES = [
    ("no_slur", lambda t: "badword" not in t.lower()),
    ("be_polite", lambda t: not any(w in t.lower() for w in ("stupid", "idiot"))),
    ("no_secret", lambda t: "password" not in t.lower()),
]

@dataclass
class RevisionResult:
    text: str
    rounds: int
    violations: list[str]

def critique(text: str) -> list[str]:
    return [name for name, fn in RULES if not fn(text)]

def revise_once(text: str) -> str:
    out = text
    if "badword" in out.lower():
        out = out.replace("badword", "[redacted]")
    for w in ("stupid", "idiot"):
        out = out.replace(w, "unhelpful").replace(w.capitalize(), "Unhelpful")
    if "password" in out.lower():
        out = out.replace("password", "[removed]")
    return out

def constitutional_loop(text: str, max_rounds: int = 5) -> RevisionResult:
    current = text
    for i in range(max_rounds):
        v = critique(current)
        if not v:
            return RevisionResult(current, i, [])
        current = revise_once(current)
    return RevisionResult(current, max_rounds, critique(current))
