import tkinter as tk
import os
from tkinter import Button, Label, font

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

def get_values():
    label.config(text=f"{spin.get()=} {spin2.get()=}")

spin = tk.Spinbox(root, from_=0, to=10, font=('Helvetica', 20), increment=2)
spin.pack(pady=10)

names = ("John", "Tim", "Mary", "Tina")
spin2 = tk.Spinbox(root, values=names, font=('Helvetica', 20), command=get_values)
spin2.pack(pady=10)

button = Button(root, text="Submit", command=get_values)
button.pack(pady=10)

label = Label(root, text="")
label.pack(pady=10)


root.mainloop()