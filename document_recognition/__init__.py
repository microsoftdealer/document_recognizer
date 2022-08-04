# import abc
# import dataclasses
# from typing import Generic, TypeVar
#
# from google.cloud.vision_v1 import ImageAnnotatorClient
#
#
# @dataclasses.dataclass
# class DocumentEntity:
#     confidence: float
#
#     @classmethod
#     def from_response(cls, response: dict) -> 'DocumentEntity':
#         return cls(
#             text=response['text'],
#             bounding_poly=response['boundingPoly'],
#             confidence=response['confidence']
#         )
#
#
#
#
# class BaseDocumentRecognition(abc.ABC):
#
#     @abc.abstractmethod
#     def recognize(self, image_path: str) -> :
#         raise NotImplementedError()
#
#
# class DocumentRecognition:
#     def __init__(self, google_vision_client: ImageAnnotatorClient, *recognizers: BaseRecognizer):
#         if not recognizers:
#             raise ValueError('At least one recognizer must be provided')
#
#         self.google_vision_client = google_vision_client
#         self.recognizers = recognizers
#
#     def recognize_document(self, image_path: str) -> DocumentEntity:
#         response = self.google_vision_client.annotate_image({
#             'image': {'source': {'filename': image_path}},
#             'features': [{'type_': 'DOCUMENT_TEXT_DETECTION'}]
#         })
#         return response.full_text_annotation.text
