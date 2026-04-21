---
name: kaggle-aice-associate-builder
description: "Kaggle 정형 데이터 소스 또는 기존 샘플 노트북을 사용하여, 한국어 시험 톤과 원래 샘플 노트북 계약을 기본으로 AICE Associate 문제/정답 노트북을 빌드하거나 정규화합니다."
---

# Kaggle AICE Associate 빌더

Kaggle 데이터셋을 AICE Associate 스타일의 시험 패키지(`문제/정답` 노트북 쌍)로 변환하거나 정규화합니다.

## 참조 계층

| 파일 | 역할 | 읽는 시점 |
|---|---|---|
| `SKILL.md` (이 파일) | 실행 절차 · 핵심 불변 규칙 · 실패 조건 | 항상 |
| `references/aice-associate-blueprint.md` | 패키지 형태 · 질문 설계 · 섹션 계획 · 정규화 규칙 | 초안 작성 또는 정규화 전 |
| `references/notebook-snippets.md` | 셀 마크다운/코드 블록 표준 템플릿 | 셀 작성 시 |

계층 간 충돌 시 상위 파일 우선. 하위 파일은 상위 규칙을 약화시킬 수 없습니다.

---

## 핵심 불변 규칙 (14개)

> 아래 규칙은 어떤 상황에서도 예외 없이 적용됩니다.

1. **`solution.ipynb` 먼저** — 해결 워크플로우가 확정된 후 `problem.ipynb`를 파생시킵니다.
2. **14문항 / 30-30-40 배점** — 섹션 수, 배점 분포, 문항 수는 변경 불가.
3. **정답 유출 금지** — `problem.ipynb`에 해결된 값, 채워진 플레이스홀더, 텍스트 힌트를 넣지 않습니다.
4. **셀 역할 동기화** — 두 노트북의 질문 순서와 셀 역할 패턴이 동일해야 합니다.
5. **한국어 시험 톤** — 문제 설명, 섹션 제목, 가이드, 주의 사항은 모두 한국어 · 명령조.
6. **데이터셋 구체성** — 변수명, 파일 경로, 메트릭, 컬럼명은 실제 데이터셋에서 가져옵니다.
7. **표준 파일명 준수** — 반드시 `problem.ipynb`와 `solution.ipynb`로 명명합니다.
8. **보조 정답 셀 유지** — `solution.ipynb`의 `# [정답]` 블록은 표준 구조의 일부이므로 제거하지 않습니다.
9. **정답 노트북 출력 보존** — `solution.ipynb`는 실행한 상태로 저장하며, setup 셀과 모든 `# [정답]` 코드 셀의 실행 결과(`outputs`, `execution_count`)를 남깁니다. import/setup처럼 자연 출력이 없는 셀은 마지막 줄에 짧은 확인 표현식을 두어 Jupyter 출력 셀이 보이게 합니다. `problem.ipynb`를 파생할 때만 실행 결과를 제거합니다.
10. **시각화 한글 폰트 설정** — `matplotlib` 또는 `seaborn` 시각화 setup 셀에는 `matplotlib.pyplot` import 직후 `import koreanize_matplotlib`을 포함합니다. 한글 표시를 위해 `plt.rcParams["font.family"]`를 직접 지정하지 않습니다.
11. **BOM-free UTF-8** — 생성되는 모든 `.ipynb`는 BOM 없는 UTF-8로 인코딩합니다.
12. **Docker 우선** — 노트북 실행 · 검증은 가능하면 Docker를 통해 수행합니다.
13. **Mermaid 구조도 즉시 연결** — 블루프린트상 구조도 이미지가 필요한 딥러닝/복잡한 모델링 블록이면, `assets/*.mmd` 소스를 만들고 `scripts/render_mermaid_assets.py`로 `.svg`를 렌더한 뒤 노트북 마크다운에 해당 이미지를 포함합니다. 텍스트 블록으로 대체하지 않습니다.
14. **데이터 획득은 Kaggle MCP 우선** — 데이터가 워크스페이스에 아직 없으면, 임의의 셸 다운로드나 수동 URL 추측 전에 Kaggle MCP로 대회/데이터셋 메타데이터와 파일 목록을 먼저 조회하고 가능한 경우 그 경로로 내려받습니다. MCP 접근이 막혀 있으면 그 사실을 명시한 뒤에만 대체 경로를 검토합니다.

---

## 작업 절차

### 1. 사전 점검

