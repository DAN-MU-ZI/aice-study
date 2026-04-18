# syntax=docker/dockerfile:1.7

FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    JUPYTER_PORT=8888 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:${PATH}"

WORKDIR /build

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv "${VIRTUAL_ENV}"

COPY requirements.txt /tmp/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --upgrade pip \
    && python -m pip install -r /tmp/requirements.txt

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    JUPYTER_PORT=8888 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:${PATH}"

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv

RUN mkdir -p /workspace/notebooks

EXPOSE 8888

CMD ["sh", "-c", "jupyter lab --ip=0.0.0.0 --port=${JUPYTER_PORT} --no-browser --allow-root --IdentityProvider.token=\"${JUPYTER_TOKEN:-aice-jupyter-token}\" --notebook-dir=/workspace/notebooks"]
