import datetime
from typing import Any


class Response:
    """
    The response wrapper.

    Attributes:
        date: The date when this crawl is executed.
        other: The other dict that will be flatten.
    """

    date: datetime.date
    other: dict[str, Any]

    def __init__(self, other: dict[str, Any]):
        self.date = datetime.date.today()
        self.other = other

    def to_dict(self):
        return {
            "date": self.date.strftime("%Y/%m/%d"),
            **self.other,
        }
