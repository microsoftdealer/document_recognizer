### What is this?
- This is library which is created to recognize the text of the forms in the images.
- It is based on the [Google Vision Api](https://cloud.google.com/vision/docs/), but can be used with any other OCR.
- Supports both sync and async.


### Installation

``` bash
pip3 install -U git+https://github.com/Fom123/document_recognizer.git
```

### How to use it?

``` python
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
        / "1.jpg",  # pass photo here, see example in tests/data
        recognizer=recognizer,
        pre_processor_of_photo=pre_processor,
    )
    recognized_document: DriverLicense  # pycharm doesn't know that it's a DriverLicense, although mypy does
    print(recognized_document)


if __name__ == "__main__":
    main()
```

The following code will print the recognized document:
``` python
DriverLicense(name='АНДРЕЙ ЮРЬЕВИЧ', patronymic='НОВОЖИЛОВ', birthday=datetime.datetime(1984, 1, 19, 0, 0), issue_date=datetime.datetime(2012, 2, 21, 0, 0), expiration_date=datetime.datetime(2022, 2, 21, 0, 0), four_digit_code=None, six_digit_code=None, abode='Калининградская обл .')
```

You can also check another examples in the [examples](https://github.com/Fom123/document_recognizer/tree/main/examples)

