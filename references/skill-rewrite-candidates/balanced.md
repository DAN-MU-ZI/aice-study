# balanced

## Goal

Preserve the official exam structure while keeping the most important sample-style surface cues.

## Draft

- Turn a Kaggle tabular source into paired AICE Associate 문제지/해설지 notebooks.
- Always create `problem.ipynb`, `solution.ipynb`, `data/raw/`, and `data/submissions/`.
- Keep exactly `14문항` and stay within `5~6 / 4~5 / 4~5` with `30 / 30 / 40` scoring.
- Match the sample-style top block: `샘플문항`, `[유의사항]`, domain, goal, short business scenario, and a dataset-specific column table.
- Keep the writing short, imperative, and Korean.
- Use direct coding as the default, then add bug-fixing, blank-filling, or interpretation where they fit the sample style.
- Keep problem and solution notebooks in the same question order and nearly the same cell rhythm.
- Make the solution notebook read like a reference answer sheet, not a tutorial.
- Inspect the data first and only then choose preprocessing, metrics, and model flow.

## Tradeoff

Best balance between prompt size and style control, but less rigid than a sample-locked draft.
