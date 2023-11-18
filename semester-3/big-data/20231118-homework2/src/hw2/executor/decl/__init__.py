from abc import abstractmethod, ABC
from typing import TypeVar, Callable, Type

import httpx

R = TypeVar("R")


class ExecutorDecl(ABC):
    """
    ExecutorDecl is a basic Executor declaration to workaround circular imports.
    """

    @abstractmethod
    def execute(
        self, request: httpx.Request, command: Callable[["ExtractorDecl"], R]
    ) -> R:
        pass
