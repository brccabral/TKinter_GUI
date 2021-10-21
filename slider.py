import tkinter as tk
import os
from tkinter.constants import HORIZONTAL

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

vertical = tk.Scale(root, from_=0, to=200)
vertical.pack()

horizontal = tk.Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


root.mainloop()