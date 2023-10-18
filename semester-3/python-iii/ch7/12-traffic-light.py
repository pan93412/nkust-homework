import functools
from tkinter import Tk, Canvas, Button, Misc
from tkinter.ttk import Label, Frame, Scale
from typing import Callable


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("C111156103 – Traffic Light Example")


class Light:
    element: int

    def __init__(self, master: Canvas, fill: str = "red"):
        x = master.winfo_reqwidth() // 2
        y = master.winfo_reqheight() // 2
        r = x // 2

        self.master = master
        self.fill = fill
        self.element = master.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            fill="#000000",
            outline="black",
            tags="light",
        )

    def pack(self) -> None:
        return  # no-op

    def turn_on(self):
        self.master.itemconfig(self.element, fill=self.fill)
        self.master.update()

    def turn_off(self):
        self.master.itemconfig(self.element, fill="#000000")
        self.master.update()


class LightChangeLoop:
    paused = True
    counter = 0

    def __init__(self, interval: int = 300):
        """
        Star the light-changing loop.

        :param interval: The interval between each color changes in millisecond.
        """
        self.canvas = Canvas
        self.interval = interval

    def toggle(self) -> None:
        self.paused = not self.paused

    def set_interval(self, interval: int) -> None:
        self.interval = interval

    def change_color(self, lights: list[Light]) -> None:
        # if paused, do nothing
        if self.paused:
            return

        active_idx = self.counter % len(lights)
        for idx, light in enumerate(lights):
            if idx == active_idx:
                light.turn_on()
            else:
                light.turn_off()
        self.counter += 1

    def loop(self, canvas: Canvas, lights: list[Light]) -> None:
        self.change_color(lights)
        canvas.after(self.interval, functools.partial(self.loop, canvas, lights))


class Control(Frame):
    def __init__(self, master: Misc, toggle_fn: Callable[[], None], speed_change_fn: Callable[[int], None], *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.toggle_fn = toggle_fn

        # First column: Frame Indicator
        frame_indicator = Frame(self)
        frame_description = Label(frame_indicator, text="Frame:")
        frame_description.grid(row=0, column=0)
        self.frame_number = Label(frame_indicator, text="")
        self.frame_number.grid(row=0, column=1)
        frame_indicator.grid(row=0, column=0)

        # Second column: Playback Control
        playback_control = Frame(self)
        playback_control_button = Button(
            playback_control, text="Play / Pause", command=toggle_fn
        )
        playback_control_button.grid(row=0, column=0)
        playback_control_speed = Scale(
            playback_control,
            from_=0,
            to=1000,
            value=500,
            command=lambda value: speed_change_fn(int(float(value))),
        )
        playback_control_speed.grid(row=1, column=0)
        playback_control.grid(row=1, column=0)

    def update_frame_count(self, n: int) -> None:
        self.frame_number.config(text=str(n))
        self.update()


class CounterChangeLoop:
    def __init__(self, llloop: LightChangeLoop, interval: int = 300) -> None:
        self.interval = interval
        self.llloop = llloop

    def loop(self, control: Control) -> None:
        control.update_frame_count(self.llloop.counter)
        control.after(self.interval, functools.partial(self.loop, control))


def main() -> None:
    app = App()

    root = Canvas(app, height=320, width=240)
    root.pack()

    # Create three children canvas, and use grid to lay them out
    lights = list[Light]()
    for i, color in enumerate(["red", "yellow", "green"]):
        canvas = Canvas(root, width=50, height=50)
        canvas.grid(column=i, row=0)

        element = Light(canvas, color)
        element.pack()

        lights.append(element)

    llloop = LightChangeLoop()
    llloop.loop(root, lights)

    control = Control(app, lambda: llloop.toggle(), lambda i: llloop.set_interval(i), padding=8)
    control.pack()

    ccloop = CounterChangeLoop(llloop, 50)
    ccloop.loop(control)

    app.bind("<space>", lambda _: llloop.toggle())
    app.mainloop()


if __name__ == "__main__":
    main()
