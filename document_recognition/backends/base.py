import abc
from dataclasses import dataclass
from pathlib import Path
from typing import Union, BinaryIO, List, Optional

PathLike = Union[str, Path, BinaryIO]


@dataclass
class Vertices:
    x: float
    y: float


@dataclass
class TextAnnotations:
    text: str
    vertices: List[Vertices]

    locale: Optional[str] = None
    mid: Optional[str] = None
    score: Optional[float] = None
    confidence: Optional[float] = None
    topicality: Optional[float] = None


@dataclass
class ApiResponse:
    text_annotations: List[TextAnnotations]
    text: Optional[str] = None


class BaseSyncBackend(abc.ABC):
    @abc.abstractmethod
    def recognize_document(self, image_path: PathLike) -> ApiResponse:
        raise NotImplementedError

    @abc.abstractmethod
    def recognize_document_from_url(self, url: str) -> ApiResponse:
        raise NotImplementedError


class BaseAsyncBackend(abc.ABC):
    @abc.abstractmethod
    async def recognize_document(self, image_path: PathLike) -> ApiResponse:
        raise NotImplementedError

    @abc.abstractmethod
    async def recognize_document_from_url(self, url: str) -> ApiResponse:
        raise NotImplementedError
