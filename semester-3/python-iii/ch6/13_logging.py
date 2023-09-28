import concurrent.futures
import logging
import time
from typing import Generator

logging.basicConfig(
    level=logging.DEBUG,
    format="\x1b[1m%(levelname)s\x1b[0m\t%(asctime)s\t| %(threadName)s\t| %(message)s",
)


def wait_then_log(sec: int):
    time.sleep(sec)
    logging.info("waited %d seconds", sec)


def multi_thread_time_delay() -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for i in range(0, 20, 2):
            futures.append(executor.submit(wait_then_log, i))

    # Wait for all futures to complete.
    concurrent.futures.wait(futures)


if __name__ == "__main__":
    multi_thread_time_delay()
