FROM ghcr.io/astral-sh/uv:0.5.2 AS uv
FROM python:3.13-alpine AS build

COPY --from=uv /uv /usr/local/bin/uv

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.13 \
    UV_PROJECT_ENVIRONMENT=/opt/venv

COPY pyproject.toml /_lock/
COPY uv.lock /_lock/

RUN cd /_lock \
    && uv sync \
        --locked \
        --no-dev \
        --no-install-project


FROM python:3.13-alpine AS release
WORKDIR /opt/challenge

ENV PATH="/opt/venv/bin:$PATH"

ENTRYPOINT [ "/opt/challenge/entrypoint.sh" ]
STOPSIGNAL SIGINT

RUN addgroup -g 10001 app \
    && adduser -D -H -u 10001 -G app app

COPY --from=build /opt/venv /opt/venv

COPY .secret_key /opt/challenge/.secret_key
COPY entrypoint.sh /opt/challenge/entrypoint.sh
COPY wsgi.py /opt/challenge/wsgi.py
COPY app /opt/challenge/app

RUN chown -R 10001:10001 /opt/challenge \
    && chmod 500 /opt/challenge/entrypoint.sh

USER 10001
EXPOSE 8000