from pathlib import Path

from document_recognition.backends.synchronous.google_vision_backend import (
    GoogleVisionBackend,
)
from document_recognition.entities.drive_license import DriverLicense
from document_recognition.photo_pre_processors.synchronous.homography_cv2_ import (
    CV2HomographyPhotoPreProcessorByTemplate,
)
from document_recognition.recognizers.synchronous.driver_license_recognizer import (
    DriverLicenseRecognizerByTemplate,
)
from document_recognition.sync_client import SyncDocumentRecognition
from document_recognition.template import Template
from google.cloud.vision_v1 import ImageAnnotatorClient
from google.oauth2 import service_account

BASE_DIR = Path(__file__).parent.resolve()


def main() -> None:
    # pass template here, see example in tests/data
    template = Template.from_xml(BASE_DIR / "template.xml")

    # create our recognizer
    recognizer = DriverLicenseRecognizerByTemplate(
        template=template,
    )
    pre_processor = CV2HomographyPhotoPreProcessorByTemplate(
        template=template,
        percent=10,
    )

    document_recognizer = SyncDocumentRecognition(
        backend=GoogleVisionBackend(
            image_annotator_client=ImageAnnotatorClient(
                credentials=service_account.Credentials.from_service_account_file(
                    str(BASE_DIR / "key.json")  # pass key file here
                )
            )
        ),
    )

    recognized_document = document_recognizer.recognize_document(
        image_path=BASE_DIR
        / "user_licenses"
        / "4.jpg",  # pass photo here, see example in tests/data
        recognizer=recognizer,
        pre_processor_of_photo=pre_processor,
    )
    recognized_document: DriverLicense  # pycharm doesn't know that it's a DriverLicense, although mypy does
    print(recognized_document)


if __name__ == "__main__":
    main()
