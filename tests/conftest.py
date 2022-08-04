from pathlib import Path
from typing import Generator

import pytest

from document_recognition.photo_pre_processors.synchronous.homography_cv2_ import (
    CV2HomographyPhotoPreProcessorByTemplate,
)
from document_recognition.recognizers.synchronous.driver_license_recognizer import (
    DriverLicenseRecognizerByTemplate,
)
from document_recognition.recognizers.synchronous.passport_recognizer import PassportRecognizerByRegularExpression
from document_recognition.template import Template, Size, Data, Coordinates
from tests.mocked_sync_client import MockedSyncDocumentRecognition

BASE_DIR = Path(__file__).parent
TEMPLATE_XML = BASE_DIR / "data" / "template.xml"
TEMPLATE_PNG = BASE_DIR / "data" / "template.png"


@pytest.fixture
def homography_cv2_pre_processor(
    template: Template,
) -> Generator[CV2HomographyPhotoPreProcessorByTemplate, None, None]:
    yield CV2HomographyPhotoPreProcessorByTemplate(template=template)


@pytest.fixture()
def document_recognizer() -> Generator[MockedSyncDocumentRecognition, None, None]:
    document_recognizer = MockedSyncDocumentRecognition()
    yield document_recognizer


@pytest.fixture()
def driver_license_recognizer_by_template(
    template: Template,
) -> Generator[DriverLicenseRecognizerByTemplate, None, None]:
    yield DriverLicenseRecognizerByTemplate(template=template)


@pytest.fixture()
def passport_recognizer_by_regular_expression():
    yield PassportRecognizerByRegularExpression()


@pytest.fixture()
def template() -> Template:
    return Template(
        path=TEMPLATE_PNG,
        size=Size(width=617, height=366, depth=3),
        objects=[
            Data(
                name="name",
                type="str",
                coordinates=Coordinates(
                    x_min=250.0, y_min=110.0, x_max=1000.0, y_max=130.0
                ),
                pose="Unspecified",
                truncated=False,
                difficult=False,
            ),
            Data(
                name="patronymic",
                type="str",
                coordinates=Coordinates(
                    x_min=250.0, y_min=65.0, x_max=1000.0, y_max=96.0
                ),
                pose="Unspecified",
                truncated=False,
                difficult=False,
            ),
            Data(
                name="birthday",
                type="datetime",
                coordinates=Coordinates(
                    x_min=250.0, y_min=149.0, x_max=360.0, y_max=161.0
                ),
                pose="Unspecified",
                truncated=False,
                difficult=False,
            ),
            Data(
                name="issue_date",
                type="datetime",
                coordinates=Coordinates(
                    x_min=250.0, y_min=203.0, x_max=360.0, y_max=220.0
                ),
                pose="Unspecified",
                truncated=False,
                difficult=False,
            ),
            Data(
                name="expiration_date",
                type="datetime",
                coordinates=Coordinates(
                    x_min=430.0, y_min=203.0, x_max=550.0, y_max=220.0
                ),
                pose="Unspecified",
                truncated=False,
                difficult=False,
            ),
            Data(
                name="four_digit_code",
                type="int",
                coordinates=Coordinates(
                    x_min=245.0, y_min=260.0, x_max=300.0, y_max=280.0
                ),
                pose="Unspecified",
                truncated=False,
                difficult=False,
            ),
            Data(
                name="six_digit_code",
                type="int",
                coordinates=Coordinates(
                    x_min=303.0, y_min=262.0, x_max=400.0, y_max=280.0
                ),
                pose="Unspecified",
                truncated=False,
                difficult=False,
            ),
            Data(
                name="abode",
                type="str",
                coordinates=Coordinates(
                    x_min=245.0, y_min=282.0, x_max=800.0, y_max=300.0
                ),
                pose="Unspecified",
                truncated=False,
                difficult=False,
            ),
        ],
    )
