import dataclasses
from datetime import date


@dataclasses.dataclass(frozen=True)
class News:
    date: date
    title: str
    abstract: str
