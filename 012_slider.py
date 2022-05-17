import tkinter as tk
import os
from tkinter.constants import HORIZONTAL, W

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")


def dynamic_size(value):
    tk.Label(root, text=value).pack()
    root.geometry(f"{horizontal.get()}x{vertical.get()}")


vertical = tk.Scale(root, from_=200, to=500, command=dynamic_size)
vertical.pack()

horizontal = tk.Scale(root, from_=200, to=400, orient=HORIZONTAL, command=dynamic_size)
horizontal.pack(anchor=W)


def show_hor():
    my_horizontal = tk.Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")


my_btn = tk.Button(root, text="Show horizontal", command=show_hor).pack()

root.mainloop()
