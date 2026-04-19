# AICE Associate Blueprint

Use this file as the detailed contract for drafting or reviewing an AICE-style notebook package.

For canonical markdown/code block shapes, also load `references/notebook-snippets.md`. Keep this file focused on notebook-pair behavior, section planning, and dataset-adaptation guidance.

## Source of Truth

Use the current official structure as the scoring authority:

- `데이터 분석 5~6문항 / 30점`
- `데이터 전처리 4~5문항 / 30점`
- `AI 모델링 4~5문항 / 40점`
- Total: `14문항 / 100점 / 90분`

Ignore any legacy `20/30/50` material. The official structure above is the only scoring source of truth.

## Core Package Shape

Always create:

- `problem.ipynb`
- `solution.ipynb`
- `data/raw/`
- `data/submissions/`

Use `problem.ipynb` and `solution.ipynb` as fixed canonical filenames. Do not replace them with dataset-specific notebook names.

## Notebook Pair Contract

Draft order is mandatory:

1. write `solution.ipynb` first
2. verify the solved notebook structure, variable names, metrics, artifacts, and cell roles
3. derive `problem.ipynb` from that solved notebook without changing question order, cell rhythm, or answer surface

Do not invent the exam scaffold independently and then backfill the solution later.

### Problem Notebook

Make the problem notebook look like a real exam paper.

Include:

- exam-style title banner
- domain
- goal
- short business scenario
- `[주의사항]`
- column description table
- section headers with point labels
- answer cells, blank cells, or intentionally wrong starter code when needed
- guide markdown blocks that state dataframe names, variable names, helper functions, and exact constraints when the question requires them
- placeholder-based starter code for scaffold-heavy preprocessing or modeling items when partial-code solving is the intended assessment format
- separate written-answer cells for interpretation items when evidence generation and textual explanation should be graded separately

Do not include final answers, final `answer_*` variables, hidden worked code, partially completed answer code, already-correct starter code for a scored item, precomputed metric values, or direct textual hints that reveal the answer.
Build the problem notebook by subtracting answers from the solved notebook, not by redesigning the flow from scratch.

### Solution Notebook

Keep the same question order and almost the same cell layout as the problem notebook.

Add:

- completed code
- visible outputs for charts, metrics, and final submission generation
- short reference-answer notes only

Do not turn the solution notebook into a long-form tutorial.
Treat the solution notebook as the canonical source of truth for execution order, helper variables, metrics, and generated artifacts.

The solution notebook must preserve the visible answer form of the problem notebook. If the problem notebook uses a dedicated written-answer cell, direct `answer_n =` cell, or split `(N-1)` / `(N-2)` structure, keep that same structure in the solution notebook rather than routing through a separate helper-answer convention.

## Required Front Matter

Write the following before question 1:

- exam title
- domain
- goal
- short business scenario tied to the dataset
- `[주의사항]` in Korean
  - 각 문항의 답안은 반드시 지정된 답안 셀에 입력해야 합니다.
  - 제공된 시험문항 셀을 삭제하거나 답안 위치가 아닌 다른 셀에 답안을 작성하면 채점되지 않습니다.
  - 답안 작성 전에 문항에 제시된 가이드를 확인해야 합니다.
  - 문항에 변수명이 제시된 경우 반드시 해당 변수명을 사용해야 합니다.
  - 제출 파일 경로가 제시된 경우 반드시 해당 경로를 사용해야 합니다.
- column description table based on actual dataset columns

Do not rely on any external exam reference to decide tone or layout. Derive both from the official structure and the rules in this file.

## Canonical Structure Contract

Treat this blueprint as the contract for block rhythm and scaffolding density.

Match the canonical structure on:

- how often title markdown and guide markdown are separated
- when a question uses `(N-1)`, `(N-2)` style subparts
- when a chart or metric question also requires a separate written answer cell
- when starter code contains blanks instead of an empty answer cell
- when setup/import cells appear before dependent questions
- when a model topology diagram or equivalent visual scaffold is part of the prompt

