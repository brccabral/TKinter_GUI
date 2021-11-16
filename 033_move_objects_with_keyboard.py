import tkinter as tk
import os
from tkinter.constants import ANCHOR, NW

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("800x600")

w = 600
h = 400
x = w//2
y = h//2

my_canvas = tk.Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# x1,y1,x2,y2 are the circle's outside rectangle
my_circle = my_canvas.create_oval(x, y, x+10, y+10, fill="cyan")

def move_left(event):
    x = -10
    y = 0
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_image, x, y)

def move_right(event):
    x = 10
    y = 0
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_image, x, y)

def move_up(event):
    x = 0
    y = -10
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_image, x, y)

def move_down(event):
    x = 0
    y = 10
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_image, x, y)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

def pressing(event: tk.Event):
    if event.char == "a":
        move_left(event)
    elif event.char == "d":
        move_right(event)
    elif event.char == "w":
        move_up(event)
    elif event.char == "s":
        move_down(event)

root.bind("<Key>", pressing)

img = tk.PhotoImage(file="images/star.png")
my_image = my_canvas.create_image(x, y, anchor=NW, image=img)

root.mainloop()