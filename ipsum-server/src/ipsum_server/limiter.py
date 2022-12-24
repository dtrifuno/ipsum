import os
import sys

from slowapi import Limiter
from slowapi.util import get_remote_address

DEFAULT_RATE_LIMIT = 20


def get_rate_limit() -> int:
    """Get rate limit from env (in requests/minute) or return default limit instead."""
    env_rate_limit = os.getenv("APP_RATE_LIMIT")
    if env_rate_limit is not None:
        if env_rate_limit.isdigit():
            rate_limit = int(env_rate_limit)
            if rate_limit > 0:
                return rate_limit
        print(
            "APP_RATE_LIMIT must be a positive integer"
            f"(allowed requests per minute), is {env_rate_limit} instead.",
            file=sys.stderr,
        )
        sys.exit(1)
    return DEFAULT_RATE_LIMIT


limit = f"{get_rate_limit()}/minute"

limiter = Limiter(key_func=get_remote_address, storage_uri=os.getenv("APP_STORAGE_URI"))
