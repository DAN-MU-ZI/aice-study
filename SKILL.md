---
name: kaggle-aice-associate-builder
description: "Build official AICE Associate problem/solution notebooks from a Kaggle tabular source, using Korean exam tone and the 14-question 30/30/40 structure."
---

# Kaggle AICE Associate Builder

Turn a Kaggle tabular source into an AICE Associate-style exam package that feels like a real exam notebook, not a tutorial and not a generic practice sheet.

This file is the operating procedure and final checklist. Put notebook design and question-structure decisions under `references/aice-associate-blueprint.md`, and use `references/notebook-snippets.md` for canonical block markdown/code shapes.

## Required Reference

Read:

1. `references/aice-associate-blueprint.md`
2. `references/notebook-snippets.md`

Use the references this way:

- `SKILL.md`: execution procedure, environment rules, and final review checklist
- `references/aice-associate-blueprint.md`: package shape, notebook-pair contract, section plan, question design rules, and adaptation guidance
- `references/notebook-snippets.md`: canonical Block Set markdown/code templates for notebook cells

## Execution Environment

- Prefer Docker when available.
- Treat Docker as the default execution path for generation, notebook runs, and validation when the repo already provides a working container.
- Do not assume host `python` is available or correctly configured.
- Treat host-side Windows PowerShell notebook writes as unsafe unless the write path is explicitly BOM-free.
- Prefer the Jupyter container and Jupyter MCP for notebook-native editing, inspection, execution, and verification.
- If Jupyter MCP appears unavailable, distinguish between:
  - the MCP server being down, and
  - the current Codex session not having loaded the MCP registration.
- Before giving up on Jupyter MCP, check the repository MCP config and endpoint health first.
- Fall back to direct `.ipynb` file editing only when Jupyter MCP is unavailable or unhealthy.
- In the final response, record the exact Docker command used when Docker was involved.

### Jupyter MCP Sanity Check

Before concluding that Jupyter MCP cannot be used, verify these in order:

1. the repo config points to the expected MCP server
2. the Jupyter MCP container is running
3. the MCP endpoint path and transport are correct
4. the MCP auth token matches the repo configuration
5. the current Codex session actually exposes the `jupyter` MCP namespace

If `localhost:4040/mcp` is healthy but the `jupyter` tools are missing in-session, treat it as a session-registration issue, not as a notebook-server issue.

## Working Procedure

1. Inspect the real dataset before writing any question.
2. Confirm task type, target column, file names, row counts, likely ID columns, missingness, class balance, and submission shape.
3. Design the notebook package strictly from `references/aice-associate-blueprint.md`.
4. Draft `solution.ipynb` first so the full workflow, variable names, metrics, and artifacts are fixed before exam scaffolding is written.
5. Derive `problem.ipynb` from the completed solution notebook by preserving question order and cell rhythm while removing answer leakage.
6. Use `references/notebook-snippets.md` only for exact block shapes, not for changing the blueprint logic.
7. Generate both notebooks and required artifacts under the dataset folder.
8. Run execution and validation, preferably through Docker.
9. Perform the final review checklist in this file before finishing.

## Non-Negotiables

- Follow `references/aice-associate-blueprint.md` for package shape, official structure, notebook skeleton, question types, problem-vs-solution rules, dataset adaptation, and deep-learning design.
- Treat `solution.ipynb` as the source notebook and derive `problem.ipynb` from it after the solved workflow is stable.
- Keep the writing in Korean, short, imperative, and exam-like.
- Write the problem notebook in Korean. Problem statements, section titles, cautions, guides, and prompts must be Korean.
- Use concrete dataset-specific paths, file names, columns, variables, metrics, and artifacts.
- Do not bypass the blueprint with a simplified ad hoc layout.
- Do not leak solved answers, solved placeholders, or final textual answers into `problem.ipynb`.
- Generated `.ipynb` files must be encoded as UTF-8 without BOM.
- When using repo generators, prefer direct `docker compose run --rm --no-deps jupyter ...` execution over host execution.
- Store reusable dataset profiles under `scripts/aice_generator/specs/`, not under a top-level `scripts/profiles/` directory.

## Anti-Patterns To Avoid

- Do not collapse scaffold-heavy blocks into one markdown cell plus one code cell.
- Do not replace dataset-specific wording with generic cookbook instructions.
- Do not invent variable names, metrics, or file paths disconnected from the real dataset.
- Do not silently switch modeling formulations inside the same graded block.

## Verification Checklist

Before finishing, verify all of the following:

- the notebooks and folder layout match `references/aice-associate-blueprint.md`
- the question count, section distribution, and notebook rhythm match the blueprint
- `problem.ipynb` contains no answer leakage
- `solution.ipynb` runs top to bottom
- generated files under `data/submissions/` are created when required
- deep-learning blocks are internally consistent from prompt to solution when present
- execution and validation were run through Docker when Docker was available
- notebook bytes do not start with UTF-8 BOM (`EF BB BF`)

Perform one final format pass before ending:

- inspect the top matter against the blueprint
- inspect one data-analysis block
- inspect one preprocessing block
- inspect one modeling block
- inspect the deep-learning block against the blueprint when present
- if the notebook feels materially too short or too dense, expand it before shipping
