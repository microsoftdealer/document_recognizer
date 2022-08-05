import dataclasses
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class DriverLicense:
    name: Optional[str] = None
    patronymic: Optional[str] = None
    birthday: Optional[datetime] = None

    issue_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None

    code: Optional[int] = None

    abode: Optional[str] = None

    def __post_init__(self):
        if self.name:
            self.name = self.name.title()
        if self.patronymic:
            self.patronymic = self.patronymic.title()
        if self.abode:
            self.abode = self.abode.title().strip(".")
