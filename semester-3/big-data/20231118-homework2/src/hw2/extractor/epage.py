import asyncio
from datetime import datetime
from typing import Awaitable

from utils import FnDescriber

from .extractor import Extractor
from hw2.structures import NewsList, IncrementalCounter

import httpx

NEWS_BOX_SELECTOR = "div.mbox"
NEWS_TITLE_SELECTOR = "div.mtitle > a"
NEWS_DATE_SELECTOR = "i.mdate"
NEWS_CONTENT_SELECTOR = "div.mpgdetail"
NEWS_CONTENT_DATE_SELECTOR = ".ptinfoproperty"


class EpageNewsExtractor(Extractor):
    @classmethod
    def description(cls) -> str:
        return "Extracts news content from epage."

    async def extract_news(self) -> NewsList:
        nl = NewsList(IncrementalCounter)

        selector = self._selector()

        # News is stored in `mbox`.
        mbox = selector.css(NEWS_BOX_SELECTOR)

        title_text_queue: list[str] = [] * len(mbox)
        date_queue: list[datetime] = [] * len(mbox)
        content_queue: list[Awaitable[str]] = [] * len(mbox)

        for news in mbox:
            title = news.css_first(NEWS_TITLE_SELECTOR)
            date = news.css_first(NEWS_DATE_SELECTOR)

            if title is None or date is None:
                continue

            title_text = title.text().strip()
            title_url = title.attributes.get("href")
            if title_url is None:
                continue

            title_text_queue.append(title_text)
            date_queue.append(plain_date_to_datetime_date(date.text()))
            content_queue.append(
                self.executor.execute(
                    httpx.Request(method="GET", url=title_url),
                    FnDescriber[[Extractor], Awaitable[str]](
                        lambda extractor: extractor.extract_news_content(),
                        "Extract news content",
                    ),
                )
            )

        # gather the response
        response = await asyncio.gather(*content_queue)
        for title_text, date, content in zip(title_text_queue, date_queue, response):
            nl.add(title_text, content, date)

        return nl

    async def extract_news_content(self) -> str:
        selector = self._selector()
        content = selector.css_first(NEWS_CONTENT_SELECTOR)

        if content is None:
            return ""

        # skip date line
        date = content.css_first(NEWS_CONTENT_DATE_SELECTOR)
        if date:
            date.decompose()

        return content.text().strip()


def plain_date_to_datetime_date(plain_date: str) -> datetime:
    """
    Turn a plain date string into a ``datetime.date`` object.

    Example:
        >>> plain_date_to_datetime_date("2019-11-18")
        datetime.date(2019, 11, 18)
    """
    return datetime.strptime(plain_date.strip(), "%Y-%m-%d")
