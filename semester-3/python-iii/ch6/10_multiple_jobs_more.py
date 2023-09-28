import threading
import time
from typing import Callable


def new_job(job_id: int, wait_for: int) -> Callable[[int], None]:
    def job(thread_id: int) -> None:
        for run_round in range(0, thread_id):
            print(f"JOB {job_id}\t{run_round}\t{time.ctime(time.time())}")
            time.sleep(wait_for)

    return job


jobs = (new_job(i, i // 4) for i in range(1, 25))
threads = 8

threads_item = list[threading.Thread]()

for target in jobs:
    t = threading.Thread(target=target, args=(threads,))
    threads_item.append(t)
    t.start()

for i in threads_item:
    t.join()

print("Finish.")
