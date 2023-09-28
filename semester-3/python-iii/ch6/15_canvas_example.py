import random
from tkinter import *

# Create a window object
window = Tk()
window.title("Canvas Text Example by Pan")

canvas = Canvas(window, width=640, height=480, bg='lightgray')
canvas.pack_configure()

canvas.create_text(320, 240, text="C111156103", font=("Arial", 32), fill='darkgray')
canvas.create_line(220, 270, 420, 270, fill='black', width=3)

canvas.bind("<Button-1>", lambda event: canvas.create_text(
    random.randint(0, 640),
    random.randint(0, 480),
    text="Hi",
    font=("Times", 12),
    fill='darkgray',
    anchor="nw"
))

window.mainloop()
