import cgi
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import httpx
from selectolax.lexbor import LexborNode, LexborHTMLParser

from hw2.structures import NewsList

if TYPE_CHECKING:
    from hw2.executor import Executor


class Extractor(ABC):
    """
    A multifunction extractor.

    extract_news:
        Extracts news from the given selector and stores them in the given storage.
    """

    content: bytes
    headers: httpx.Headers
    executor: "Executor"

    def __init__(
        self,
        executor: "Executor",
        content: bytes,
        headers: httpx.Headers | None = None,
    ):
        if headers is None:
            headers = httpx.Headers()

        self.content = content
        self.headers = headers
        self.executor = executor

    def _selector(self) -> LexborNode:
        content_type, options = cgi.parse_header(self.headers["content-type"])
        encoding = options.get("charset", "utf-8")

        if content_type != "text/html":
            raise Exception(f"unsupported content type: {content_type}")

        content = self.content.decode(encoding)
        return LexborHTMLParser(content).root or LexborNode()

    @classmethod
    def description(cls) -> str:
        return ""

    @abstractmethod
    def extract_news(self) -> NewsList:
        pass

    @abstractmethod
    def extract_news_content(self) -> str:
        pass
