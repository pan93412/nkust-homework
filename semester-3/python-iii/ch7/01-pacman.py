from tkinter import Canvas, Tk, Button, Frame, Label, CHORD, ARC, PIESLICE
from tkinter.font import Font

RIGHT = 0
TOP = 90
LEFT = 180
BOTTOM = 270

pacman_r = 60
pacman_a = 60


def write_pacman(c: Canvas, orientation=RIGHT) -> int:
    r = pacman_r
    a = pacman_a

    # Find the center of the canvas.
    w = c.winfo_reqwidth()
    h = c.winfo_reqheight()

    # Get the center coordinates.
    (cx, cy) = (w // 2, h // 2)

    item = c.create_arc(
        cx - r,
        cy - r,
        cx + r,
        cy + r,
        extent=360 - a,
        width=10,
        start=orientation + a // 2,
        fill="yellow",
    )
    c.pack()

    return item


def on_pacman_change(c: Canvas, item: int, orientation: int) -> None:
    c.itemconfig(
        item,
        start=orientation + pacman_a // 2,
        fill=["yellow", "red", "green", "blue"][orientation // 90],
    )


root = Tk()
root.wm_title("C111156103 – Pacman Example")

frame = Frame(root, pady=16)
frame.pack()

# Create a font for title
font = Font(root, ("TkDefaultFont", 24, "bold"))
Label(frame, text="Pacman Orientation Example", font=font).grid(
    column=0, row=0, columnspan=4, pady=(0, 4)
)

canvas = Canvas(root, bg="lightgray", cursor="plus", width="640", height="360")
item = write_pacman(canvas)

for index, (text, orientation) in enumerate(
    [("Right", RIGHT), ("Top", TOP), ("Left", LEFT), ("Bottom", BOTTOM)]
):
    Button(
        frame,
        text=text,
        command=lambda orientation=orientation: on_pacman_change(
            canvas, item, orientation
        ),
    ).grid(column=int(index), row=1)

# demonstrating our three friends
canvas.create_arc(10, 35, 100, 135, style=ARC)
canvas.create_arc(110, 35, 200, 135, style=PIESLICE, fill="blue")
canvas.create_arc(210, 35, 310, 135, style=CHORD, fill="black")

if __name__ == "__main__":
    root.mainloop()
