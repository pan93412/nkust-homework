from typing import Awaitable, TypeVar, Callable, Type

import httpx
from loguru import logger

from hw2.extractor.extractor import Extractor

R = TypeVar("R")


class Executor:
    def __init__(self, extractor: Type[Extractor]):
        self.client = httpx.AsyncClient()
        self.extractor_class = extractor

    def new_extractor(self, content: bytes, headers: httpx.Headers) -> Extractor:
        return self.extractor_class(content=content, headers=headers, executor=self)

    async def get_response(self, request: httpx.Request) -> httpx.Response:
        response = await self.client.send(request)
        response.raise_for_status()

        return response

    async def execute(self, request: httpx.Request, command: Callable[[Extractor], Awaitable[R]]) -> R:
        logger.debug("Execute (using command '{}'): -> [{}] {}", command, request.method, request.url)
        response = await self.get_response(request)
        extractor = self.new_extractor(response.content, response.headers)

        return await command(extractor)
