from typing import Awaitable, Callable, Generic, Type, TypeVar

import httpx
from executor import Executor
from extractor import Extractor
from serializer.serializer import Serializer
from structures.response import Response
from utils.fn_describer import FnDescriber, describe_fn
from wrapper.wrapper import Wrapper

V = TypeVar("V")
O = TypeVar("O")


class Flow(Generic[V, O]):
    """A flow for crawling."""

    _executor: Executor | None
    _request: httpx.Request | None
    _execute_fn: Callable[[Extractor], Awaitable[Response]] | None
    _display: list[Callable[[V], None]]

    def __init__(self) -> None:
        self._executor = None
        self._request = None
        self._execute_fn = None
        self._display = []

    def request(self, request: httpx.Request) -> "Flow[V, O]":
        self._request = request
        return self

    def extract_with(self, extractor: Type[Extractor]) -> "Flow[V, O]":
        self._executor = Executor(extractor)
        return self

    def command(
        self,
        command: Callable[[Extractor], Awaitable[V]],
        wrapper_class: Type[Wrapper[V]],
    ) -> "Flow[V, O]":
        wrapper = wrapper_class()

        @describe_fn("Execute command in flow")
        async def wrapped_execute_fn(extractor: Extractor) -> Response:
            assert self._request
            response = await command(extractor)

            for fn in self._display:
                fn(response)

            return wrapper.wrap(response)

        self._execute_fn = wrapped_execute_fn
        return self

    def display(self, fn: Callable[[V], None]) -> "Flow[V, O]":
        self._display.append(fn)
        return self

    def serializer(self, serializer: Type[Serializer[O]]) -> "Flow[V, O]":
        self._serializer = serializer()
        return self

    async def execute(self) -> O:
        assert self._request is not None
        assert self._executor is not None
        assert self._execute_fn is not None
        assert self._serializer is not None

        async with self._executor as e:
            response = await e.execute(self._request, self._execute_fn)
            return self._serializer.serialize_response(response)
