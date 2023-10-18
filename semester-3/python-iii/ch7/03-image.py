from tkinter import Tk, Canvas, CENTER
from PIL import Image, ImageTk

root = Tk()
root.wm_title("C111156103 – Image Example")

img = Image.open("placeholder.jpg")
img_tk = ImageTk.PhotoImage(img)

canvas = Canvas(root, width=img.width * 1.2, height=img.height * 1.2)
canvas.pack()
canvas.create_image(canvas.winfo_reqwidth() // 2, canvas.winfo_reqheight() // 2, anchor=CENTER, image=img_tk)

if __name__ == "__main__":
    root.mainloop()
