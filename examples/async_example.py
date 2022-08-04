import asyncio
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from google.cloud.vision_v1 import ImageAnnotatorClient
from google.oauth2 import service_account

from document_recognition.async_client import AsyncDocumentRecognition
from document_recognition.backends.asynchronous import AsyncBackendWrapper
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
from document_recognition.template import Template
from document_recognition.utils import to_async

BASE_DIR = Path(__file__).parent.resolve()


async def main() -> None:
    # pass template here, see example in tests/data
    template = Template.from_xml(BASE_DIR / "template.xml")

    # create our recognizer
    recognizer = to_async()(DriverLicenseRecognizerByTemplate(template=template))
    # run in thread pool executor, although it's pointless because there isn't io operations
    pre_processor = CV2HomographyPhotoPreProcessorByTemplate(
        template=template,
        percent=10,
    )
    # unfortunately, we can't run cv2 in process pool executor because some objects are unpickable.

    document_recognizer = AsyncDocumentRecognition(
        backend=AsyncBackendWrapper(  # wrap backend to run in thread pool executor
            GoogleVisionBackend(
                image_annotator_client=ImageAnnotatorClient(
                    credentials=service_account.Credentials.from_service_account_file(
                        str(BASE_DIR / "key.json")  # pass key file here
                    )
                )
            )
        ),
    )

    recognized_document = await document_recognizer.recognize_document(
        image_path=BASE_DIR
        / "user_licenses"
        / "1.jpg",  # pass photo here, see example in tests/data
        recognizer=recognizer,
        pre_processor_of_photo=pre_processor,
    )
    recognized_document: DriverLicense  # pycharm doesn't know that it's a DriverLicense, although mypy does
    print(recognized_document)


if __name__ == "__main__":
    asyncio.run(main())
