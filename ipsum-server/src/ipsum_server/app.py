import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import uvicorn

from ipsum_server.api_v1 import api_v1
from ipsum_server.limiter import limiter

app = FastAPI(docs_url=None, redoc_url=None)

# Set up rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Set up CORS
origins = []
if os.getenv("APP_ENV") == "production":
    env_app_cors_origin = os.getenv("APP_CORS_ORIGIN")
    if env_app_cors_origin is not None:
        origins = [env_app_cors_origin]
else:
    origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["GET"])

app.mount("/api/v1", api_v1)


def main() -> None:
    """Launch FastAPI application using uvicorn."""
    port = 8000
    env_app_port = os.getenv("APP_PORT")
    if env_app_port is not None:
        port = int(env_app_port)
    host = os.getenv("APP_HOST") or "127.0.0.1"
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
