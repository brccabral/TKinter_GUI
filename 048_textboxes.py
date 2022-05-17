import tkinter as tk
import os
from tkinter import Button, Frame, Label
from tkinter.constants import END

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x600")


def clear():
    # here is different from others
    # it starts with 1.0 not 0
    textbox.delete(1.0, END)


def get_text():
    label.config(text=f"{textbox.get(1.0, END)}")


def get_lines():
    # get line 1.0 until 3.0 not included
    label.config(text=f"{textbox.get(1.0, 3.0)}")


textbox = tk.Text(root, width=30, height=15, font=("Helvetica", 16))
textbox.pack(pady=10)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=0, padx=10)

get_text_button = Button(button_frame, text="Get text", command=get_text)
get_text_button.grid(row=0, column=1, padx=10)

get_lines_button = Button(button_frame, text="Get lines", command=get_lines)
get_lines_button.grid(row=0, column=2, padx=10)

label = Label(root, text="")
label.pack()

root.mainloop()