Avoid these drifts away from the canonical structure:

- collapsing a guide markdown cell into a shorter title-only question
- replacing blank-filled starter code with a generic comment-only code cell
- removing explicit variable names, helper function names, seeds, split ratios, metric names, output paths, or callback names that the problem statement should state
- compressing a multi-step question into one vague instruction
- introducing a solution-only helper-answer cell that has no visible partner in the problem notebook

## Guide Minimum Contract

Guide markdown is required when the student needs any of the following to answer correctly:

- dataframe or series name
- target variable name
- train/valid split ratio
- seed or `random_state`
- `stratify` requirement
- metric name
- file path or save path
- explicit output variable name such as `answer_7`
- helper function or model argument that the problem intends to assess

A title-only question is acceptable only when the task is genuinely trivial and no hidden constraints are needed.

## Question Types

Use direct coding as the default form. Add the other types only when they improve assessment quality or fit the dataset naturally.

### Type A: direct coding

Typical pattern:

1. Markdown title cell
2. Markdown guide cell when constraints matter
3. Code answer cell

Prefer explicit guide bullets such as dataframe name, variable name, ratio, seed, metric, or output path when the task depends on them.

### Type B: bug fixing

Use when a preprocessing or modeling step benefits from correcting realistic starter code.

Prefer realistic broken starter code plus a narrow fix target over a generic "오류를 정정하시오" instruction alone.

The fix target should be concrete enough that the student can identify what to change, and narrow enough that the answer surface stays stable between `problem.ipynb` and `solution.ipynb`.

### Type C: fill in the blanks

Use sparingly for modeling or evaluation steps that benefit from answer placeholders.

This is especially useful when students should complete method names, callback arguments, model-layer fragments, or key exclusion lists inside starter code.

Do not convert a placeholder-based block into a generic blank answer cell during derivation.

### Type D: result interpretation

Use when the student must read a real chart, metric, or table and type the result.

When evidence generation and written interpretation are distinct skills, preserve that split across two answer cells or one code cell plus one written-answer cell.

## Cell Rhythm Guardrail

Before finalizing a question block, ask:

1. Should this block use more than one cell for clarity or grading separation?
2. Should this block provide bullet guidance instead of one sentence?
3. Should this block use placeholders or starter code instead of a blank comment cell?
4. Should this block require a separate written answer cell for the interpreted result?
5. Should the solution notebook preserve the exact same answer surface and cell roles for this block?

If the answer is yes, keep the richer scaffold.

## Explicit Failure Patterns

Treat these as structure failures, not minor style issues:

- guide omission in a block that depends on named inputs, outputs, ratios, metrics, or paths
- a generic comment-only code cell where a guide or starter-code scaffold should exist
- a bug-fix prompt that does not expose a realistic broken code target
- a chart-reading question that loses its separate interpretation answer surface
- `answer_*_blank_*`, `answer_*_model`, or similar helper-answer patterns that are not visible as part of the graded problem structure
- any post-split evaluation block that drifts from `X_valid`, `y_valid` to train-all or test data without explicit question intent

## Official Section Plan

### 1. 데이터 분석 [5~6문항 / 30점]

- 필요한 라이브러리 로딩
- 데이터 구성 및 특성 파악
- 데이터 요약과 시각화

### 2. 데이터 전처리 [4~5문항 / 30점]

- 결측치 및 이상치 처리
- 데이터 정리
- 인코딩 또는 스케일링
- Train/Valid 분리

### 3. AI 모델링 [4~5문항 / 40점]

- 머신러닝 모델 학습
- 딥러닝 모델 학습 또는 합리적 대체 문항
- 모델 성능 평가 및 비교
- 최종 제출 생성 또는 성능 개선 시각화

## Distribution Strategy

