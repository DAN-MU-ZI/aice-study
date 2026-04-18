# syntax=docker/dockerfile:1.7

FROM quay.io/jupyter/tensorflow-notebook:b74418220768

USER root

WORKDIR /workspace

COPY requirements.txt /tmp/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r /tmp/requirements.txt \
    && mkdir -p /workspace/notebooks \
    && chown -R "${NB_UID}:${NB_GID}" /workspace

EXPOSE 8888

USER ${NB_UID}
