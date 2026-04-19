---
name: kaggle-aice-associate-builder
description: "Build official AICE Associate problem/solution notebooks from a Kaggle tabular source, using Korean exam tone and the 14-question 30/30/40 structure."
---

# Kaggle AICE Associate Builder

Turn a Kaggle tabular source into an AICE Associate-style exam package that feels like a real exam notebook, not a tutorial and not a generic practice sheet.

This file is the operating procedure and final checklist. Put notebook design and question-structure decisions under `references/aice-associate-blueprint.md`, and use `references/notebook-snippets.md` for canonical block markdown/code shapes.

## Single Source of Truth

Treat the rule stack as follows:

- `SKILL.md`: execution procedure, environment rules, preflight, failure conditions, and final review checklist
- `references/aice-associate-blueprint.md`: package shape, notebook-pair contract, section plan, question design rules, and structure guardrails
- `references/notebook-snippets.md`: canonical Block Set markdown/code templates for notebook cells

Do not duplicate or weaken a rule in a lower layer. If two files seem to disagree, resolve the conflict in favor of the higher layer and then update the lower layer to match.

The stable core rules are:

- Docker-first
- `solution.ipynb` first, `problem.ipynb` derived second
- `14` scored questions with `30/30/40` section weights
- no answer leakage in `problem.ipynb`
- format-first validation before execution-first validation
- sample-level cell rhythm and guide detail

## Required References

Read:

1. `references/aice-associate-blueprint.md`
2. `references/notebook-snippets.md`

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

## Common Preflight

Run a short preflight before generation or validation. Stop early if a required condition is not met.

Check:

1. Docker availability and whether the intended service image can run
2. Jupyter or Jupyter MCP availability when notebook-native work is expected
3. whether host `python` is being relied on by mistake
4. dataset access path, output directory, and required folder readiness
5. network need versus actual network availability
6. Git lock or workspace state issues that would block artifact writes
7. UTF-8 without BOM safety for any notebook write path

If preflight fails, do not continue into notebook drafting and do not improvise a weaker host-side path without stating that the preflight failed.

## Working Procedure

1. Inspect the real dataset before writing any question.
2. Confirm task type, target column, file names, row counts, likely ID columns, missingness, class balance, and whether the exam should use only the public training file.
3. Design the notebook package strictly from `references/aice-associate-blueprint.md`.
4. Draft `solution.ipynb` first so the full workflow, variable names, metrics, artifacts, and cell roles are fixed before exam scaffolding is written.
5. Derive `problem.ipynb` from the completed solution notebook by preserving question order, cell rhythm, and cell role while removing answer leakage.
6. Use `references/notebook-snippets.md` only for exact block shapes, not for changing the blueprint logic.
7. Generate both notebooks and required artifacts under the dataset folder.
8. Perform a format-first review before running execution-heavy validation.
9. Run execution and validation, preferably through Docker.
10. Perform the final review checklist in this file before finishing.

## Non-Negotiables

- Follow `references/aice-associate-blueprint.md` for package shape, official structure, notebook skeleton, question types, problem-vs-solution rules, dataset adaptation, and deep-learning design.
- Treat `solution.ipynb` as the source notebook and derive `problem.ipynb` from it after the solved workflow is stable.
- Keep the writing in Korean, short, imperative, and exam-like.
- Write the problem notebook in Korean. Problem statements, section titles, cautions, guides, and prompts must be Korean.
- Use concrete dataset-specific paths, file names, columns, variables, metrics, and artifacts.
- For Kaggle competitions, treat extra competition files such as `test.csv` or sample submissions as reference-only unless the user explicitly asks for a submission-style task. Default to `train.csv`-only exam flow when one-file execution matches the sample exam style better.
- Do not bypass the blueprint with a simplified ad hoc layout.
- Do not leak solved answers, solved placeholders, or final textual answers into `problem.ipynb`.
- Do not add helper answer variables such as `answer_*_blank_*` or `answer_*_model` unless the grading structure truly requires them and the same role is visible in the problem notebook.
- Keep the answer form stable between the paired notebooks. If the problem notebook shows a dedicated answer cell or direct `answer_n =` cell, the solution notebook must solve in that same cell shape instead of introducing an alternate answer path.
- Generated `.ipynb` files must be encoded as UTF-8 without BOM.
- When using repo generators, prefer direct `docker compose run --rm --no-deps jupyter ...` execution over host execution.
- Keep the generation profile JSON inside the target notebook directory, for example `notebooks/<dataset-dir>/profile.json`, so temporary generation context and outputs stay together.

## Anti-Patterns To Avoid

- Do not collapse scaffold-heavy blocks into one markdown cell plus one generic comment-only code cell.
- Do not replace dataset-specific wording with generic cookbook instructions.
- Do not invent variable names, metrics, or file paths disconnected from the real dataset.
- Do not silently switch modeling formulations inside the same graded block.
- Do not let a graded question end as a title-only prompt when the student needs variable names, split ratios, metrics, file paths, or output constraints.
- Do not introduce solution-only helper cells that change the scoring surface or the visible answer shape.
- Do not let validation or comparison questions drift away from the established `X_valid`, `y_valid` flow after train/valid split has been introduced.

## Failure Conditions

Treat the notebook package as not ready if any of the following is true:

- the section count, point distribution, or question count differs from `14` and `30/30/40`
- `problem.ipynb` leaks solved answers, solved placeholders, or direct textual hints
- question order or cell role differs between `problem.ipynb` and `solution.ipynb`
- a block that should use guide markdown, split answer cells, or starter code has been flattened into a vague shorter block
- answer variables are routed through hidden helper variables instead of the visible graded structure
- validation questions use train-all or test data where the block should continue using `X_valid`, `y_valid`
- the notebook bytes start with UTF-8 BOM

## Verification Checklist

Before finishing, verify all of the following in this order.

### 1. Format-first review

- the notebooks and folder layout match `references/aice-associate-blueprint.md`
- the question count, section distribution, and notebook rhythm match the blueprint
- front matter matches the blueprint and includes the required caution style
- guide density is sufficient for blocks that depend on names, ratios, seeds, metrics, or output paths
- `problem.ipynb` contains no answer leakage
- `problem.ipynb` and `solution.ipynb` preserve the same question order and the same cell role pattern
- no graded block was compressed into a generic comment-only answer cell

### 2. Execution and artifact review

- `solution.ipynb` runs top to bottom
- generated files under `data/submissions/` are created when required
- deep-learning blocks are internally consistent from prompt to solution when present
- post-split validation and comparison steps continue to use `X_valid`, `y_valid` unless the block is the final submission question
- execution and validation were run through Docker when Docker was available
- notebook bytes do not start with UTF-8 BOM (`EF BB BF`)

Perform one final format pass before ending:

- inspect the top matter against the blueprint
- inspect one data-analysis block
- inspect one preprocessing block
- inspect one modeling block
- inspect the deep-learning block against the blueprint when present
- if the notebook feels materially too short or too dense, expand it before shipping
