import tkinter as tk
import os
from tkinter import Button, Label, font, IntVar, StringVar

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("600x400")


def get_values():
    label.config(text=f"{spin.get()=} {spin2.get()=} {init_spin_int.get()=} {init_spin_str.get()=}")


init_spin_int = IntVar(root)
init_spin_int.set(0)

spin = tk.Spinbox(root, from_=0, to=50, font=('Helvetica', 20),
                  command=get_values, increment=2, textvariable=init_spin_int)
spin.pack(pady=10)

names = ["John", "Tim", "Mary", "Tina"]
init_spin_str = StringVar(root)
init_spin_str.set("John")

spin2 = tk.Spinbox(root, values=names, font=('Helvetica', 20),
                   command=get_values, textvariable=init_spin_str)
spin2.pack(pady=10)

button = Button(root, text="Submit", command=get_values)
button.pack(pady=10)

label = Label(root, text="")
label.pack(pady=10)


def reset_values():
    init_spin_int.set(0)
    init_spin_str.set("John")


reset_button = Button(root, text="Reset", command=reset_values)
reset_button.pack(pady=10)


root.mainloop()
