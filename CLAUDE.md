# adp-cloud-trial — read first

This repo runs the Agentic Development Protocol (ADP). Cloud threads do not run
ADP's hooks, so these rules are on you; CI ("ADP checks", "Tests") is the gate.

- You are the **developer** unless told otherwise. Read `docs/prompts/developer.md`
  and `docs/prompts/process.md`, then pick up the task named in the Dispatch block
  of `docs/tasks/current.md`.
- **Never edit `docs/tasks/current.md`** or `.adp/`. Report the result in the PR
  description; the architect records it.
- Edit only `src/` and `tests/`. Never touch `.github/` or `.claude/`.
- Every behaviour change ships with a test. Run `python3 -m unittest discover -s tests -v`.
- Conventional commits only (`feat:`, `fix:`, `test:` …). Stage files by exact path.
- Work on a branch and open a pull request to `main`; never push to `main`.
