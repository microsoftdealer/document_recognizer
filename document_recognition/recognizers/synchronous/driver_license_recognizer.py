import re
from typing import List, Tuple, Optional, Callable

from document_recognition.backends.base import TextAnnotations
from document_recognition.entities.drive_license import DriverLicense
from document_recognition.recognizers.base import BaseSyncRecognizer, ApiResponse, T

from document_recognition.template import Template
from document_recognition.utils import type_or_none, int_or_none


def strip_english_letters_and_whitespaces(text: str) -> str:
    return re.sub(r"[a-zA-Z]", "", text).strip()


class DriverLicenseRecognizerByRegularExpression(BaseSyncRecognizer[DriverLicense]):
    """Returns only a code of the driver license"""

    def __init__(
            self,
            code_re: Optional[str] = None
    ) -> None:
        if code_re is None:
            code_re = r"\d{2}([ \t]+)?\d{2}([ \t]+)?\d{6}"
        self.code_re = re.compile(code_re)

    def __call__(self, response: ApiResponse) -> T:
        text_annotations = response.text
        code = self.code_re.search(text_annotations)
        return DriverLicense(
            code=int_or_none("".join(code.group().split()) if code else None)
        )


class DriverLicenseRecognizerByTemplate(BaseSyncRecognizer[DriverLicense]):
    def __init__(
            self,
            template: Template,
            *,
            separator: str = " ",
            strip_characters: Callable[[str], str] = strip_english_letters_and_whitespaces,
    ) -> None:
        self.template = template
        self.separator = separator
        self.strip_characters = strip_characters

    @staticmethod
    def _find_average_coordinates(
            annotations: List[TextAnnotations],
    ) -> List[Tuple[str, float, float]]:
        text_infos = []
        for word in annotations:
            xmin, ymin = min((vertice.x, vertice.y) for vertice in word.vertices)
            xmax, ymax = max((vertice.x, vertice.y) for vertice in word.vertices)

            xcenter = (xmin + xmax) / 2
            ycenter = (ymin + ymax) / 2

            text_infos.append((word.text, xcenter, ycenter))
        return text_infos

    def __call__(self, response: ApiResponse) -> T:
        """Parse the response and return DriverLicense object."""
        text_infos = self._find_average_coordinates(response.text_annotations)

        result_dict = {}
        for template_object in self.template.objects:
            name = template_object.name
            coordinates = template_object.coordinates
            texts = [
                text
                for text, x_center, y_center in text_infos
                if coordinates.x_min <= x_center <= coordinates.x_max
                if coordinates.y_min <= y_center <= coordinates.y_max
            ]
            result_dict[name] = type_or_none(
                self.strip_characters(self.separator.join(texts)),
                type_=template_object.type,
            )

        return DriverLicense(**result_dict)
