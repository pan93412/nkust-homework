import datetime
import sqlite3

from loguru import logger
import httpx
from selectolax.lexbor import LexborHTMLParser

from hw3 import extract_news, migrate

url = "https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw"

sqlite3.register_adapter(datetime.date, lambda date: date.isoformat())
sqlite3.register_adapter(datetime.datetime, lambda date: date.isoformat())


def main() -> None:
    logger.info("Start crawling {}…", url)
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()

    logger.info("Parsing HTML…")
    html = response.text
    tree = LexborHTMLParser(html)

    logger.info("Extract news…")
    news_list = extract_news(tree)

    logger.info("Putting to news.db…")
    with sqlite3.connect("news.db") as conn:
        migrate(conn)

        for news in news_list:
            logger.debug("Putting {} ({})", news.title, news.date)
            conn.execute(
                """
                INSERT INTO news (date, title, abstract)
                VALUES (?, ?, ?)
                """,
                (news.date, news.title, news.abstract),
            )


if __name__ == "__main__":
    main()
