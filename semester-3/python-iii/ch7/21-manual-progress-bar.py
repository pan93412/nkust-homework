from tkinter import Tk, Misc, StringVar, DoubleVar
from tkinter.ttk import Progressbar, Button, Frame, Label


class Application(Frame):
    bar: Progressbar
    progress: DoubleVar

    def __init__(self, master: Misc):
        super().__init__(master)

        self.progress = DoubleVar(value="0.0")

        self.bar = Progressbar(self, mode="determinate", variable=self.progress)
        self.bar.grid(row=0, column=0, columnspan=2)

        start_button = Button(self, text="開始", command=self.next_step)
        start_button.grid(row=1, column=0)

        stop_button = Button(self, text="結束", command=self.reset)
        stop_button.grid(row=1, column=1)

        progress_area = Frame(self)
        progress_area.grid(row=2, column=0, columnspan=2)
        progress_desc = Label(progress_area, text="目前進度：")
        progress_desc.grid(row=0, column=0)

        progress_value = StringVar(value="0.0%")
        self.progress.trace_add(
            "write",
            lambda *_: progress_value.set(
                f"{self.progress.get()}%" if self.progress.get() != 100 else "完成"
            ),
        )
        progress_value_presentator = Label(progress_area, textvariable=progress_value)
        progress_value_presentator.grid(row=0, column=1)

    def next_step(self):
        if self.progress.get() == 100:
            return

        self.progress.set(self.progress.get() + 10)

    def reset(self):
        self.progress.set(0.0)


def main() -> None:
    root = Tk()
    root.wm_title("C111156103 – Manual Progress Bar Example")

    application = Application(root)
    application.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
