import functools
from tkinter import Tk, Canvas

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]


tk = Tk()

canvas = Canvas(tk, height=320, width=240, bg="#FAFAFA")
canvas.pack()


def create_light(background: Canvas) -> int:
    r = 60
    x = background.winfo_reqwidth() // 2
    y = background.winfo_reqheight() // 2
    element = background.create_oval(
        x - r, y - r, x + r, y + r, fill=colors[0], tags="light"
    )

    return element


class StopChangingHandler:
    stop = False

    def toggle(self) -> None:
        self.stop = not self.stop

    def stopped(self) -> bool:
        return self.stop


sch = StopChangingHandler()


def modify_light_color(background: Canvas, element: int, color_to_change: str) -> None:
    if sch.stopped():
        return

    background.itemconfig(element, fill=color_to_change)
    background.update()


def color_change_loop() -> None:
    interval = 1000

    for i, color in enumerate(colors):
        canvas.after(
            interval * i, functools.partial(modify_light_color, canvas, light, color)
        )

    # repeat the loop
    canvas.after(interval * (len(colors) - 1), color_change_loop)


light = create_light(canvas)
canvas.tag_bind("light", "<ButtonPress-1>", lambda _: sch.toggle())
color_change_loop()

color_change_loop()


if __name__ == "__main__":
    tk.mainloop()
