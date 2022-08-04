import tempfile
from io import BytesIO
from pathlib import Path

import cv2
import numpy as np
import pytest

from document_recognition.photo_pre_processors.synchronous.homography_cv2_ import (
    CV2HomographyPhotoPreProcessorByTemplate,
)
from document_recognition.template import Template
from tests.conftest import BASE_DIR

IMAGES = list((BASE_DIR / "data" / "user_licenses").rglob("*"))


@pytest.mark.parametrize("image", IMAGES)
def test_homography_cv2_photo_pre_processor_by_template(
    homography_cv2_pre_processor: CV2HomographyPhotoPreProcessorByTemplate,
    template: Template,
    image: Path,
):
    assert homography_cv2_pre_processor.template_img.width == template.size.width
    assert homography_cv2_pre_processor.template_img.height == template.size.height

    photo = homography_cv2_pre_processor(image_path=str(image))

    assert isinstance(photo, BytesIO)

    decode_img = cv2.imdecode(np.frombuffer(photo.getbuffer(), np.uint8), -1)

    height, width, _ = decode_img.shape

    assert height == template.size.height
    assert width == template.size.width


def test_homography_cv2_photo_pre_processor_by_template_with_invalid_image(
    homography_cv2_pre_processor: CV2HomographyPhotoPreProcessorByTemplate,
    template: Template,
):
    with pytest.raises(ValueError):
        homography_cv2_pre_processor(image_path="invalid_image.jpg")


@pytest.mark.parametrize("image", IMAGES)
def test_homography_cv2_photo_pre_processor_by_template_output(
    homography_cv2_pre_processor: CV2HomographyPhotoPreProcessorByTemplate,
    image: Path,
):
    with tempfile.TemporaryDirectory() as directory:
        destination = Path(directory) / image.name

        homography_cv2_pre_processor(
            image_path=str(image), destination=str(destination)
        )

        assert destination.exists()
