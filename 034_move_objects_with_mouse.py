import tkinter as tk
import os
from tkinter.constants import ANCHOR, NW

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("800x600")

w = 600
h = 400
x = w // 2
y = h // 2

my_canvas = tk.Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

img = tk.PhotoImage(file="images/star.png")
my_image = my_canvas.create_image(x, y, image=img)


def mouse_drag_drop(event: tk.Event):
    x, y = my_canvas.coords(my_image)
    x, y = event.x - x, event.y - y
    my_canvas.move(my_image, x, y)
    my_label.config(text=f"{event.x=} {event.y=} | {x=} {y=}")


my_canvas.bind("<B1-Motion>", mouse_drag_drop)

my_label = tk.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
