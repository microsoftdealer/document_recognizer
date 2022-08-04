from collections import deque
from typing import TYPE_CHECKING, Deque, Optional, Type

from document_recognition.backends import BaseSyncBackend, ApiResponse, PathLike
from document_recognition.sync_client import SyncDocumentRecognition


class MockedBackend(BaseSyncBackend):
    def __init__(self):
        super().__init__()
        self.responses: Deque[ApiResponse] = deque()

    def add_result(self, response: ApiResponse) -> ApiResponse:
        self.responses.append(response)
        return response

    def recognize_document(self, image_path: PathLike) -> ApiResponse:
        return self.responses.pop()

    def recognize_document_from_url(self, url: str) -> ApiResponse:
        return self.responses.pop()


class MockedSyncDocumentRecognition(SyncDocumentRecognition):
    if TYPE_CHECKING:
        backend: MockedBackend

    def __init__(self):
        super().__init__(
            backend=MockedBackend(),
        )

    def add_result(
        self,
        response: ApiResponse,
    ) -> ApiResponse:
        self.backend.add_result(response)
        return response
