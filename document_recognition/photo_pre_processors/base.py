import abc
from typing import Optional, Union, Callable, Awaitable

from document_recognition.backends.base import PathLike

SyncPreProcessorType = Union[
    "BaseSyncPhotoPreProcessor", Callable[[PathLike, Optional[PathLike]], PathLike]
]
AsyncPreProcessorType = Union[
    "BaseAsyncPhotoPreProcessor",
    Callable[[PathLike, Optional[PathLike]], Awaitable[PathLike]],
]


class BaseSyncPhotoPreProcessor(abc.ABC):
    """Base class for all synchronous photo pre processors, which are used to pre process photos.

    Usually it's cpu-bound like cropping or resizing using Pillow/PIL/CV2.
    If you're making requests to the API in it or want to run cpu-bound in a process pool executor,
    you may want to use an :class:`BaseAsyncPhotoPreProcessor` instead.
    """

    @abc.abstractmethod
    def __call__(
        self, image_path: PathLike, destination: Optional[PathLike] = None
    ) -> PathLike:
        raise NotImplementedError


class BaseAsyncPhotoPreProcessor(abc.ABC):
    @abc.abstractmethod
    async def __call__(
        self, image_path: PathLike, destination: Optional[PathLike] = None
    ) -> PathLike:
        raise NotImplementedError
