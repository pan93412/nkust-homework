import threading
import time


def job1(thread_id: int) -> None:
    for run_round in range(0, thread_id):
        print(f"JOB 1\t{run_round}\t{time.ctime(time.time())}")
        time.sleep(1)


def job2(thread_id: int) -> None:
    for run_round in range(0, thread_id):
        print(f"JOB 2\t{run_round}\t{time.ctime(time.time())}")
        time.sleep(1)


jobs = [job1, job2]
threads = 8

threads_item = list[threading.Thread]()

for target in jobs:
    t = threading.Thread(target=target, args=(threads,))
    threads_item.append(t)
    t.start()

for i in threads_item:
    t.join()

print("Finish.")
