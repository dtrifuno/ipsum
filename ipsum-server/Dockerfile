FROM python:3.11-slim-bullseye AS build-image

WORKDIR /root

RUN pip install poetry
COPY README.md LICENSE.md pyproject.toml poetry.lock ./
RUN poetry export --only=main --format=requirements.txt --without-hashes --output="requirements.txt"

COPY src/ ./
RUN poetry build --format=wheel


FROM python:3.11-slim-bullseye as runtime-image

WORKDIR /app

COPY --from=build-image /root/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY --from=build-image /root/dist/ipsum_server*.whl /tmp
RUN pip install /tmp/ipsum_server*.whl
RUN rm -rf /tmp/*

ENV APP_ENV=production
ENV APP_PORT=8000
ENV APP_HOST=127.0.0.1

CMD ["python", "-m", "ipsum_server.app"]