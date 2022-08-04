from typing import Optional

from document_recognition.backends.base import BaseSyncBackend, PathLike
from document_recognition.photo_pre_processors.base import SyncPreProcessorType
from document_recognition.recognizers.base import (
    BaseSyncRecognizer,
    T,
    SyncRecognizerType,
)


class SyncDocumentRecognition:
    def __init__(
        self,
        backend: BaseSyncBackend,
    ) -> None:
        self.backend = backend

    def recognize_document(
        self,
        image_path: PathLike,
        *,
        recognizer: SyncRecognizerType[T],
        pre_processor_of_photo: Optional[SyncPreProcessorType] = None
    ) -> T:
        if pre_processor_of_photo:
            image_path = pre_processor_of_photo(image_path)

        api_response = self.backend.recognize_document(image_path)

        recognized_document = recognizer(api_response)

        return recognized_document
