from tkinter import Canvas, Tk

root = Tk()
root.wm_title("C111156103 – Rectangle Example")

rectangle_parameters = [
    {},
    {"dash": (4, 4), "outline": "blue"},
    {"fill": "red"},
    {"outline": "blue"},
    {"width": 2},
    {"width": 3, "outline": "blue", "dash": (4, 4)},
    {"width": 4, "fill": "#FFB630", "outline": "#946000"},
    {"width": 5, "fill": "#CCCCFF", "outline": "#0a0", "dash": (5, 5)},
]

oval_parameters = [
    {},
    {"fill": "green"},
    {
        "width": 3,
        "outline": "red",
        "fill": "#F00078",
    },
    {"width": 5, "outline": "#006000"},
]

line_parameters = [
    {},
    {"width": 3, "fill": "#1C1CFF", "dash":(4,4)},
    {"width": 4},
    {"width": 5, "fill": "red"},
]

polygon_parameters = [
    ([40, 40, 60, 20, 80, 40, 80, 80, 40, 80], {}),
    ([100, 40, 120, 20, 140, 40, 140, 80, 100, 80], {"fill": "red"}),
    ([160, 80, 200, 80, 180, 20], {"fill": "green"}),
    ([220, 80, 260, 80, 240, 20], {"outline": "#1C1CFF"})
]

row_ptr = 0
for i, parameters in enumerate([rectangle_parameters, oval_parameters, line_parameters]):
    shape = ['rectangle', 'oval', 'line'][i]

    for i, param in enumerate(parameters):
        canvas = Canvas(root, cursor="plus", width="96", height="96")

        pad = 16

        w = canvas.winfo_reqwidth() - pad
        h = canvas.winfo_reqheight() - pad

        # dynamic way to create a specific shape
        getattr(canvas, f'create_{shape}')(pad, pad, w, h, **param)

        canvas.grid(column=i % 4, row=i // 4 + row_ptr)

    row_ptr += len(parameters) // 4

polygon_canvas = Canvas(root, cursor="plus", width="256", height="96")
polygon_canvas.grid(column=0, columnspan=4, row=row_ptr+1)

for (i, (args, kargs)) in enumerate(polygon_parameters):
    polygon_canvas.create_polygon(*args, **kargs)

# for (i, (args, kargs)) in enumerate(polygon_parameters):
#     canvas = Canvas(root, cursor="plus", width="96", height="96")
#
#     w = canvas.winfo_reqwidth() - pad
#     h = canvas.winfo_reqheight() - pad
#
#     canvas.create_polygon(*args, **param)
#
#     canvas.grid(column=i % 4, row=i // 4 + row_ptr)
#
# row_ptr += len(polygon_parameters) // 4

if __name__ == "__main__":
    root.mainloop()
