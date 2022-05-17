import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")

options = ["Monday", "Tuesday", "Wednesday"]

str_value = tk.StringVar()
str_value.set(options[1])  # if don't set, no value will be selected when start

drop = tk.OptionMenu(root, str_value, *options)
drop.pack()


def show_value():
    tk.Label(root, text=str_value.get()).pack()


my_button = tk.Button(root, text="Show selection", command=show_value)
my_button.pack()

root.mainloop()
