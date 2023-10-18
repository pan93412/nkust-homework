import functools
from tkinter import Tk, Canvas


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("C111156103 – Async Loop Example")


class Light:
    element: int

    def __init__(self, master: Canvas, radius: int = 60, fill: str = "#FFFFFF"):
        r = radius

        x = master.winfo_reqwidth() // 2
        y = master.winfo_reqheight() // 2

        self.master = master
        self.element = master.create_oval(
            x - r, y - r, x + r, y + r, fill=fill, tags="light"
        )

    def pack(self) -> None:
        return  # no-op

    def change_color(self, color: str) -> None:
        self.master.itemconfig(self.element, fill=color)
        self.master.update()


class LightChangeLoop:
    paused = False
    current_color_idx = 0

    def __init__(self, colors: list[str], interval: int = 1):
        """
        Star the light-changing loop.

        :param colors: The color list to change sequentially.
        :param interval: The interval between each color changes in seconds.
        """
        self.canvas = Canvas
        self.colors = colors
        self.interval = interval

    def toggle(self) -> None:
        self.paused = not self.paused

    def change_color(self, light: Light) -> None:
        # if paused, do nothing
        if self.paused:
            return

        color_idx = self.current_color_idx % len(self.colors)
        light.change_color(self.colors[color_idx])
        self.current_color_idx += 1

    def loop(self, canvas: Canvas, light: Light) -> None:
        self.change_color(light)
        canvas.after(int(self.interval * 1000), functools.partial(self.loop, canvas, light))


def main() -> None:
    app = App()
    canvas = Canvas(app, height=320, width=240, bg="#FAFAFA")
    canvas.pack()

    light = Light(canvas)
    light.pack()

    llloop = LightChangeLoop(
        ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"], 0.1
    )
    llloop.loop(canvas, light)

    app.bind("<space>", lambda _: llloop.toggle())
    app.mainloop()


if __name__ == "__main__":
    main()
