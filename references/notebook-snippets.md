# Notebook Snippets

Use this file only for concrete Block Set markdown/code shapes. The controlling rules still live in `../SKILL.md`.

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
### **타이타닉 승객 데이터를 활용한 <span style="color:darkgreen">생존 여부</span> 예측**
---

- 도메인 : 해상 안전 데이터 분석
- 목표 : 승객 정보를 활용해 생존 여부를 예측하는 분류 모델을 개발
- 상황 : 사고 분석팀이 구조 우선순위 판단과 사전 위험 분석에 활용할 예측 모델을 만들고자 한다.
---
```

## Block Set B: Caution Cell

```md
#### **<span style="color:red">[유의사항]</span>**
- 각 문항의 답안은 반드시 지정된 답안 셀에 입력하세요.
- 문항에서 제시한 변수명은 그대로 사용하세요.
- 답안 위치가 아닌 다른 셀에 작성하면 채점되지 않습니다.
- 정답지 실행 시 `data/submissions/` 아래에 결과 파일이 저장될 수 있습니다.
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

```md
### **1. `pandas`를 `pd` 별칭으로 불러오세요.**
---
```

```python
# (1) 여기에 답안코드를 작성하고 실행하세요.
```

## Block Set F: Question + Guide + Code

```md
### **2. `data/raw/train.csv`를 읽어 `df`에 저장하고 상위 4개 행을 출력하세요.**
### **데이터 로딩과 기본 확인을 동시에 수행하세요.**
---
```

```md
* **
- 데이터프레임 변수명 : `df`
- 데이터 파일명 : `data/raw/train.csv`
- 출력할 행 수 : 상위 4개
---
```

```python
# (2) 여기에 답안코드를 작성하고 실행하세요.
```

## Block Set G: Chart + Interpretation Split

```md
### **3. `Pclass` 분포를 시각화하고 가장 많이 등장하는 객실 등급을 답하세요.**
---
```

```md
* **
- **(3-1) seaborn을 사용해 `Pclass`의 countplot을 그리세요**
- **(3-2) 가장 많이 등장하는 객실 등급을 답안 셀에 입력하세요**
---
```

```python
# (3-1) 여기에 답안코드를 작성하고 실행하세요.
```

```python
# (3-2) 여기에 답안을 입력하세요(실행 불필요)
```

## Block Set H: Bug-Fix or Blank-Fill

```md
### **7. 아래 starter code의 오류를 수정하여 전처리를 완료하세요.**
---
```

```md
* **
- 대상 데이터프레임 : `df`
- 입력 변수는 `PassengerId`, `Survived`를 제외한 컬럼만 사용하세요
- 입력 데이터는 `X`, 타깃 데이터는 `y`에 저장하세요
- 최종 입력 변수 개수는 `feature_count`에 저장하세요
- 아래 starter code의 빈칸을 채우거나 오류를 수정하세요
---
```

```python
# (코드 셀) 코드의 빈칸을 채우고 실행하세요

feature_cols = [c for c in df.columns if c not in [<#7-1>]]
X = df[feature_cols].copy()
y = df[<#7-2>].copy()

feature_count = len(feature_cols)
```

```python
# (7-1) 여기에 답안을 입력하세요(실행 불필요)
```

```python
# (7-2) 여기에 답안을 입력하세요(실행 불필요)
```

## Block Set I: Pre-Run Notice + Shared Setup

```md
> **<span style="color:red">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**
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
> **<span style="color:red">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**
```

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

tf.keras.utils.set_random_seed(7)
```

```md
<br>
<br>
```

```md
### **13. 분류용 딥러닝 모델을 구성하고 학습하세요.**
### **아래 가이드에 따라 모델 구조와 학습 조건을 정확히 맞추세요.**
---
```

```md
* **
- hidden layer는 2개 이상 사용하세요
- hidden layer activation은 `relu`를 사용하세요
- output layer activation은 `sigmoid`를 사용하세요
- optimizer는 `adam`, loss는 `binary_crossentropy`를 사용하세요
- `EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)`를 사용하세요
- 학습 결과는 `history`에 저장하세요
---
```

````md
```mermaid
graph LR
    Input([입력층]) --- Dense1[Dense 128 unit relu]
    Dense1 --- Dropout[Drop Out 0.3]
    Dropout --- Dense2[Dense 64 unit relu]
    Dense2 --- Dense3[Dense 32 unit relu]
    Dense3 --- Output([출력층 Dense 2 unit sigmoid])

    style Input fill:#6A1B9A,color:#fff
    style Output fill:#1B5E20,color:#fff
    style Dropout fill:#757575,color:#fff
```
````

```python
# (코드 셀) 코드의 빈칸을 채우고 실행하세요

model = Sequential([
    <#13-1>
])

estop = EarlyStopping(monitor='val_loss', <#13-2>=10, restore_best_weights=True)
```

```python
# (13-1) 여기에 답안을 입력하세요(실행 불필요)
```

```python
# (13-2) 여기에 답안을 입력하세요(실행 불필요)
```

## Block Set K: Closing Cell

```md
### **모든 문항이 완료되었습니다.**
### **정답지 실행 시 제출 파일과 답안 요약 파일이 생성될 수 있습니다.**
```
