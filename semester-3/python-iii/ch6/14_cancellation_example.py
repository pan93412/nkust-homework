import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="\x1b[1m%(levelname)s\x1b[0m\t%(asctime)s\t| %(threadName)s\t| %(message)s",
)


def do_work(task_name: str) -> None:
    logging.debug("Start %s", task_name)
    t = threading.current_thread()
    elapsed_second = 0

    while not getattr(t, "terminate", False):
        logging.info("Working on %s (%ds)", task_name, elapsed_second)
        elapsed_second += 1
        time.sleep(1)

    logging.info("Completed %s. %d seconds elapsed.", task_name, elapsed_second)


if __name__ == "__main__":
    tasks = [
        ("Downloading video", 6),
        ("Downloading audio", 4),
        ("Downloading subtitle", 3),
    ]

    tasks_of_thread = list[threading.Thread]() * len(tasks)

    # Sort the task time.
    tasks.sort(key=lambda task: task[1])

    for (task_name, task_estimate_sec) in tasks:
        t = threading.Thread(target=do_work, args=(task_name,))
        t.start()

        tasks_of_thread.append(t)

    last_waited_seconds = 0
    for (task_id, (_, task_estimate_sec)) in enumerate(tasks):
        time.sleep(task_estimate_sec - last_waited_seconds)
        tasks_of_thread[task_id].terminate = True
        last_waited_seconds = task_estimate_sec

    for t in tasks_of_thread:
        t.join()
