import inspect
from typing import Union, Optional, Callable, Any

from document_recognition.backends import BaseAsyncBackend, PathLike, ApiResponse
from document_recognition.photo_pre_processors.base import (
    SyncPreProcessorType,
    AsyncPreProcessorType,
)
from document_recognition.recognizers.base import (
    SyncRecognizerType,
    AsyncRecognizerType,
    T,
)


def _is_async(f: Callable[..., Any]) -> bool:
    if inspect.isawaitable(f) or inspect.iscoroutinefunction(f):
        return True


class AsyncDocumentRecognition:
    def __init__(self, backend: BaseAsyncBackend) -> None:
        self.backend = backend

    async def recognize_document(
        self,
        image_path: PathLike,
        *,
        recognizer: Union[SyncRecognizerType[T], AsyncRecognizerType[T]],
        pre_processor_of_photo: Optional[
            Union[SyncPreProcessorType, AsyncPreProcessorType]
        ] = None
    ) -> T:
        if pre_processor_of_photo:
            if _is_async(pre_processor_of_photo):
                image_path = await pre_processor_of_photo(image_path)
            else:
                image_path = pre_processor_of_photo(image_path)

        api_response = await self.backend.recognize_document(image_path)

        if _is_async(recognizer):
            recognized_document = await recognizer(api_response)
        else:
            recognized_document = recognizer(api_response)

        return recognized_document
