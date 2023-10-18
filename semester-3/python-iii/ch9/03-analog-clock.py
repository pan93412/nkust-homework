import functools
import math
from datetime import datetime
from tkinter import Tk, Label, StringVar, Canvas

root = Tk()
canvas = Canvas(root, width=640, height=480, bg='skyblue')
canvas.pack()

cx, cy = canvas.winfo_reqwidth() // 2, canvas.winfo_reqheight() // 2

# circle
r = cx // 2
outline_width = 8
circle = canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline='darkblue', fill='lightgray', width=8)

# scale and text
for i in range(0, 360):
    # the out circle's radius
    start_r = r - outline_width // 2
    end_r = r - 10
    font_size = 18

    # --- scale ---
    scale = [
        cx + start_r * math.cos(math.radians(i)),
        cy + start_r * math.sin(math.radians(i)),
        cx + end_r * math.cos(math.radians(i)),
        cy + end_r * math.sin(math.radians(i))
    ]
    match (i % 6 == 0, i % 30 == 0):
        case (True, False):
            # Each 6 degrees, we draw a line.
            canvas.create_line(*scale, fill="black", width=2)
        case (_, True):
            # Each 30 degrees, we draw a bolder line and a text.
            canvas.create_line(*scale, fill="black", width=5)

            # --- text ---
            time_r = end_r - font_size // 2 - 1
            text = [
                cx + time_r * math.cos(math.radians(i)),
                cy + time_r * math.sin(math.radians(i))
            ]
            canvas.create_text(
                *text,
                # Begin from 90°.
                text=((i + 90) // 30) % 12 or 12,
                fill="black",
                font=("Times", font_size, "bold")
            )

# pointer
now = datetime.now()
color_map = {"hour": "brown", "minute": "blue", "second": "red"}
stroke_width_map = {"hour": 5, "minute": 4, "second": 2}
radius_map = {"hour": 70, "minute": 110, "second": 130}
value_map = {
    "hour": now.hour % 12,
    "minute": now.minute,
    "second": now.second
}


def update(elements: dict[str, int]) -> None:
    now = datetime.now()
    value_map = {
        "hour": now.hour % 12,
        "minute": now.minute,
        "second": now.second
    }

    for t in value_map:
        el = elements[t]
        vl = value_map[t]
        r = radius_map[t]
        canvas.coords(
            el,
            cx,
            cy,
            cx + r * math.cos(math.radians(vl * 6 - 90)),
            cy + r * math.sin(math.radians(vl * 6 - 90)))

    canvas.after(200, functools.partial(update, elements))



elements = {}
for (t, value) in value_map.items():
    elements[t] = canvas.create_line(
        cx,
        cy,
        cx + radius_map[t] * math.cos(math.radians(value * 6 - 90)),
        cy + radius_map[t] * math.sin(math.radians(value * 6 - 90)),
        fill=color_map[t],
        width=stroke_width_map[t]
    )
dot_r = 3
canvas.create_oval(cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r, fill="black", width=0)

update(elements)
root.mainloop()
