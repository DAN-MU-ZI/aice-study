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
docker compose up --build -d
```

컨테이너 내부 작업 기준 경로는 `/workspace`이고, 노트북 작업 경로는 `/workspace/notebooks`다.

## Notes

- 노트북 파일은 호스트의 `./notebooks`와 컨테이너의 `/workspace/notebooks`가 연결된다.
- 이미지가 없거나 최신 설정 반영이 필요하면 `docker compose build`로 다시 빌드한다.
- 별도 요구가 없으면 CPU 기반 TensorFlow 환경으로 간주한다.
