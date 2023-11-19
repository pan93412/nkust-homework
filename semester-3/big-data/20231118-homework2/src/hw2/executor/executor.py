from typing import TypeVar, Callable, Type

import httpx
from loguru import logger

from hw2.extractor.extractor import Extractor

R = TypeVar("R")


class Executor:
    def __init__(self, extractor: Type[Extractor]):
        self.client = httpx.Client()
        self.extractor_class = extractor

    def new_extractor(self, content: bytes, headers: httpx.Headers) -> Extractor:
        return self.extractor_class(content=content, headers=headers, executor=self)

    def get_response(self, request: httpx.Request) -> httpx.Response:
        response = self.client.send(request)
        response.raise_for_status()

        return response

    def execute(self, request: httpx.Request, command: Callable[[Extractor], R]) -> R:
        logger.debug("Execute (using command '{}'): -> [{}] {}", command, request.method, request.url)
        response = self.get_response(request)
        extractor = self.new_extractor(response.content, response.headers)

        return command(extractor)
