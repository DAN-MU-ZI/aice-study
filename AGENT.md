# Agent Instructions

이 저장소에서 Jupyter Notebook 기반 작업이 필요하면 기본 실행 환경으로 도커 이미지를 사용한다.

## Default Environment

- 기본 이미지: `aice-study-jupyter`
- 기본 서비스: `jupyter`
- 정의 파일: `docker-compose.yml`

## Required Python Stack

아래 라이브러리가 포함된 환경을 기준으로 작업한다.

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `tensorflow`
- `xgboost`

## Execution Rule

에이전트는 로컬 파이썬 환경을 임의로 만들기보다 먼저 아래 도커 환경 사용을 우선한다.

```bash
docker compose up --build -d jupyter jupyter-mcp
```

컨테이너 내부 작업 기준 경로는 `/workspace`이고, 노트북 작업 경로는 `/workspace/notebooks`다.

## Notebook Authoring Rule

노트북을 생성하거나 수정할 때는 단순히 문항 수만 맞추지 말고, 제공된 AICE 샘플문항의 셀 구성 리듬과 스캐폴딩 수준을 재현해야 한다.

- 샘플이 `제목 markdown + 가이드 markdown + 답안 cell` 구조를 쓰면 같은 구조를 유지한다.
- 샘플이 `# (3-1)`, `# (3-2)`, `#5-1`, `#13-2` 같은 답안 위치를 명시하면 그 패턴을 유지한다.
- 샘플이 starter code의 빈칸 채우기나 오류 정정 패턴을 쓰는 문항은, 한 줄짜리 빈 코드셀로 축약하지 않는다.
- 샘플이 함수명, 변수명, 데이터프레임명, 하이퍼파라미터, seed, metric, callback을 직접 지정하면 같은 수준으로 구체화한다.
- 딥러닝 문항은 샘플처럼 setup 안내, import/setup cell, 구조 가이드, placeholder starter code, 필요 시 topology diagram을 유지한다.

## Notes

- 노트북 파일은 호스트의 `./notebooks`와 컨테이너의 `/workspace/notebooks`가 연결된다.
- 이미지가 없거나 최신 설정 반영이 필요하면 `docker compose build`로 다시 빌드한다.
- 별도 요구가 없으면 CPU 기반 TensorFlow 환경으로 간주한다.
- Jupyter MCP가 가능하면 노트북 내용 변경과 검증은 MCP 기반으로 우선 수행한다.
