import tkinter as tk
from tkinter import Button, Label, colorchooser
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")


def getcolor():
    my_color = colorchooser.askcolor()
    Label(root, text=my_color).pack(pady=5)
    Label(root, text=my_color[0][0]).pack(pady=5)
    Label(root, text=my_color[0][1]).pack(pady=5)
    Label(root, text=my_color[0][2]).pack(pady=5)
    Label(root, text=my_color[1]).pack(pady=5)
    Label(root, text="You picked a color", font=("helvetica", 24), bg=my_color[1]).pack(
        pady=5
    )


my_button = Button(root, text="Pick a color", command=getcolor)
my_button.pack()

root.mainloop()
