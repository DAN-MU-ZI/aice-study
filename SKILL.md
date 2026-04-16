---
name: kaggle-aice-associate-builder
description: "Build official AICE Associate problem/solution notebooks from a Kaggle tabular source, using Korean sample-exam tone and the 14-question 30/30/40 structure."
---

# Kaggle AICE Associate Builder

Turn a Kaggle tabular source into an AICE Associate-style exam package that reads like the provided sample exam, not a tutorial notebook.

## Outputs

- Create all of the following under a dataset-specific notebook folder:
- `problem.ipynb`
- `solution.ipynb`
- `data/raw/`
- `data/submissions/`
- Use these notebook filenames as fixed canonical names. Do not rename them to dataset-specific forms such as `<slug>.ipynb` or `<slug>_solution.ipynb`.
- If Docker is available, prefer it and keep the exact run command for the final response.

## Official Structure

- Produce exactly `14문항`.
- Follow the current official ranges: `데이터 분석 5~6문항 / 30점`, `데이터 전처리 4~5문항 / 30점`, `AI 모델링 4~5문항 / 40점`.
- Treat sample notebooks as style references only. Do not copy their older `20/30/50` scoring.
- Use direct coding as the default question type. Add bug-fixing, blank-filling, or interpretation only where they improve sample fidelity.

## Sample-First Format

- Match the sample tone at the top of both notebooks: `샘플문항`, `[유의사항]`, domain, goal, short business scenario, and a dataset-specific column description table before question 1.
- Keep the writing in Korean, short, imperative, and exam-like.
- Save notebooks and any Korean text artifacts in UTF-8.
- Problem and solution notebooks must share the same question order and nearly the same cell rhythm.
- The problem notebook must not contain final answers, partially solved answer code, hidden worked code, ready-to-run imports that directly answer a question, final metric values, or direct textual answer hints.
- The solution notebook should read like a reference answer sheet, with completed code and short answer-style notes only.
- Use explicit section headers with point labels and sample-like answer cells.

## Dataset Rules

- Inspect the real data before drafting. Confirm task type, target, row counts, likely ID columns, missingness, categorical vs numeric columns, and submission shape.
- Use real file names, paths, columns, and variable names after inspection. Do not leave placeholders.
- Do not force a canned preprocessing recipe. Check that null handling, outlier handling, encoding, scaling, metrics, and models fit the data.
- Include a small deep-learning section when the environment and dataset make it reasonable; otherwise replace it with another modeling question and explain that choice in the solution notebook.

## Verification

- Verify that all required artifacts exist, the section split stays within the official ranges, and both notebooks are runnable top to bottom with matching question order.
- Verify that the problem notebook does not leak answers. Check for filled answer cells, completed bug-fix cells, precomputed `answer_*` variables, solved blank placeholders, or markdown text that reveals the expected answer directly.
- Prefer output-first verification: execute `solution.ipynb`, then inspect the executed notebook outputs and generated artifacts directly.
- Treat charts, printed metrics, saved submission files, and notebook-visible tables as the primary evidence of correctness.
- If a `.py` validator is used, keep it as a thin runner/checker around the executed notebook and generated files. Do not re-implement the full answer logic in the validator unless the user explicitly asks for a recomputation-based checker.
- Before finishing the task, perform one final review pass over the generated package. Re-check file naming, question counts, section score ranges, answer leakage in `problem.ipynb`, and whether the executed outputs in `solution.ipynb` still match the intended exam flow.
- Read `references/aice-associate-blueprint.md` once before drafting and use it for detailed cell patterns and question-type examples.
