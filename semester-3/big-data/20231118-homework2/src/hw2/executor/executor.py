from typing import Any, Awaitable, TypeVar, Callable, Type

import httpx
from loguru import logger

from hw2.extractor.extractor import Extractor

R = TypeVar("R")


class Executor:
    client: httpx.AsyncClient | None = None

    def __init__(self, extractor: Type[Extractor]):
        self.extractor_class = extractor

    def new_extractor(self, content: bytes, headers: httpx.Headers) -> Extractor:
        return self.extractor_class(content=content, headers=headers, executor=self)

    async def get_response(self, request: httpx.Request) -> httpx.Response:
        client = self._get_client()

        response = await client.send(request)
        response.raise_for_status()

        return response

    async def execute(self, request: httpx.Request, command: Callable[[Extractor], Awaitable[R]]) -> R:
        logger.debug("Execute (using command '{}'): -> [{}] {}", command, request.method, request.url)
        response = await self.get_response(request)
        extractor = self.new_extractor(response.content, response.headers)

        return await command(extractor)

    def _get_client(self) -> httpx.AsyncClient:
        if not self.client:
            raise RuntimeError("Executor client is not initialized.")

        return self.client

    async def __aenter__(self):
        self.client = httpx.AsyncClient()

        return self

    async def __aexit__(
        self, *args: Any, **kwargs: Any
    ) -> bool | None:
        client = self._get_client()

        await client.aclose()
        self.client = None
