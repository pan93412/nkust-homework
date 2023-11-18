import dataclasses
from datetime import datetime
from typing import Type

from .counter import Counter


@dataclasses.dataclass(frozen=True)
class News:
    seq: int
    title: str
    content: str
    date: datetime


class NewsList:
    _counter: Counter[int]
    _news: list[News]

    def __init__(self, counter_class: Type[Counter[int]]):
        self._counter = counter_class()
        self._news = []

    def add(self, title: str, content: str, date: datetime):
        self._news.append(News(self._counter.next(), title, content, date))

    def __iter__(self):
        return iter(self._news)

    def __repr__(self):
        return f"NewsList({self._news!r})"
