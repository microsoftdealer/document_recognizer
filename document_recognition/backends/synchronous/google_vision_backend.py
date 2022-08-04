from pathlib import Path

from google.cloud import vision
from google.cloud.vision_v1 import ImageAnnotatorClient

from document_recognition.backends.base import (
    BaseSyncBackend,
    PathLike,
    TextAnnotations,
    Vertices,
    BaseAsyncBackend,
)
from document_recognition.recognizers.base import ApiResponse


class GoogleVisionBackend(BaseSyncBackend):
    def __init__(self, image_annotator_client: ImageAnnotatorClient) -> None:
        self.image_annotator_client = image_annotator_client

    def recognize_document(self, image_path: PathLike) -> ApiResponse:
        if isinstance(image_path, (str, Path)):
            path = {"source": {"filename": str(image_path)}}
        else:
            path = {"content": image_path.read()}
        payload = {
            "image": path,
            "features": [{"type_": vision.Feature.Type.DOCUMENT_TEXT_DETECTION}],
        }
        response = self.image_annotator_client.annotate_image(payload)
        return ApiResponse(
            text_annotations=[
                TextAnnotations(
                    text=text_annotation.description,
                    vertices=[
                        Vertices(
                            x=vertex.x,
                            y=vertex.y,
                        )
                        for vertex in text_annotation.bounding_poly.vertices
                    ],
                )
                for text_annotation in response.text_annotations
            ],
            text=response.full_text_annotation.text,
        )

    def recognize_document_from_url(self, url: str) -> ApiResponse:
        raise NotImplementedError
