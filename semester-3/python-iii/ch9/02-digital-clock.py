from datetime import datetime
from tkinter import Tk, Label, StringVar

root = Tk()
current_time = StringVar()
clock = Label(root, font=("Times", 20, "bold"), bg="skyblue", fg="black", padx=5, pady=5, textvariable=current_time)
clock.pack(expand=True, fill="both")


def tick() -> None:
    current_time.set(datetime.now().strftime("%I:%M:%S"))
    clock.after(200, tick)


tick()
root.mainloop()
