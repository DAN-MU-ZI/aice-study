# 노트북 스니펫 (Notebook Snippets)

이 파일은 `references/aice-associate-blueprint.md` 가이드라인에 정의된 구조를 실제로 구현하기 위한 마크다운 및 코드 블록 모음입니다. 규칙에 대한 상세 내용은 **Blueprint** 파일을 참조하고, 여기서는 복사하여 사용할 수 있는 패턴만 제공합니다.

## 목차

- 블록 세트 A: 제목 + 시나리오
- 블록 세트 B: 주의사항 셀
- 블록 세트 C: 컬럼 설명
- 블록 세트 D: 스페이서(Spacer) 셀
- 블록 세트 E: 단순 직접 코딩 질문
- 블록 세트 F: 질문 + 가이드 + 코드
- 블록 세트 G: 차트 + 해석 분할
- 블록 세트 H: 버그 수정 또는 빈칸 채우기
- 블록 세트 I: 사전 실행 알림 + 공통 설정
- 블록 세트 J: 딥러닝 섹션
- 블록 세트 K: 종료 셀

## 블록 세트 A: 제목 + 시나리오

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

## 블록 세트 B: 주의사항 셀

```md
#### **<span style="color:red">[주의사항]</span>**
- 각 문항의 답안은 반드시 지정된 셀에만 작성합니다.
- 문항에서 제시한 데이터프레임명, 변수명, 파일 경로를 그대로 사용합니다.
- 서술형 답안은 코드 대신 문자열 또는 숫자로 직접 입력합니다.
- 제출 파일은 문항에서 제시한 경로에 저장합니다.
- setup 셀 선실행 지시가 있는 경우 해당 셀을 먼저 실행합니다.
```

## 블록 세트 C: 컬럼 설명

```md
**[ 데이터 컬럼 설명 (`train.csv`) ]**

| 컬럼명 | 설명 | 비고 |
| --- | --- | --- |
| PassengerId | 승객 고유 번호 | 식별자 |
| Survived | 생존 여부 | 타깃 |
| Pclass | 객실 등급 | 범주형 |
```

## 블록 세트 D: 스페이서(Spacer) 셀

```md
<br>
<br>
```

## 블록 세트 E: 단순 직접 코딩 질문

```md
### **1. 분석에 필요한 라이브러리를 먼저 불러오려고 합니다.**
### **`pandas`와 `numpy`를 각각 `pd`, `np` 별칭으로 불러오세요.** [5점]
---
```

```python
# (1) 여기에 답안 코드를 작성하세요.
```

```md
# [정답]
```

## 블록 세트 F: 질문 + 가이드 + 코드

```md
### **학습용 데이터를 읽어와 확인하려고 합니다.**
### **데이터프레임 `train_df`에 할당하고 상위 3개 행을 출력하세요.** [5점]
---
```

```md
* 가이드
- 데이터프레임명: `train_df`
- 파일 경로: `data/raw/train.csv`
- 출력 범위: 상위 3개 행
```

```python
# (2) 여기에 답안 코드를 작성하세요.
```

```md
# [정답]
```

## 블록 세트 G: 차트 + 해석 분할

```md
### **시각화를 통해 `Pclass` 분포를 파악하려고 합니다.**
### **가장 많은 승객이 속한 객실 등급을 확인하세요.** [10점]
---
```

```md
* 가이드
- **(3-1)** `seaborn`을 사용해 `Pclass` countplot을 그리세요.
- **(3-2)** 가장 많은 승객이 속한 객실 등급 값을 답안 셀에 직접 입력하세요.
```

```python
# (3-1) 여기에 답안 코드를 작성하세요.
```

```python
# (3-2) 여기에 답안을 입력하세요. 실행은 필요하지 않음
```

```md
# [정답]
```

## 블록 세트 H: 버그 수정 또는 빈칸 채우기

```md
### **모델링에 사용할 입력값과 정답값을 분리하려고 합니다.**
### **아래 starter code의 빈칸을 채워 학습용 특성과 타깃을 분리하세요.** [10점]
---
```

```md
* 가이드
- 원본 데이터프레임명: `train_df`
- 제외할 열: `PassengerId`, `Name`, `Ticket`, `Cabin`, `Survived`
- 특성 데이터프레임명: `train_features`
- 타깃 시리즈명: `y`
```

```python
# (코드 셀) starter code의 빈칸을 채우고 실행하세요.
drop_cols = [<#7-1>]
feature_cols = [c for c in train_df.columns if c not in drop_cols]
train_features = train_df[feature_cols].copy()
y = train_df[<#7-2>].copy()
```

```python
# (7-1) 여기에 답안을 입력하세요. 실행은 필요하지 않음
```

```python
# (7-2) 여기에 답안을 입력하세요. 실행은 필요하지 않음
```

```md
# [정답]
```

## 블록 세트 I: 사전 실행 알림 + 공통 설정

`matplotlib` 또는 `seaborn` 시각화가 포함된 노트북에서는 `koreanize_matplotlib`을 공통 setup 셀에 포함합니다. 한글 폰트를 `plt.rcParams["font.family"]`로 직접 지정하지 않습니다.

```md
> **<span style="color:red">다음 문항을 풀기 전에 </span>아래 코드를 먼저 실행하세요.**
```

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import warnings

warnings.filterwarnings("ignore")
```

## 블록 세트 J: 딥러닝 섹션

```md
> **<span style="color:red">다음 문항을 풀기 전에 </span>아래 setup 셀을 먼저 실행하세요.**
```

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

tf.keras.utils.set_random_seed(7)
```

```md
### **딥러닝 분류 모델을 구성하고 성능을 확인하려고 합니다.**
### **아래 제약을 만족하는 모델을 구성하고 검증 정확도를 `answer_13`에 저장하세요.** [10점]
---
```

```md
* 가이드
- hidden layer는 2개 이상 사용하세요.
- hidden layer activation은 `relu`를 사용하세요.
- output layer activation은 `sigmoid`를 사용하세요.
- optimizer는 `adam`, loss는 `binary_crossentropy`를 사용하세요.
- `EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)`를 사용하세요.
- 검증 데이터는 기존 `X_valid`, `y_valid` 흐름을 유지하세요.
```

````md
![딥러닝 구조도](assets/deep-learning-architecture.svg)
````

구조도는 위처럼 렌더된 `.svg` 이미지로만 삽입합니다. 아래처럼 fenced `text` 또는 `mermaid` 코드블록으로 구조를 설명하지 않습니다.

```python
# (코드 셀) starter code의 빈칸을 채우고 실행하세요.
model = Sequential([
    <#13-1>
])

estop = EarlyStopping(monitor='val_loss', <#13-2>=10, restore_best_weights=True)
```

```python
# (13-1) 여기에 답안을 입력하세요. 실행은 필요하지 않음
```

```python
# (13-2) 여기에 답안을 입력하세요. 실행은 필요하지 않음
```

```md
# [정답]
```

## 블록 세트 K: 종료 셀

```md
### **모든 문항이 제시되었습니다.**
### **동일한 문항 순서의 `solution.ipynb`에서 정답 코드와 실행 결과를 확인할 수 있습니다.**
```
