---
name: operational-quick-ref
description: Repo architecture, key paths, run/test/deploy commands. DO trigger at session start for any code role. Do NOT trigger for pure planning/review sessions.
---

# Operational quick reference

**Purpose:** the answers every code session otherwise re-derives — what runs where, how to start it, how to test it. Fill the placeholders once at install; keep ≤150 lines.

## Architecture in five lines

<<<ARCHITECTURE_SUMMARY>>>
(e.g. "FastAPI backend under api/, React frontend under web/src/, Postgres via docker-compose, deploys to Cloud Run via deploy.sh")

## Key paths

| What | Where |
|---|---|
| Backend entrypoint | <<<BACKEND_ENTRY>>> |
| Frontend entrypoint | <<<FRONTEND_ENTRY>>> |
| Config / env | <<<CONFIG_PATHS>>> |
| Migrations | <<<MIGRATIONS_PATH>>> |
| CI definition | <<<CI_PATH>>> |

## Commands

| Action | Command |
|---|---|
| Run local stack | python3 -c "import sys; sys.path.insert(0,'src'); from tally import count_words; print(count_words('a a b'))" |
| Full test suite | python3 -m unittest discover -s tests -v |
| Single test file | <<<TEST_ONE_CMD>>> |
| Lint / typecheck | <<<LINT_CMD>>> |
| Build | <<<BUILD_CMD>>> |
| Deploy (gated — see process.md §8) | <<<DEPLOY_CMD>>> |

## Gotchas (n≥2 only — anecdotes stay in the process-miss log)

- <<<GOTCHA_1>>>
