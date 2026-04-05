---
name: kaggle-aice-associate-builder
description: "Build AICE Associate-style Kaggle practice sets from a competition or dataset. Use when Codex must inspect a Kaggle tabular source and generate a realistic exam package in Jupyter format: a problem notebook, a worked-solution notebook, raw/submission folders, and a validation script. Best for regression or classification tasks that need Korean exam wording, mixed A/B/C/D question types, dataset-specific preprocessing, and Docker-friendly execution."
---

# Kaggle AICE Associate Builder

Create a runnable AICE-style mock exam package from a Kaggle source. Mirror the look and flow of a real AICE exam paper, not a generic tutorial notebook.

## Required Outputs

Always create all of the following under a dataset-specific folder in the workspace notebook area:

- `<slug>.ipynb` for the exam paper
- `<slug>_solution.ipynb` for the worked solution
- `data/raw/`
- `data/submissions/`
- `tests/validate_notebook.py`

If Docker is available, prefer Docker execution and keep the exact command you used ready for the final response.

## Workflow

1. Resolve the Kaggle source with Kaggle MCP.
If the user provides a competition or dataset name, fetch metadata first. If access is blocked by authentication or competition acceptance, surface that immediately.

2. Inspect the dataset before drafting anything.
Identify the main train/test files, target column, task type, ID columns, missing-value pattern, categorical columns, row counts, and whether the dataset naturally supports submission generation.

3. Read `references/aice-associate-blueprint.md` before writing notebooks.
Treat that file as the structure contract for the paper.

4. Design the exam package before writing cells.
Choose a valid 14-question mix and map each question to actual dataset columns and realistic preprocessing/modeling steps.

5. Write the problem notebook first.
Make it look like a real exam sheet: scenario text, cautions, column table, scored sections, and answer cells with blanks or incorrect starter code where appropriate.

6. Derive the solution notebook from the problem notebook.
Keep the same question order and same structure, then fill in code, answers, and short explanations.

7. Add validation after the notebooks exist.
Execute the solution notebook end to end and verify outputs, required `answer_*` variables, metrics, and submission file structure.

8. Verify end to end.
If Python or Docker is available, run the validation script yourself before finishing.

## Hard Rules

- Keep exactly 14 scored questions. Count subparts carefully.
- Prefer any user-provided sample exam over generic defaults. Match its tone, section headers, point style, and cell conventions unless the user says otherwise.
- Write notebook text in Korean unless the user asks for another language.
- Include exam front matter: title, domain, goal, scenario, cautions, and a column description table tied to the actual dataset.
- Use mixed A/B/C/D question types across the paper. Do not make all 14 questions direct coding tasks.
- Insert setup cells before visualization sections or TensorFlow sections when needed.
- Use concrete file names, paths, and column names. Do not leave placeholders once the dataset is known.
- Check each preprocessing step against the real data before committing to it. Never emit instructions that would obviously collapse the dataset, such as a blind `dropna()` if it would remove nearly all rows.
- Align metrics with the task. Use the competition metric when available and stable. Add a secondary teaching metric only when it improves clarity.
- Keep the solution notebook executable from top to bottom with the repo's available packages whenever feasible.
- Keep `answer_*` variable names stable in the solution notebook for deterministic validation.
- Do not use JSON artifacts as a substitute for the worked solution notebook. The solution notebook itself must contain the completed code and visible outputs.
- Do not stop at a scaffold if local data is already available or can be downloaded in the current environment.

## Deep Learning Rule

Many AICE samples include at least one neural-network question. Include a small deep-learning section when the environment and dataset make it reasonable.

Only omit deep learning when it is genuinely unrealistic or harmful for the task. If you omit it, replace it with another modeling or interpretation question and state the reason in the solution notebook.

## Validation Expectations

- Execute the solution notebook from start to finish.
- Verify required `answer_*` variables and key numeric outputs.
- Verify metric artifacts if the notebook writes them.
- Verify submission file schema and row count when the dataset supports submission generation.
- Verify both notebooks exist and share the same question order.

## Reference

Read `references/aice-associate-blueprint.md` before drafting. Use it as the exam-writing contract, especially for notebook pair structure, question-type balance, and failure-mode avoidance.
