# Notebook Snippets

Use this file only for concrete Block Set markdown/code shapes. The controlling rules live in `../SKILL.md`, and the structure contract lives in `aice-associate-blueprint.md`.

These snippets are examples of the desired cell rhythm. Reuse the pattern, not the literal dataset names.

## Table of Contents

- Block Set A: Title + Scenario
- Block Set B: Caution Cell
- Block Set C: Column Description
- Block Set D: Spacer Cell
- Block Set E: Simple Direct-Coding Question
- Block Set F: Question + Guide + Code
- Block Set G: Chart + Interpretation Split
- Block Set H: Bug-Fix or Blank-Fill
- Block Set I: Pre-Run Notice + Shared Setup
- Block Set J: Deep-Learning Section
- Block Set K: Closing Cell

## Block Set A: Title + Scenario

```md
**AICE Associate <font color=red>실전문항</font>**
```

```md
### **타이타닉 승객 데이터 기반 <span style="color:darkgreen">생존 예측</span>**
---

- 도메인: 고객 안전 데이터 분석
- 목표: 승객의 특성을 사용해 생존 여부를 예측하는 분류 모델을 만든다.
- 상황: 해운사 분석팀은 사고 보고서를 재현하고 구조 우선순위와 생존 패턴을 설명할 수 있는 예측 모델을 구축하려고 한다.
---
```

## Block Set B: Caution Cell

```md
#### **<span style="color:red">[주의사항]</span>**
- 각 문항의 답안은 반드시 지정된 셀에만 작성합니다.
- 문항에서 제시한 데이터프레임명, 변수명, 파일 경로를 그대로 사용합니다.
- 서술형 답안은 코드 대신 문자열 또는 숫자로 직접 입력합니다.
- 제출 파일은 문항에서 제시한 경로에 저장합니다.
- setup 셀 선실행 지시가 있는 경우 해당 셀을 먼저 실행합니다.
```

## Block Set C: Column Description

```md
**[ 데이터 컬럼 설명 (`train.csv`, `test.csv`) ]**

| 컬럼명 | 설명 | 비고 |
| --- | --- | --- |
| PassengerId | 승객 고유 번호 | 식별자 |
| Survived | 생존 여부 | 타깃 |
| Pclass | 객실 등급 | 범주형 |
```

## Block Set D: Spacer Cell

```md
<br>
<br>
```

## Block Set E: Simple Direct-Coding Question

Use this only when the task is truly simple and does not need hidden constraints.

```md
### **1. 분석에 필요한 `pandas`와 `numpy`를 각각 `pd`, `np` 별칭으로 불러오시오.** [5점]
---
```

```python
# (1) 여기에 답안 코드를 작성하시오.
```

## Block Set F: Question + Guide + Code

This is the default pattern when names, paths, output variables, ratios, or constraints matter.

```md
### **2. 학습용 데이터를 읽어와 데이터프레임 `train_df`에 할당하고 상위 3개 행을 출력하시오.** [5점]
---
```

```md
* 가이드
- 데이터프레임명: `train_df`
- 파일 경로: `data/raw/train.csv`
- 출력 범위: 상위 3개 행
```

```python
# (2) 여기에 답안 코드를 작성하시오.
```

Do not compress this pattern into a title cell plus a generic comment-only answer cell when the guide carries scoring constraints.

## Block Set G: Chart + Interpretation Split

Use this when evidence generation and interpretation should be graded separately.

```md
### **3. `Pclass` 분포를 시각화하고 가장 많은 승객이 속한 객실 등급을 확인하시오.** [10점]
---
```

```md
* 가이드
- **(3-1)** `seaborn`을 사용해 `Pclass` countplot을 그리시오.
- **(3-2)** 가장 많은 승객이 속한 객실 등급 값을 답안 셀에 직접 입력하시오.
```

```python
# (3-1) 여기에 답안 코드를 작성하시오.
```

```python
# (3-2) 여기에 답안을 입력하시오. 실행은 필요하지 않음
```

## Block Set H: Bug-Fix or Blank-Fill

Use this when the assessment format is "fix the provided code" or "fill the critical blanks".

```md
### **7. 아래 starter code의 빈칸을 채워 학습용 특성과 타깃을 분리하시오.** [10점]
---
```

```md
* 가이드
- 원본 데이터프레임명: `train_df`
- 제외할 열: `PassengerId`, `Name`, `Ticket`, `Cabin`, `Survived`
- 특성 데이터프레임명: `train_features`
- 타깃 시리즈명: `y`
- 최종 특성 수를 `answer_7`에 저장하시오.
```

```python
# (코드 셀) starter code의 빈칸을 채우고 실행하시오.
drop_cols = [<#7-1>]
feature_cols = [c for c in train_df.columns if c not in drop_cols]
train_features = train_df[feature_cols].copy()
y = train_df[<#7-2>].copy()

answer_7 = len(feature_cols)
answer_7
```

```python
# (7-1) 여기에 답안을 입력하시오. 실행은 필요하지 않음
```

```python
# (7-2) 여기에 답안을 입력하시오. 실행은 필요하지 않음
```

Prefer this over a vague "오류를 정정하시오" prompt with no visible target. Do not replace this with a single generic answer cell.

## Block Set I: Pre-Run Notice + Shared Setup

```md
> **<span style="color:red">다음 문항을 풀기 전에 </span>아래 코드를 먼저 실행하시오.**
```

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")
```

## Block Set J: Deep-Learning Section

```md
<br>
<br>
```

```md
> **<span style="color:red">다음 문항을 풀기 전에 </span>아래 setup 셀을 먼저 실행하시오.**
```

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

tf.keras.utils.set_random_seed(7)
```

```md
### **13. 아래 제약을 만족하는 딥러닝 분류 모델을 구성하고 검증 정확도를 `answer_13`에 저장하시오.** [10점]
---
```

```md
* 가이드
- hidden layer는 2개 이상 사용하시오.
- hidden layer activation은 `relu`를 사용하시오.
- output layer activation은 `sigmoid`를 사용하시오.
- optimizer는 `adam`, loss는 `binary_crossentropy`를 사용하시오.
- `EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)`를 사용하시오.
- 검증 데이터는 기존 `X_valid`, `y_valid` 흐름을 유지하시오.
```

````md
```md
![딥러닝 구조도](assets/deep-learning-architecture.svg)
```
````

```python
# (코드 셀) starter code의 빈칸을 채우고 실행하시오.
model = Sequential([
    <#13-1>
])

estop = EarlyStopping(monitor='val_loss', <#13-2>=10, restore_best_weights=True)
```

```python
# (13-1) 여기에 답안을 입력하시오. 실행은 필요하지 않음
```

```python
# (13-2) 여기에 답안을 입력하시오. 실행은 필요하지 않음
```

## Block Set K: Closing Cell

```md
### **모든 문항이 제시되었습니다.**
### **동일한 문항 순서의 `solution.ipynb`에서 정답 코드와 실행 결과를 확인할 수 있습니다.**
```
