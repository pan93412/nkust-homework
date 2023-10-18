from tkinter import Tk, ttk
from tkinter.ttk import Progressbar, Button, Frame


def main() -> None:
    root = Tk()
    root.wm_title("C111156103 – Progress Bar Example")

    frame = Frame(root)
    frame.pack(padx=8, pady=8)

    bar = Progressbar(frame)
    bar.start(100)
    bar.grid(row=0, column=0, columnspan=2)

    start_button = Button(frame, text="Start", command=lambda: bar.start(100))
    start_button.grid(row=1, column=0)

    stop_button = Button(frame, text="Stop", command=lambda: bar.stop())
    stop_button.grid(row=1, column=1)

    root.mainloop()


if __name__ == "__main__":
    main()
