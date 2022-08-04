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
