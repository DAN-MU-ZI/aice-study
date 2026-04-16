# sample_locked

## Goal

Maximize resemblance to the sample exam while keeping the official current scoring structure.

## Draft

- Turn a Kaggle tabular source into an AICE Associate-style exam package that reads like the provided sample exam, not a tutorial notebook.
- Always create `problem.ipynb`, `solution.ipynb`, `data/raw/`, and `data/submissions/`.
- Keep exactly `14문항`.
- Follow the current official ranges: `데이터 분석 5~6문항 / 30점`, `데이터 전처리 4~5문항 / 30점`, `AI 모델링 4~5문항 / 40점`.
- Treat sample notebooks as style references only. Do not copy their older `20/30/50` scoring.
- Match the sample tone at the top of both notebooks: `샘플문항`, `[유의사항]`, domain, goal, short business scenario, and a dataset-specific column description table before question 1.
- Keep the writing in Korean, short, imperative, and exam-like.
- Problem and solution notebooks must share the same question order and nearly the same cell rhythm.
- The problem notebook must not contain final answers or hidden worked code.
- The solution notebook should read like a reference answer sheet, with completed code and short answer-style notes only.
- Use explicit section headers with point labels and sample-like answer cells.
- Inspect the real data before drafting and use real file names, paths, columns, and variables after inspection.
- Do not force a canned preprocessing recipe. Check that null handling, outlier handling, encoding, scaling, metrics, and models fit the data.
- Include a small deep-learning section when the environment and dataset make it reasonable; otherwise replace it with another modeling question and explain that choice in the solution notebook.
- Verify that all required artifacts exist, the section split stays within the official ranges, and both notebooks are runnable top to bottom with matching question order.

## Tradeoff

Strongest sample fidelity, but the most likely to feel rigid on unusual datasets.
