# Active Tasks

**All sessions read this file on startup.** The Dispatch block below tells each session what to pick up next. See `docs/prompts/process.md` for the full protocol (§3 task dispatch, §3a Dispatch block, §4a commit hygiene, §5a Gate 0, §9 session lifecycle, §10 archive convention).

---

## Dispatch — architect-maintained (updated 2026-11-04)

### Status snapshot
- Trial repo for ADP in a cloud project. App = `src/tally.py` (word counter), 2 tests green. T1 and T2 dispatched to developer.

### Developer session (next)
- **Pick up:** T1 — top-N words
- **After T1:** T2
- **Do not start:** —
- **Context budget:** end session at ≤30% remaining
- **Standing reminders:** Gate 0 on every bug. Stage by exact path; `git status --short` before every commit.

### Designer session (next)
- **Pick up:** no pickup pending
- **After:** —
- **Context budget:** end session at ≤30% remaining
- **Standing reminders:** Preserve load-bearing test selectors. New i18n strings land in all locales in the same commit.

### Reviewer queue (optional — delete if not using reviewer role)
- (list tasks awaiting reviewer verdict, in order)

### User actions pending (no session needed)
- (list items only the human can do: domain registration, console toggles, manual deploys, etc.)

---

## Architecture rules ratified
(Architect: as the project ratifies rules over time, list them here for free lookup. Each rule should be a one-liner with a date and a brief rationale. Example: "2026-06-01: All new strings must use the translation hook (no hardcoded en-only). Reason: post-launch i18n audit caught 14 hardcoded strings.")

---

## Process misses log
(Architect: when a session skips a process rule and it costs time, log it here so the pattern is visible. Format: "MISS YYYY-MM-DD: {what was skipped} → {cost in time/effort} → {rule that should have caught it}". Keeps the rules honest.)

---

## Active tasks

(Tasks live here. Use the format below — see process.md §3 for the canonical spec.)

### T1: Add top_words(text, n)
- **Agent:** developer
- **Status:** NEW
- **Plan:** none (trial task)
- **Priority:** P1
- **Created:** 2026-11-04

**Instruction:**
In `src/tally.py` add `top_words(text: str, n: int) -> list[tuple[str, int]]` returning the n most frequent words (ties broken alphabetically), built on `count_words`. Add tests in `tests/test_tally.py`. Open a pull request against `main`.

**What NOT to change:**
`count_words` behaviour, `.github/`, `.claude/`, this task file (the architect records results).

**Acceptance criteria:**
- [ ] `python3 -m unittest discover -s tests -v` passes with new tests for ties and n larger than the vocabulary
- [ ] PR checks "ADP checks" and "Tests" are green

**Result:**
(Recorded by the architect from the developer's report.)

### T2: Ignore digits-only tokens
- **Agent:** developer
- **Status:** NEW
- **Plan:** none (trial task)
- **Priority:** P2
- **Created:** 2026-11-04

**Instruction:**
`count_words` must skip tokens made only of digits ("2026", "42"). Add a test. Open a pull request against `main`.

**What NOT to change:**
`.github/`, `.claude/`, this task file.

**Acceptance criteria:**
- [ ] New test covers "in 2026 we had 42 cats" → {"in","we","had","cats"}
- [ ] PR checks green

**Result:**
(Recorded by the architect from the developer's report.)

---

## Archive index (last 10 closed tasks — free lookup)

(Architect: after archiving a task, add a one-line entry here so future sessions can answer "what did T-X do?" without opening the archive file.)

- (none yet)

---

*End of current.md.*
