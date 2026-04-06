---
name: kaggle-aice-associate-builder
description: "Build AICE Associate-style Kaggle practice sets from a competition or dataset. Use when Codex must inspect a Kaggle tabular source and generate a realistic exam package in Jupyter format: a problem notebook, a worked-solution notebook, raw/submission folders, and a validation script. Best for regression or classification tasks that need Korean exam wording, mixed A/B/C question types (Coding, Blank-filling, Interpretation), fixed 14-question flow (30/30/40 pts) matching official syllabus, and Docker-friendly execution."
---

# Kaggle AICE Associate Builder

Create a runnable AICE-style mock exam package from a Kaggle source. Mirror the look and flow of a real AICE exam paper, not a generic tutorial notebook.

## Required Outputs

Always create all of the following under a dataset-specific folder in the workspace notebook area:

- `problem.ipynb` for the exam paper
- `solution.ipynb` for the worked solution (Reference Solution)
- `data/raw/`
- `data/submissions/`


If Docker is available, prefer Docker execution and keep the exact command you used ready for the final response.

## Workflow

1. Resolve the Kaggle source with Kaggle MCP.
If the user provides a competition or dataset name, fetch metadata first. If access is blocked by authentication or competition acceptance, surface that immediately.

2. Inspect the dataset before drafting anything.
Identify the main train/test files, target column, task type, ID columns, missing-value pattern, categorical columns, row counts, and whether the dataset naturally supports submission generation.

3. Read `references/aice-associate-blueprint.md` before writing notebooks.
Treat that file as the structure contract for the paper.

4. Design the exam package before writing cells.
   Strictly follow the 14-question standard sequence defined in the blueprint (30pt Analysis, 30pt Preprocessing, 40pt Modeling). Map each question to actual dataset columns and realistic preprocessing/modeling steps.

5. Write the problem notebook first.
Make it look like a real exam sheet: scenario text, cautions, column table, scored sections, and answer cells with blanks or incorrect starter code where appropriate.

6. Derive the solution notebook from the problem notebook.
Keep the same question order and same structure, then fill in code, answers, and short explanations.

7. Verify the package.
Confirm that the solution notebook is runnable and contains the expected model answers and outputs. Ensure the notebooks share the same question order.
- Ensure each question follows the "AICE Standard Snippet Format" (3-Cell or derivative):
    1. **Title Cell (Markdown)**: `### **N. Task summary.**\n### **아래 가이드에 따라 ... 하세요.**`
    2. **Guide Cell (Markdown)**: Starts with `* **`, followed by `- 대상 데이터프레임 : ...` and specific constraints, ending with a horizontal line `---`. 
       - Use `<font color=blue>` for critical instructions like filling in blanks.
    3. **Answer Cell (Code)**: Standard coding prompt `# (N) 여기에 답안코드를 작성하고 실행하세요.`
       - For blank-filling, use `# (코드 셀) 코드의 빈칸을 채우고 실행하세요` followed by `# (N-1) 여기에 답안을 입력하세요(실행 불필요)` cells.


## Hard Rules

- Keep exactly 14 scored questions. Count subparts carefully.
- Include exam front matter:
    1. **Header**: Exam Title (`AICE Associate <font color=red>연습문제</font>`), Domain, Goal, Scenario.
    2. **Rules**: Standard exam regulations.
    3. **Column Table**: Detailed data dictionary using MD table format, separated by `---`.
- Follow the official point distribution strictly: Data Analysis (30pt), Preprocessing (30pt), and AI Modeling (40pt).
- Use visual branding: Blue bold headers for sections (e.g., `## <font color=blue>**<데이터 분석 (30점)>**</font>`).
- Primarily use direct coding (Type A). Use blank-filling (Type B) for modeling or complex evaluation tasks to mirror sample quality.

- Insert setup cells before visualization sections or TensorFlow sections when needed.
- Use concrete file names, paths, and column names. Do not leave placeholders once the dataset is known.
- Check each preprocessing step against the real data before committing to it. Never emit instructions that would obviously collapse the dataset, such as a blind `dropna()` if it would remove nearly all rows.
- Align metrics with the task. Use the competition metric when available and stable. Add a secondary teaching metric only when it improves clarity.
- Keep the solution notebook executable from top to bottom with the repo's available packages whenever feasible.

- Do not use JSON artifacts as a substitute for the worked solution notebook. The solution notebook itself must contain the completed code and visible outputs.
- Do not stop at a scaffold if local data is already available or can be downloaded in the current environment.

## Deep Learning Rule

Many AICE samples include at least one neural-network question. Include a small deep-learning section when the environment and dataset make it reasonable.

Only omit deep learning when it is genuinely unrealistic or harmful for the task. If you omit it, replace it with another modeling or interpretation question and state the reason in the solution notebook.

## Verification Expectations

- Ensure the solution notebook reflects correct answers for the dataset.
- Verify both notebooks exist and share the same question order.


## Reference

Read `references/aice-associate-blueprint.md` before drafting. Use it as the exam-writing contract, especially for notebook pair structure, question-type balance, and failure-mode avoidance.
