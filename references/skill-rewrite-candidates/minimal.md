# minimal

## Goal

Keep only the rules that protect the official exam contract and basic sample tone.

## Draft

- Turn a Kaggle tabular source into an AICE Associate-style exam package.
- Always create `problem.ipynb`, `solution.ipynb`, `data/raw/`, and `data/submissions/`.
- Keep exactly `14문항`.
- Follow the official ranges: `데이터 분석 5~6 / 30점`, `데이터 전처리 4~5 / 30점`, `AI 모델링 4~5 / 40점`.
- Write in Korean and keep the notebooks exam-like, not tutorial-like.
- Put `샘플문항`, `[유의사항]`, domain, goal, scenario, and a column table before question 1.
- Keep problem and solution notebooks in the same question order.
- Inspect the real data first and use real columns, paths, and metrics.

## Tradeoff

Shortest option, but weakest control over sample-like cell rhythm and answer-sheet tone.
