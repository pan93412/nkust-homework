import logging
import threading
import time

def do_work() -> None:
    print("Start task.")
    t = threading.current_thread()
    elapsed_second = 0

    while not getattr(t, "terminate", False):
        print(f"Elapsed {elapsed_second} seconds…")
        elapsed_second += 1
        time.sleep(1)

    print(f"Terminated by `terminate` attribute.")


if __name__ == "__main__":
    t = threading.Thread(target=do_work)
    t.start()

    time.sleep(5)
    t.terminate = True
    t.join()
