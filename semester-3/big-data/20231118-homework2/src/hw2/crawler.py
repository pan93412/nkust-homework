from typing import Callable, Generic, Type, TypeVar

import httpx
from executor import Executor
from extractor import Extractor
from serializer.serializer import Serializer
from structures.response import Response
from wrapper.wrapper import Wrapper

V = TypeVar("V")
O = TypeVar("O")


class Flow(Generic[O]):
    """A flow for crawling."""

    _executor: Executor | None
    _request: httpx.Request | None
    _execute_fn: Callable[[Extractor], Response] | None
    _serializer: Serializer[O] | None

    def request(self, request: httpx.Request) -> "Flow[O]":
        self._request = request
        return self

    def extract_with(self, extractor: Type[Extractor]) -> "Flow[O]":
        self._executor = Executor(extractor)
        return self

    def command(
        self, command: Callable[[Extractor], V], wrapper_class: Type[Wrapper[V]]
    ) -> "Flow[O]":
        wrapper = wrapper_class()
        self._execute_fn = lambda extractor: wrapper.wrap(command(extractor))
        return self

    def serializer(self, serializer: Type[Serializer[O]]) -> "Flow[O]":
        self._serializer = serializer()
        return self

    def execute(self) -> O:
        assert self._request is not None
        assert self._executor is not None
        assert self._execute_fn is not None
        assert self._serializer is not None

        response = self._executor.execute(self._request, self._execute_fn)
        return self._serializer.serialize_response(response)
