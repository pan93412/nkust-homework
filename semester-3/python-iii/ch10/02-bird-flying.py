import functools
import operator
from tkinter import Tk, Canvas
from typing import Literal

from PIL import ImageTk

(
    pillar_width,
    piston_width,
    piston_height,
    opened_width,
    pillar_offset,
    bird_pillar_offset,
) = (48, 64, 32, 84, 60, 24)

tk = Tk()
canvas = Canvas(tk, width=640, height=640, bg="blue")
canvas.pack()

# Get the height of the pillar.
pillar_height = (canvas.winfo_reqheight() - (piston_height * 2)) // 2

# Get the x coordinate of pillars and pistons.
pillar_left_x = (canvas.winfo_reqwidth() // 2) - (pillar_width // 2) + pillar_offset
pillar_right_x = (canvas.winfo_reqwidth() // 2) + (pillar_width // 2) + pillar_offset
piston_left_x = (canvas.winfo_reqwidth() // 2) - (piston_width // 2) + pillar_offset
piston_right_x = (canvas.winfo_reqwidth() // 2) + (piston_width // 2) + pillar_offset

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

# Consturct the birds
bird_image = [
    ImageTk.PhotoImage(file="assets/f1.png"),
    ImageTk.PhotoImage(file="assets/f2.png"),
    ImageTk.PhotoImage(file="assets/f3.png"),
]
killed_image = ImageTk.PhotoImage(file="assets/f3.png")
bird = canvas.create_image(0, 0, image=bird_image[0], anchor="nw")

global_state = "close"

def animate_bird(x=0):
    # Cycle the bird.
    if x >= canvas.winfo_reqwidth():
        canvas.after(50, functools.partial(animate_bird, 0))
        return

    new_bird_image = bird_image[x % 2]

    k = pillar_left_x - bird_pillar_offset
    C = canvas.winfo_reqheight() // 2

    # https://www.desmos.com/calculator/jdoiyjymjo
    canvas.coords(bird, x, C if x > k else (C / k) * x)
    bird_left_x, _ = canvas.coords(bird)

    if global_state == "close" and piston_left_x < bird_left_x < piston_right_x:
        canvas.itemconfig(bird, image=bird_image[2])
    else:
        canvas.itemconfig(bird, image=new_bird_image)

    canvas.after(50, functools.partial(animate_bird, x + 3))


canvas.after(50, animate_bird)

def control_open_and_close(state: Literal["open", "close"]):
    global global_state

    # move the piston top and piston bottom half the opened_width.
    half_opened_width = opened_width // 2

    y_minus = (0, -half_opened_width, 0, -half_opened_width)
    y_plus = (0, +half_opened_width, 0, +half_opened_width)
    coord_op = lambda left, offset: tuple(map(operator.add, left, offset))

    # The evens will be - and the odds will be +.
    items_to_move = [
        pillar_top,
        pillar_bottom,
        piston_top,
        piston_bottom,
    ]

    match state:
        case "open":
            if global_state != "open":
                global_state = "open"
                for i, item in enumerate(items_to_move):
                    if i % 2 == 0:  # even
                        canvas.coords(item, coord_op(canvas.coords(item), y_minus))
                    else:  # odd
                        canvas.coords(item, coord_op(canvas.coords(item), y_plus))
        case "close":
            global_state = "close"
            for i, item in enumerate(items_to_move):
                if i % 2 == 0:  # even
                    canvas.coords(item, coord_op(canvas.coords(item), y_plus))
                else:  # odd
                    canvas.coords(item, coord_op(canvas.coords(item), y_minus))

            canvas.after(50, lambda: control_open_and_close("open"))


control_open_and_close("open")  # default
canvas.bind("<Button-1>", lambda event: control_open_and_close("close"))

tk.mainloop()
