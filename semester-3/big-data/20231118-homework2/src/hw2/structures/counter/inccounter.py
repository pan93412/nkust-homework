from abc import ABC

from .counter import Counter


class IncrementalCounter(Counter[int], ABC):
    _counter: int

    def __init__(self):
        self._counter = 0

    def next(self) -> int:
        self._counter += 1
        return self._counter
