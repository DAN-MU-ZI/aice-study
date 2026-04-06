# AICE Associate Blueprint

Use this file as the contract for drafting or reviewing an AICE-style notebook package.

## Core Package Shape

Always create:

- one problem notebook
- one solution notebook (Reference Solution)
- `data/raw/`
- `data/submissions/`


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
- visible outputs for charts, metrics, and final submission generation
- short explanations of the logic (Reference Answer style)


Do not turn the solution notebook into a long-form tutorial. Keep the style exam-like.

## Required Front Matter

Write the following before question 1:

- exam title
- domain
- goal
- short business scenario tied to the dataset
- instructions (지시사항)
    - 반드시 한국어로 다음 내용을 포함할 것:
        - 각 문항의 답안은 반드시 '# 여기에 답안코드를 작성하세요' 등이 표시된 셀에 입력해야 합니다.
        - 제공된 시험문항 셀을 삭제하거나 답안 위치가 아닌 다른 셀에 답안코드를 작성 시 채점되지 않습니다.
        - 답안 작성 전에 문항에 제시된 지시사항(가이드)을 확인하세요.
        - 문항에 변수명이 제시된 경우 반드시 해당 변수명을 사용하세요.
        - 시험 문항과 데이터 등을 무단으로 촬영/캡처, 공유/유포 시 법적 제재를 받을 수 있습니다.
- column description table based on actual dataset columns

If the user provides a sample exam, mirror its tone and layout first.

## Question Variety (Types)

The exam should primarily consist of direct coding, with other types used optionally to mirror the AICE sample style where appropriate.

### Type A: direct coding (Primary)

Use for imports, loading data, plotting, splitting data, fitting models.

Typical prompt layout across cells:
1. Markdown Cell (Title):
   ```
   ### **N. [Task Objective]**
   ### **아래 가이드에 따라 ... 하세요.**
   ```
2. Markdown Cell (The Guide):
   ```
   * **
   - 대상 데이터프레임 : df
   - [Detailed instruction 1]
   - [Detailed instruction 2]
   ---
   ```
3. Code Cell:
   ```python
   # (N) 여기에 답안코드를 작성하고 실행하세요.
   ```

### Type B: bug fixing (Optional/Strategic)

If specific dataset steps are prone to common errors, provide starter code with intentional mistakes for the student to correct. Treat this as a secondary type to add flavor, not a hard requirement for every paper.

### Type C: fill in the blanks (Optional)

Use placeholders like `<#7-1>` inside a code cell plus separate answer cells.

### Type D: result interpretation

Ask the student to read a chart, metric, or table and type the result in a text-answer cell.

Do not make all text-answer questions trivial. Tie them to actual plots or model outputs.

## Section Plan (Total 100 points, 14 questions, 90 mins)

Follow this official distribution and point structure:

### 1. 데이터 분석 (Data Analysis) [5~6문항 / 30점]
- 필요 라이브러리 설치 (`import`)
- 데이터 구성 및 특성 파악 (`shape`, `info`, `describe`, `head`)
- 데이터 품질 점검 및 시각화 (기본 EDA, 상관관계 등)

### 2. 데이터 전처리 (Data Preprocessing) [4~5문항 / 30점]
- 데이터 결측치/이상치 처리 (`isnull`, `dropna`, `fillna`, `outliers`)
- 데이터 스케일링 및 변환 (`StandardScaler`, `MinMaxScaler`)
- 라벨 인코딩 / 원핫 인코딩 (`LabelEncoder`, `get_dummies`)
- 데이터셋 분할 (`train_test_split`)

### 3. AI 모델링 (AI Modeling) [4~5문항 / 40점]
- 머신러닝 모델 학습 (Linear, Tree, Ensemble 등)
- 딥러닝 모델 학습 (Artificial Neural Networks)
- 모델 성능 평가 및 시뮬레이션 (MSE, MAE, R2, Accuracy, F1 등)
- 모델 성능 개선 및 그래픽 출력 (Feature Importance, History plots)

### 4. 문항 분배 전략 (Question Distribution Strategy)
The AI must balance the 14 questions within these official ranges based on the dataset's complexity:
- **Data Analysis**: 5 or 6 questions
- **Data Preprocessing**: 4 or 5 questions
- **AI Modeling**: 4 or 5 questions

### Example 14-Question Layout (5-4-5 Split)
Below is one standard anchor layout. The AI may shift 1 question between sections (e.g., to a 6-4-4 or 5-5-4 split) if the dataset requires more analysis or preprocessing steps.

1. **[Analysis] Library Import**: Import requirements with specific aliases (e.g., `pd`, `np`). (Type A)
2. **[Analysis] Data Loading**: Load CSV, assign to variable (e.g., `df`), and output `head(n)`. (Type A)
3. **[Analysis] Basic Data Check**: `info()`, `shape`, or `describe()` to understand data composition. (Type A)
   > *Insert Visualization Setup Cell (Font settings) here.*
4. **[Analysis] Distribution Analysis**: Visualization (e.g., `countplot`) + **Interpretation** (Type A + Type C).
5. **[Analysis] Relationship Analysis**: Visualization (e.g., `jointplot`, `boxplot`). (Type A)
6. **[Preprocessing] Outlier & Selection**: Filter outliers (e.g., `df[df.col < N]`) and drop ID/RID columns. (Type A)
7. **[Preprocessing] Missing Values**: Check `isnull()` and `dropna()`. Often includes an **Error Correction** task or **Result Count** check. (Type A/B + Type C)
8. **[Preprocessing] Encoding & Scaling**: `get_dummies()` and `StandardScaler`/`RobustScaler`. Usually a **Blank Filling** task. (Type B/A)
9. **[Preprocessing] Data Split**: `train_test_split()` with specific ratio and `random_state`. (Type A)
10. **[Modeling] ML Training**: Train **Decision Tree** and **Random Forest** models with specific hyperparameters (`max_depth`, `random_state`). (Type A)
11. **[Modeling] Feature Importance**: Visualization of `feature_importances_` + **Variable Identification** (Type A + Type C).
12. **[Modeling] ML Evaluation**: Calculate metrics (MAE for Reg, Accuracy for Clf) and **Model Comparison**. (Type A + Type C)
    > *Insert TensorFlow Setup Cell here.*
13. **[Modeling] DL Construction**: `Sequential` model with specific layers (Dense, Dropout, BN) and `EarlyStopping`. Usually a **Blank Filling** task. (Type B/A)
14. **[Modeling] DL Evaluation**: Learning curve visualization (`mse` or `accuracy` history). (Type A)

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
- Keep code runnable from top to bottom.

## Common Failure Modes

Treat these as hard failures:

- only one notebook is produced
- the notebook reads like a tutorial instead of an exam paper
- question count is not exactly 14
- preprocessing steps were not checked against the real dataset

