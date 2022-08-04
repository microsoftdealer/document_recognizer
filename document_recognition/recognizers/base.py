import abc
from typing import TypeVar, Generic, Union, Callable, Awaitable

from document_recognition.backends.base import ApiResponse

T = TypeVar("T")

SyncRecognizerType = Union["BaseSyncRecognizer[T]", Callable[[ApiResponse], T]]
AsyncRecognizerType = Union[
    "BaseAsyncRecognizer[T]", Callable[[ApiResponse], Awaitable[T]]
]


class BaseSyncRecognizer(abc.ABC, Generic[T]):
    """Base class for all synchronous recognizers, which are used to recognize documents.

    Usually it's cpu-bound like regex or finding by coordinates.
    If you're making requests to the API in it, you may want to use an :class:`BaseAsyncRecognizer` instead.
    """

    @abc.abstractmethod
    def __call__(self, response: ApiResponse) -> T:
        raise NotImplementedError


class BaseAsyncRecognizer(abc.ABC, Generic[T]):
    """Base class for all asynchronous recognizers, which are used to recognize documents.

    Usually it's a request to the API or queues with workers.
    """

    @abc.abstractmethod
    async def __call__(self, response: ApiResponse) -> T:
        raise NotImplementedError
