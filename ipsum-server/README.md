# ipsum-server

[![Check Server](https://github.com/dtrifuno/ipsum/actions/workflows/check-server.yml/badge.svg)](https://github.com/dtrifuno/ipsum/actions/workflows/check-server.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A FastAPI web app providing REST API access to the
[Ipsum](https://github.com/dtrifuno/ipsum/) placeholder text generator library.

A deployed copy of the server can be accessed at
[ipsum.trifunovski.me/api/v1](https://ipsum.trifunovski.me/api/v1),
or through the frontend at [ipsum.trifunovski.me](https://ipsum.trifunovski.me/).

## Development

To start a development copy, run `poetry run dev`.

### Typechecking, linting and testing

You can run

```
poetry run mypy /src /tests
```

to typecheck,

```
poetry run flake8
```

to lint, or

```
poetry run pytest --cov
```

to test the code.

## Docker

This application is available as a Docker container image on [Docker Hub](https://hub.docker.com/dtrifuno/ipsum).

## Environment variables

### `APP_CORS_ORIGIN`

Not set by default. This environment variable can be set to a cross-origin host
that you would like the application to allow.

### `APP_HOST`

Host that `uvicorn` should attempt to bind to. Defaults to `127.0.0.1`.

### `APP_PORT`

Port number of socket that `uvicorn` should attempt to bind to. Defaults to `8000`.

### `APP_RATE_LIMIT`

Positive integer representing the number of requests per minute for each user
that the rate limiter should allow. Defaults to `20` requests per IP address per
minute.

### `APP_STORAGE_URI`

Not set by default. Can be set to the URI of a [storage backend supported by
limits](https://limits.readthedocs.io/en/stable/storage.html) such as Redis if
you would like the rate limiter to use it as storage. If no URI is set, the rate
limiter will just store the data in-memory.

## License

[MIT](https://github.com/dtrifuno/ipsum/ipsum-server/blob/main/LICENSE.md)
