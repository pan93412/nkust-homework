from datetime import datetime

from .extractor import Extractor
from hw2.structures import NewsList, IncrementalCounter

NEWS_BOX_SELECTOR = "div.mbox"
NEWS_TITLE_SELECTOR = "div.mtitle > a ::text"
NEWS_DATE_SELECTOR = "i.mdate ::text"
NEWS_CONTENT_SELECTOR = "div.meditor"


class EpageNewsExtractor(Extractor):
    @classmethod
    def description(cls) -> str:
        return "Extracts news content from epage."

    def extract_news(self) -> NewsList:
        nl = NewsList(IncrementalCounter)

        selector = self._selector()

        # News is stored in `mbox`.
        mbox = selector.css(NEWS_BOX_SELECTOR)

        for news in mbox:
            title = news.css(NEWS_TITLE_SELECTOR).get()
            date = news.css(NEWS_DATE_SELECTOR).get()
            content = news.css(NEWS_CONTENT_SELECTOR).get()

            if title is None or date is None or content is None:
                continue

            nl.add(title.strip(), content.strip(), plain_date_to_datetime_date(date))

        return nl


def plain_date_to_datetime_date(plain_date: str) -> datetime.date:
    """
    Turn a plain date string into a ``datetime.date`` object.

    Example:
        >>> plain_date_to_datetime_date("2019-11-18")
        datetime.date(2019, 11, 18)
    """
    return datetime.strptime(plain_date.strip(), "%Y-%m-%d").date()
