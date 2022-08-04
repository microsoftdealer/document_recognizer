from functools import cached_property
from io import BytesIO
from pathlib import Path
from typing import Optional, BinaryIO

import cv2
import numpy as np

from document_recognition.backends.base import PathLike
from document_recognition.photo_pre_processors.base import BaseSyncPhotoPreProcessor
from document_recognition.template import Template


def read_image_from_pathlike(image_path: PathLike) -> np.ndarray:
    if isinstance(image_path, (str, Path)):
        image = cv2.imread(image_path)
    else:
        image = cv2.imdecode(np.frombuffer(image_path.read(), np.uint8), 1)
    return image


class TemplateImage:
    def __init__(self, image_path: PathLike, orb: cv2.ORB):
        self._image_path = image_path
        self._orb = orb

    @cached_property
    def image(self) -> np.ndarray:
        return read_image_from_pathlike(self._image_path)

    @cached_property
    def height(self) -> int:
        return self.image.shape[0]

    @cached_property
    def width(self) -> int:
        return self.image.shape[1]

    @cached_property
    def kp_and_des(self) -> np.ndarray:
        return self._orb.detectAndCompute(self.image, None)


class CV2HomographyPhotoPreProcessorByTemplate(BaseSyncPhotoPreProcessor):
    def __init__(
        self,
        template: Template,
        orb: Optional[cv2.ORB] = None,
        bf: Optional[cv2.BFMatcher] = None,
        percent: float = 50,
    ) -> None:
        if orb is None:
            orb = cv2.ORB_create(nfeatures=30000)
        if bf is None:
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        self.orb = orb
        self.bf = bf
        self.template_img = TemplateImage(str(template.path), orb=orb)
        self.percent = percent

    def __call__(
        self,
        image_path: PathLike,
        destination: Optional[PathLike] = None,
        seek: bool = True,
    ) -> Optional[BinaryIO]:
        if destination is None:
            destination = BytesIO()

        # read the image
        img = read_image_from_pathlike(image_path)

        # detect the keypoints and compute the descriptors
        kp, des = self.orb.detectAndCompute(img, None)
        template_kp, template_des = self.template_img.kp_and_des

        # match the descriptors
        matches = self.bf.match(des, template_des)
        # sort the matches in the order of their distance
        matches = sorted(matches, key=lambda x: x.distance)

        # get the good matches
        good = matches[: int(len(matches) * (self.percent / 100))]

        # get the coordinates of the good matches
        src_points = np.float32([kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_points = np.float32([template_kp[m.trainIdx].pt for m in good]).reshape(
            -1, 1, 2
        )

        # compute the homography matrix
        try:
            m, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)
        except cv2.error:
            raise ValueError("Could not find a homography")

        # apply the homography matrix
        img_scan = cv2.warpPerspective(
            img, m, (self.template_img.width, self.template_img.height)
        )

        if isinstance(destination, (str, Path)):
            cv2.imwrite(destination, img_scan)
            return
        is_success, buffer = cv2.imencode(".jpg", img_scan)
        destination.write(buffer)
        if seek:
            destination.seek(0)
        return destination
