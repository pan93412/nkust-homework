import concurrent.futures
import queue
import threading
import time
from typing import Iterable


def job(L, q):
    q.put(sum(L))


def multithreading(L):
    q = queue.Queue()
    s = 0

    for i in range(4):
        t = threading.Thread(target=job, args=(L, q))
        t.start()
        t.join()
        s += q.get()

    print("multithreading, sum:", s)


def optimized_multithreading(l: Iterable[int]) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        result = sum(executor.map(sum, map(lambda _: l, range(4))))
        print("process pool, sum:", result)



def normal(L):
    s = sum(L)
    print("normal, sum:", s)


if __name__ == "__main__":
    L = list(range(1000000))

    start_time = time.time()
    normal(L * 4)
    print("normal time:", time.time() - start_time)

    start_time = time.time()
    multithreading(L)
    print("multithreading time:", time.time() - start_time)

    start_time = time.time()
    optimized_multithreading(L)
    print("optimized multithreading time:", time.time() - start_time)