시작 전 아래를 확인하고, 하나라도 실패하면 중단합니다.

- [ ] Docker 및 Jupyter 서비스 실행 가능 여부
- [ ] 데이터셋 경로 · 출력 디렉토리 존재 여부
- [ ] 노트북 쓰기 경로의 BOM-free UTF-8 안전 여부
- [ ] Git 락 또는 워크스페이스 충돌 없음

> **Jupyter MCP 확인 순서** (사용 불가로 판단하기 전): 저장소 MCP 구성 → 컨테이너 실행 여부 → 엔드포인트/토큰 일치 여부 → 세션 내 `jupyter` 네임스페이스 노출 여부. 모두 확인 후에도 안 되면 직접 `.ipynb` 편집으로 전환합니다.

### 2. 데이터셋 검사

질문 작성 전 실제 파일을 열어 아래를 확인합니다.

- 태스크 유형, 타겟 컬럼, 파일명, 행 수
- ID 컬럼 · 결측치 · 클래스 불균형 여부
- 시험에서 `train.csv`만 쓸지, 추가 파일도 쓸지

### 2-1. 데이터 획득

워크스페이스에 원본 데이터가 없으면 아래 순서를 따릅니다.

- [ ] Kaggle MCP로 대회/데이터셋 메타데이터 조회
- [ ] Kaggle MCP로 파일 목록과 주요 파일명 확인
- [ ] 가능한 경우 Kaggle MCP로 필요한 원본 파일 다운로드
- [ ] MCP 접근이 막히거나 인증/약관 문제로 실패하면 그 사실을 먼저 기록
- [ ] 그 다음에만 수동 다운로드, 로컬 대체본, 사용자 제공 파일 여부를 검토

셸에서 임의 URL을 추정해 바로 내려받거나, 데이터 구조를 보지 않은 채 문제부터 작성하지 않습니다.

### 3. 작업 유형 결정

| 유형 | 참조 |
|---|---|
| 데이터셋에서 신규 생성 또는 정규화 | `blueprint.md` + `snippets.md` |

### 3-1. 문제 정의의 Source of Truth

- 데이터셋별 문제 정의의 최종 source of truth는 각 패키지의 `profile.json`입니다.
- 일회성 요청 처리를 위해 데이터셋별 문항, 정답 코드, 컬럼 설명을 별도 Python 스크립트에만 하드코딩하지 않습니다.
- 반복 생성 기능이 필요하면 `scripts/aice_generator/` 내부의 scaffold/helper로 일반화하고, 생성 결과는 반드시 `profile.json`으로 저장한 뒤 기존 `generate_aice_associate.py --profile ...` 경로로 노트북을 생성합니다.
- scaffold/helper는 초안 생성을 돕는 도구일 뿐이며, 최종 검토·수정·재생성의 기준은 `profile.json`, `solution.ipynb`, `problem.ipynb` 패키지입니다.

### 4. 생성 루프

```
작성자(writer) → solution.ipynb 초안
       ↓
강력한 평가자(evaluator) → blueprint · 샘플 · 정답 노출면 대조
       ↓ (이슈 있음)
작성자 → 기존 초안 패치 (재작성보다 패치 우선)
       ↓
평가자 결과 종결 시 → problem.ipynb 파생
```

### 4-1. 구조도 자산 연결

딥러닝 문항이나 복잡한 모델 구조를 설명하는 블록이 있으면 아래를 즉시 수행합니다.

- [ ] `assets/` 아래에 Mermaid 원본(`*.mmd`) 작성
- [ ] `python /workspace/scripts/render_mermaid_assets.py <asset-dir 또는 .mmd>` 실행으로 `.svg` 생성
- [ ] 노트북 마크다운에는 `.mmd`가 아니라 렌더된 `.svg` 이미지를 삽입
- [ ] 문제지와 정답지 모두 동일한 구조도 이미지를 참조

이 단계는 선택 사항이 아니라, `references/aice-associate-blueprint.md`의 “Mermaid 로 작성된 구조도 이미지를 마크다운에 포함” 규칙을 실행 절차로 내린 것입니다.

### 5. 형식 검증 → 실행 검증

형식 검증을 먼저 통과한 후 실행합니다. 순서를 바꾸지 마세요.

---

## 실패 조건

아래 중 하나라도 해당하면 패키지를 미완성으로 간주합니다.