- `5-4-5` is only an anchor pattern, not a fixed rule.
- Shift by one question within the official ranges when the dataset needs more analysis or preprocessing, such as `6-4-4` or `5-5-4`.
- Keep the total at `14문항` and the section points at `30/30/40`.
- Make the modeling section large enough to cover ML, evaluation, and one deep-learning or replacement task.

## Example 14-Question Flow

One common anchor flow is:

1. Library import
2. Data loading
3. Basic data check
4. Visualization setup
5. Distribution or relationship analysis
6. Outlier or ID-column handling
7. Missing-value handling
8. Encoding or scaling
9. Train/valid split
10. First ML model
11. Second ML model or feature importance
12. Metric evaluation and comparison
13. Deep-learning construction or justified replacement task
14. Submission generation or learning-curve style follow-up

Use this as a canonical rhythm anchor, not a mandatory one-to-one script.

## Dataset Adaptation Guardrails

Inspect the real data first. Confirm:

- train/test row counts
- target column
- likely ID columns
- missing-value ratios
- categorical vs numeric columns
- whether the task expects a submission file

Do not copy a generic preprocessing recipe without checking its effect.

Avoid:

- `dropna()` when it would remove nearly all rows
- plotting columns that do not exist
- unjustified encoding of high-cardinality free text
- metrics that conflict with the task goal

If the competition exposes an official metric, use it in at least one modeling question when feasible.

When train/valid split has been introduced, keep later model comparison, confusion-matrix, threshold, and deep-learning validation blocks on the `X_valid`, `y_valid` path unless the question explicitly switches to final submission generation.

## Deep Learning Guidance

If TensorFlow is available and the dataset size is reasonable, include at least one neural-network question plus one related evaluation or history-plot question.

If deep learning is unrealistic, replace it with another modeling or interpretation task and explain why in the solution notebook.

When deep learning is included and the question is scaffold-heavy, preserve the same level of guidance:

- setup notice markdown before the graded question
- dedicated import/setup code cell
- explicit architecture constraints
- exact optimizer, loss, metric, callback, epoch, and batch-size requirements when the question design depends on them
- topology diagram or equivalent visual reference when architecture is part of the graded prompt
- prefer an image asset rendered from Mermaid source or an equivalent diagram source, then embed it in the notebook markdown so the architecture is visible in both `problem.ipynb` and `solution.ipynb`
- when starter code asks the student to fill architecture blanks, place the rendered architecture image immediately before the setup notice or starter cell and keep the image consistent with the solution architecture
- placeholder-based starter code when the student is not expected to write the entire block from scratch

## Writing Rules

- Write notebook text in Korean by default.
- Save notebooks, markdown files, CSV summaries, and other Korean text artifacts in UTF-8 without BOM.
- Use concrete paths, file names, columns, and variables once the dataset is known.
- Keep section labels and point labels explicit.
- Use short, imperative exam wording.
- Keep code runnable from top to bottom.
- Do not optimize away scaffold repetition if that repetition is part of the exam format.

## Verification Preference

Prefer format-first review, then execution-first review.

The default verification flow is:

1. inspect notebook pair structure, section counts, question rhythm, guide density, and answer leakage
2. confirm the problem and solution notebooks still share the same question order and visible answer surface
3. execute `solution.ipynb`
4. inspect notebook-visible outputs such as charts, printed metrics, tables, and saved-file messages
5. inspect generated artifacts such as submission files or summary CSVs
6. inspect `problem.ipynb` to ensure scored answer cells are still blank, intentionally incomplete, or intentionally incorrect as designed
7. perform one final review pass before closing the task, checking naming, section counts, score distribution, answer leakage, notebook flow, and validation-data consistency one more time

A `.py` validator may be used as a thin automation wrapper for notebook execution and artifact checks.
Avoid writing validators that fully recompute the notebook answers from scratch unless the user explicitly asks for a second independent checker.
