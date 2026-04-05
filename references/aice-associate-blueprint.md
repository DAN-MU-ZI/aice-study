# AICE Associate Blueprint

Use this file as the contract for drafting or reviewing an AICE-style notebook package.

## Non-Negotiable Package Shape

Always create:

- one problem notebook
- one solution notebook
- `data/raw/`
- `data/submissions/`
- `tests/validate_notebook.py`

Do not treat a single notebook as complete output.

## Notebook Pair Contract

### Problem Notebook

Make the problem notebook look like a real exam paper.

Include:

- title
- domain
- objective
- scenario paragraph
- cautions/instructions
- column description table
- section headers with point labels
- answer cells, blank cells, or intentionally wrong code cells

Do not include final answers, final `answer_*` variables, or hidden worked code in the problem notebook.

### Solution Notebook

Keep the same question order and almost the same cell layout as the problem notebook.

Add:

- completed code
- `answer_*` variables for deterministic checks
- short explanations where the student would need interpretation
- visible outputs for charts, metrics, and final submission generation

Do not turn the solution notebook into a long-form tutorial. Keep the style exam-like.

## Required Front Matter

Write the following before question 1:

- exam title
- domain
- goal
- short business scenario tied to the dataset
- cautions/instructions
- column description table based on actual dataset columns

If the user provides a sample exam, mirror its tone and layout first.

## Question Types

Mix these four types across the paper.

### Type A: direct coding

Use for imports, loading data, plotting, splitting data, fitting models.

Typical prompt marker:

```python
# (N) Write the answer code here and run it.
```

### Type B: bug fixing

Provide starter code with real mistakes, then ask the student to correct it.

Typical mistakes:

- wrong method name
- wrong metric import
- wrong `fit_transform` / `transform` use
- wrong attribute such as `feature_importances_`
- wrong prediction target or wrong split variable

### Type C: fill in the blanks

Use placeholders like `<#7-1>` inside a code cell plus separate answer cells.

### Type D: result interpretation

Ask the student to read a chart, metric, or table and type the result in a text-answer cell.

Do not make all text-answer questions trivial. Tie them to actual plots or model outputs.

## Section Plan

Keep exactly 14 scored questions.

Use one of these valid mixes:

- 6 data analysis / 4 preprocessing / 4 modeling
- 5 data analysis / 5 preprocessing / 4 modeling
- 5 data analysis / 4 preprocessing / 5 modeling

Prefer this order unless the dataset strongly suggests another order:

1. imports and data loading
2. basic shape and schema checks
3. one or two EDA plots
4. missing values / duplicates / simple statistics
5. preprocessing
6. encoding or scaling
7. train/validation split
8. machine-learning models
9. feature importance or error analysis
10. deep learning or training-history interpretation
11. final prediction or submission generation

## Dataset Adaptation Guardrails

Inspect the real data first. Confirm:

- train/test row counts
- target column
- likely ID columns
- missing-value ratios by column
- categorical vs numeric columns
- whether the competition expects a submission file

Never copy a generic preprocessing recipe without checking its effect.

Examples of what to avoid:

- `dropna()` when it would remove nearly all rows
- plotting columns that do not exist
- applying label encoding to high-cardinality free-text fields without justification
- using a metric that conflicts with the competition goal when a better aligned metric is available

If the Kaggle competition has an official evaluation metric, use it in at least one modeling question when feasible.

## Deep Learning Guidance

If the environment contains TensorFlow and the dataset size is reasonable, include at least one neural-network question plus one history-plot question. This matches many AICE samples.

If deep learning is unrealistic for the dataset or environment, replace it with another modeling or interpretation question and explain why in the solution notebook.

## Writing Rules

- Write notebook text in Korean by default.
- Use concrete paths, not placeholders, once the dataset is known.
- Keep point labels and section labels explicit.
- Use short, imperative exam wording.
- Keep answer-variable names stable in the solution notebook, such as `answer_3_1`.
- Keep code runnable from top to bottom.

## Validation Rules

The validation script should:

- execute the solution notebook
- confirm required `answer_*` values or artifacts exist
- re-compute important numeric answers when practical
- check model metrics if the notebook writes them
- check submission schema and row count when applicable
- confirm both notebooks exist

## Common Failure Modes

Treat these as hard failures:

- only one notebook is produced
- the notebook reads like a tutorial instead of an exam paper
- all questions are direct coding with no B/C/D variety
- question count is not exactly 14
- preprocessing steps were not checked against the real dataset
- validation checks only file existence and not notebook outputs
