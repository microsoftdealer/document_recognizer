import dataclasses
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class Passport:
    serial_number: Optional[str] = None
    number: Optional[str] = None
