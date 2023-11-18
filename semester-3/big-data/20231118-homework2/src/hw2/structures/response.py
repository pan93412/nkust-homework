import datetime
from typing import Iterable

from .news import News, NewsList


class Response:
    """
    The response of the news crawler.

    Attributes:
        date: The date when this crawl is executed.
        news: The news list.
    """

    date: datetime.date
    news: list[News]

    def __init__(self):
        self.date = datetime.date.today()
        self.news = []

    def add_from_iterator(self, iterator: Iterable[News]) -> None:
        """
        Add news from an iterator.

        Args:
            iterator: An iterator with news entries.
        """
        self.news.extend(iterator)
