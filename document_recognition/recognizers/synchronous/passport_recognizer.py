import re
from typing import Optional

from document_recognition.backends import ApiResponse
from document_recognition.entities.passport import Passport
from document_recognition.recognizers.base import BaseSyncRecognizer, T


class PassportRecognizerByRegularExpression(BaseSyncRecognizer[Passport]):
    def __init__(
        self, serial_number_re: Optional[str] = None, number_re: Optional[str] = None
    ) -> None:
        if serial_number_re is None:
            serial_number_re = r"\d{2}[ \t]+\d{2}"
        if number_re is None:
            number_re = r"\d{6}"

        self.serial_number_re = re.compile(serial_number_re)
        self.number_re = re.compile(number_re)

    def __call__(self, response: ApiResponse) -> T:
        text_annotations = response.text

        serial_number = self.serial_number_re.search(text_annotations)
        number = self.number_re.search(text_annotations)

        return Passport(serial_number=serial_number.group(), number=number.group())
