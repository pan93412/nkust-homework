from datetime import datetime
from hw3.news import News
from selectolax.lexbor import LexborHTMLParser

NEWS_BOX_SELECTOR = "div.mbox"
NEWS_TITLE_SELECTOR = "div.mtitle > a"
NEWS_DATE_SELECTOR = "i.mdate"
NEWS_ABSTRACT_SELECTOR = ".mdetail"


def extract_news(selector: LexborHTMLParser) -> list[News]:
    # News is stored in `mbox`.
    mbox = selector.css(NEWS_BOX_SELECTOR)
    news_list: list[News] = [] * len(mbox)

    for news in mbox:
        title = news.css_first(NEWS_TITLE_SELECTOR)
        date = news.css_first(NEWS_DATE_SELECTOR)
        abstract = news.css_first(NEWS_ABSTRACT_SELECTOR)

        if title is None or date is None or abstract is None:
            continue

        news_list.append(
            News(
                date=plain_date_to_datetime_date(date.text()),
                title=title.text().strip(),
                abstract=abstract.text().strip(),
            )
        )

    return news_list


def plain_date_to_datetime_date(plain_date: str) -> datetime:
    """
    Turn a plain date string into a ``datetime.date`` object.

    Example:
        >>> plain_date_to_datetime_date("2019-11-18")
        datetime.date(2019, 11, 18)
    """
    return datetime.strptime(plain_date.strip(), "%Y-%m-%d")
