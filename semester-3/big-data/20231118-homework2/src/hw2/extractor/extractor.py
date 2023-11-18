import cgi
from abc import ABC, abstractmethod

import httpx
import parsel

from hw2.executor.decl import ExecutorDecl
from hw2.structures import NewsList


class Extractor(ABC):
    """
    A multifunction extractor.

    extract_news:
        Extracts news from the given selector and stores them in the given storage.
    """

    content: bytes
    headers: httpx.Headers
    executor: ExecutorDecl

    def __init__(
        self,
        executor: ExecutorDecl,
        content: bytes,
        headers: httpx.Headers | None = None,
    ):
        if headers is None:
            headers = httpx.Headers()

        self.content = content
        self.headers = headers
        self.executor = executor

    def _selector(self) -> parsel.Selector:
        content_type, options = cgi.parse_header(self.headers["content-type"])
        encoding = options.get("charset", "utf-8")

        if content_type != "text/html":
            raise Exception(f"unsupported content type: {content_type}")

        content = self.content.decode(encoding)
        return parsel.Selector(content)

    @classmethod
    def description(cls) -> str:
        pass

    @abstractmethod
    def extract_news(self) -> NewsList:
        pass
