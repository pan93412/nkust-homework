import os
import threading

from queue import Queue
from typing import Generic, TypeVar

queue = Queue[int](128)

T = TypeVar("T")


class ContextManagedQueue(Generic[T]):
    def __init__(self, inner_queue: Queue[T]):
        self.queue = inner_queue

    def __enter__(self):
        return self.queue.get()

    def __exit__(self, exc_type, exc_value, traceback):
        return self.queue.task_done()


wq = ContextManagedQueue(queue)
semaphore = threading.Semaphore()


def consumer():
    while True:
        with wq as entry:
            with semaphore as _:
                print(
                    "{:<6d}".format((entry**2 + entry * 8 + entry % 4) % 10**5),
                    queue.qsize(),
                    sep="\t",
                )


def producer():
    for i in range(0, 10**5):
        queue.put(i)


if __name__ == "__main__":
    for i in range(0, os.cpu_count() // 2):
        threading.Thread(target=consumer, daemon=True).start()

    for i in range(0, os.cpu_count() // 2):
        threading.Thread(target=producer, daemon=True).start()

    queue.join()
    print("Done.")
