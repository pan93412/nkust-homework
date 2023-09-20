import threading


def job(**kwargs: dict[str, str]) -> None:
    for i in kwargs:
        print(i, kwargs[i], "\t")


t = threading.Thread(
    target=job,
    kwargs={
        f"language{i + 1}": language
        for i, language in enumerate(["Python", "JavaScript", "PHP"])
    },
)

t.start()
for i in range(0, 3):
    print("Main thread", i)
t.join()

print("Finish.")
