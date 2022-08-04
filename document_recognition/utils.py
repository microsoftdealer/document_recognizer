import asyncio
from concurrent.futures import Executor
from datetime import datetime
from functools import wraps, partial
from typing import Optional, Any


class to_async:
    def __init__(self, *, executor: Optional[Executor] = None):
        self.executor = executor

    def __call__(self, blocking):
        @wraps(blocking)
        async def wrapper(*args, **kwargs):
            loop = asyncio.get_running_loop()

            func = partial(blocking, *args, **kwargs)

            return await loop.run_in_executor(self.executor, func)

        return wrapper


def int_or_none(value: str) -> Optional[int]:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def type_or_none(value: str, type_: str) -> Any:
    type_str = {
        "datetime": lambda s: datetime.strptime(s, "%d.%m.%Y"),
        "int": int,
        "float": float,
        "str": str,
    }
    try:
        return type_str[type_](value)
    except (ValueError, TypeError):
        return None
