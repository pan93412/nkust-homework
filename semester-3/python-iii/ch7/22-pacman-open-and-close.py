from enum import Enum
from tkinter import Canvas, Tk, Button, Frame, Label, CHORD, ARC, PIESLICE
from tkinter.font import Font


class Angle(Enum):
    OPEN = 60
    CLOSE = 1


class Pacman:
    canvas: Canvas
    item: int

    r = 60
    angle = Angle.OPEN

    def __init__(self, canvas: Canvas):
        self.canvas = canvas

        # Find the center of the canvas.
        w = canvas.winfo_reqwidth()
        h = canvas.winfo_reqheight()

        r = self.r

        # Get the center coordinates.
        (cx, cy) = (w // 2, h // 2)

        self.item = canvas.create_arc(
            cx - r,
            cy - r,
            cx + r,
            cy + r,
            width=10,
            fill="yellow",
            **self._get_pacman_angle_properties(),
        )
        print(self.item)

    def _update_item(self):
        self.canvas.itemconfig(self.item, **self._get_pacman_angle_properties())

    def _get_pacman_angle_properties(self) -> dict[str, int]:
        a = self.angle.value

        return {
            "extent": 360 - a,
            "start": a // 2,
        }

    def to_mode(self, mode: Angle) -> None:
        self.angle = mode
        self._update_item()


root = Tk()
root.wm_title("C111156103 – Pacman Example")

frame = Frame(root, pady=16)
frame.pack()

# Create a font for title
font = Font(root, ("TkDefaultFont", 24, "bold"))
Label(frame, text="Pacman Orientation Example", font=font).grid(
    column=0, row=0, columnspan=4, pady=(0, 4)
)

Button(frame, text="Open", command=lambda: pacman.to_mode(Angle.OPEN)).grid(
    column=1, row=1
)
Button(frame, text="Close", command=lambda: pacman.to_mode(Angle.CLOSE)).grid(
    column=2, row=1
)

canvas = Canvas(root, bg="lightgray", cursor="plus", width="640", height="360")
pacman = Pacman(canvas)
canvas.pack()

if __name__ == "__main__":
    root.mainloop()
