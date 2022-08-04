from asyncio import get_running_loop
from concurrent.futures import Executor
from functools import partial, partialmethod
from typing import Optional, Awaitable, Any

from document_recognition.backends import BaseAsyncBackend, BaseSyncBackend


class AsyncBackendWrapper(BaseAsyncBackend):
    """Wrapper for sync backend that allows to use it in async context"""

    def __init__(
        self,
        backend: BaseSyncBackend,
        /,
        executor: Optional[Executor] = None,
    ) -> None:
        """
        :param backend: sync backend to wrap
        :param executor: executor to use for async calls. If None, default executor will be used
        """
        self.backend = backend
        self.executor = executor

    def _call(self, method_name: str, *args, **kwargs) -> Awaitable[Any]:
        return get_running_loop().run_in_executor(
            self.executor, partial(getattr(self.backend, method_name), *args, **kwargs)
        )

    recognize_document = partialmethod(_call, "recognize_document")
    recognize_document_from_url = partialmethod(_call, "recognize_document_from_url")
