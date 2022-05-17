import tkinter as tk
from tkinter import Button, Label, filedialog
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")


def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=f'"{my_program}"')
    # os.system(f"\"{my_program}\"")


my_button = Button(root, text="Open program", command=open_program)
my_button.pack()

my_label = Label(root, text="")
my_label.pack()

root.mainloop()