- 문항 수 ≠ 14, 또는 섹션 배점 ≠ 30/30/40
- `problem.ipynb`에 정답 · 힌트 유출
- `problem.ipynb`에 실행 결과 출력 잔류
- `solution.ipynb`의 setup 셀 또는 `# [정답]` 코드 셀에 실행 결과가 남아 있지 않음
- 두 노트북 간 질문 순서 또는 셀 역할 불일치
- 파일명이 표준 규약(`problem.ipynb`, `solution.ipynb`)과 불일치
- 보조 정답 셀(`# [정답]`) 구조가 표준 가이드와 불일치
- 가이드가 누락되거나 일반적인 주석으로만 채워진 블록 존재
- `matplotlib`/`seaborn` 시각화 setup 셀에서 `koreanize_matplotlib`을 누락하거나, 한글 폰트를 `plt.rcParams["font.family"]`로 수동 지정
- 구조도 블록을 렌더된 `.svg` 이미지 대신 fenced `text`/`mermaid` 코드블록으로 삽입
- 검증 질문이 `X_valid/y_valid` 대신 전체 훈련 데이터를 사용
- 노트북 바이트가 UTF-8 BOM(`EF BB BF`)으로 시작
- 구조도 이미지가 필요한 블록에서 Mermaid 자산 생성·렌더·삽입을 생략하고 텍스트로만 대체
- 로컬 데이터가 없는데 Kaggle MCP 확인 없이 셸 다운로드나 임의 대체 경로로 바로 진행
- 데이터셋별 문항 정의가 각 패키지의 `profile.json`이 아니라 임시 생성 스크립트에만 존재함

---

## 검증 체크리스트

### 형식 검증 (실행 전 필수)

- [ ] 문항 수 14개 · 섹션 배점 30/30/40 확인
- [ ] 프론트매터 및 주의 사항 스타일이 `blueprint.md`와 일치
- [ ] `problem.ipynb` 정답 유출 없음
- [ ] 두 노트북의 셀 역할 동기화 확인
- [ ] 가이드 밀도 충분 (반복이 아닌 실질적 제약 조건 포함)
- [ ] 파일명 · 폴더 구조가 표준 규약과 일치
- [ ] `solution.ipynb`의 `# [정답]` 블록 유지 확인
- [ ] 시각화 setup 셀에 `import koreanize_matplotlib` 포함 및 수동 `font.family` 설정 없음 확인
- [ ] 구조도 필요 블록에서 Mermaid `.mmd`와 렌더된 `.svg`가 모두 존재하고, 노트북이 `.svg`를 참조
- [ ] 로컬 원본 데이터가 없었던 경우 Kaggle MCP 조회/다운로드 경로를 먼저 거쳤는지 확인

### 실행 검증 (Docker 우선)

- [ ] `solution.ipynb` 처음부터 끝까지 실행 성공
- [ ] `solution.ipynb`의 setup 셀과 모든 `# [정답]` 코드 셀에 실행 결과와 `execution_count`가 남아 있음 확인
- [ ] 시각화 setup 셀에서 `koreanize_matplotlib` import 성공 확인
- [ ] 필요한 아티팩트 생성 확인
- [ ] 검증 단계가 `X_valid/y_valid` 사용 확인
- [ ] BOM 없음 확인 (`xxd notebook.ipynb | head -1`의 첫 바이트 확인)
- [ ] Mermaid 자산이 있으면 `scripts/render_mermaid_assets.py` 실행 후 최신 `.svg` 반영 확인

### 종료 전 최종 샘플링

블루프린트와 대조하여 무작위로 각 1개 셀 점검: 프론트매터 · EDA 블록 · 전처리 블록 · 모델링 블록. 딥러닝 포함 시 해당 블록도 점검.

---

## 피해야 할 주요 안티 패턴

> 세부 패턴은 `references/aice-associate-blueprint.md`를 참조합니다. 여기서는 가장 빈번한 실수만 요약합니다.

- 스캐폴딩 블록을 단일 마크다운 + 주석 코드 셀로 압축
- 데이터셋 고유 문구를 일반적인 레시피 설명으로 대체
- 동일 태스크를 제목 셀과 가이드 셀에 중복 서술 (계층은 하나만)
- `problem.ipynb`에 노트북 실행 출력 잔류
- 정답 변수를 숨겨진 보조 변수로 우회 라우팅
- 데이터셋별 문항을 일회성 Python 스크립트에 하드코딩하고 `profile.json`을 최종 기준으로 남기지 않음
