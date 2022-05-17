import tkinter as tk
import os
import time
from tkinter import font

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("800x400")

my_label = tk.Label(root, text="Initial")
my_label.pack(pady=20)


def update_label():
    my_label.config(text="Updated")


my_label.after(5000, update_label)


def clock():
    my_clock.config(text=time.strftime("%I:%M:%S %p %A"))
    my_clock.after(1000, clock)


my_clock = tk.Label(
    root, text="Initial", font=("Helvetica", 48), fg="green", bg="black"
)
my_clock.pack(pady=20)
clock()

root.mainloop()
