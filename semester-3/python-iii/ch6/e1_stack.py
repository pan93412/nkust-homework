import timeit
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class Stack(ABC, Generic[T]):
    @abstractmethod
    def push(self, element: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass


class ListStack(Stack):
    list = list[T | None]()

    def push(self, element: T) -> None:
        self.list.append(element)

    def pop(self) -> T:
        return self.list.pop()

    def __len__(self) -> int:
        return len(self.list)


class FixedStack(Stack):
    stack: list[T | None]
    ptr: int

    def __init__(self, size: int):
        self.stack = [None] * size
        self.ptr = 0

    def push(self, element: T) -> None:
        # if self.ptr + 1 >= len(self.stack):
        #     raise Exception("Stack overflow.")

        self.stack[self.ptr] = element
        self.ptr += 1

    def pop(self) -> T:
        # if self.ptr - 1 < 0:
        #     raise Exception("Stack exhausted.")

        self.ptr -= 1
        value = self.stack[self.ptr]

        return value

    def __len__(self) -> int:
        return self.ptr


if __name__ == "__main__":
    ls = ListStack()
    fs = FixedStack(128)

    def stack_benchmark(s: Stack) -> None:
        for i in range(100):
            s.push(i)

        while len(s) > 0:
            _ = s.pop()

    lst = timeit.timeit(lambda: stack_benchmark(ls))
    fst = timeit.timeit(lambda: stack_benchmark(fs))

    print("Improvement: ", (lst - fst) / lst * 100, "%", sep="")
