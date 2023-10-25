import operator
import sys
from tkinter import Tk, Canvas
from typing import Literal

pillar_width, piston_width, piston_height, opened_width = 48, 64, 32, 24

tk = Tk()
canvas = Canvas(tk, width=640, height=640, bg="blue")
canvas.pack()

# Get the height of the pillar.
pillar_height = (canvas.winfo_reqheight() - (piston_height * 2)) // 2

# Get the x coordinate of pillars and pistons.
pillar_left_x = (canvas.winfo_reqwidth() // 2) - (pillar_width // 2)
pillar_right_x = (canvas.winfo_reqwidth() // 2) + (pillar_width // 2)
piston_left_x = (canvas.winfo_reqwidth() // 2) - (piston_width // 2)
piston_right_x = (canvas.winfo_reqwidth() // 2) + (piston_width // 2)

# Construct the pillars.
pillar_top = canvas.create_rectangle(
    pillar_left_x,
    0,
    pillar_right_x,
    pillar_height,
    fill="green",
    width=3,
    outline="black",
)
piston_top = canvas.create_rectangle(
    piston_left_x,
    pillar_height,
    piston_right_x,
    pillar_height + piston_height,
    fill="red",
    width=3,
    outline="black",
)
piston_bottom = canvas.create_rectangle(
    piston_left_x,
    pillar_height + piston_height,
    piston_right_x,
    pillar_height + (piston_height * 2),
    fill="yellow",
    width=3,
    outline="black",
)
pillar_bottom = canvas.create_rectangle(
    pillar_left_x,
    pillar_height + (piston_height * 2),
    pillar_right_x,
    canvas.winfo_reqheight(),
    fill="white",
    width=3,
    outline="black",
)


def control_open_and_close(state: Literal["open", "close"]):
    # move the piston top and piston bottom half the opened_width.
    half_opened_width = opened_width // 2

    y_minus = (0, -half_opened_width, 0, -half_opened_width)
    y_plus = (0, +half_opened_width, 0, +half_opened_width)
    coord_op = lambda left, offset: tuple(map(operator.add, left, offset))
    closed = lambda item: canvas.coords(item)[1] - canvas.coords(item)[3] == 0

    # The evens will be - and the odds will be +.
    items_to_move = [
        pillar_top,
        pillar_bottom,
        piston_top,
        piston_bottom,
    ]

    match state:
        case "open":
            for i, item in enumerate(items_to_move):
                if i % 2 == 0:  # even
                    canvas.coords(item, coord_op(canvas.coords(item), y_minus))
                else:  # odd
                    canvas.coords(item, coord_op(canvas.coords(item), y_plus))
        case "close":
            for i, item in enumerate(items_to_move):
                if i % 2 == 0:  # even
                    canvas.coords(item, coord_op(canvas.coords(item), y_plus))
                else:  # odd
                    canvas.coords(item, coord_op(canvas.coords(item), y_minus))


canvas.bind("<Button-1>", lambda event: control_open_and_close("open"))
canvas.bind(
    "<Button-2>" if sys.platform == "darwin" else "<Button-3>",
    lambda event: control_open_and_close("close"),
)

tk.mainloop()
