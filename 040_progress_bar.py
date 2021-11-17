import tkinter as tk
from tkinter import Button, Label, ttk
import os
import time
from tkinter.constants import HORIZONTAL

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("600x400")

my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
my_progress.pack(pady=10)

my_progress2 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode="indeterminate")
my_progress2.pack(pady=10)

def step_progress():
    my_progress['value'] += 20
    my_progress2['value'] += 20
    my_label.config(text=my_progress['value'])

def auto_progress():
    for x in range(5):
        my_progress['value'] += 20
        my_progress2['value'] += 20
        my_label.config(text=my_progress['value'])
        root.update_idletasks()
        time.sleep(1)

def start_progress():
    my_progress.start(20)
    my_progress2.start(20)

def stop_progress():
    my_progress.stop()
    my_progress2.stop()

my_button = Button(root, text="Progress Step", command=step_progress)
my_button.pack(pady=10)

my_button = Button(root, text="Progress Start", command=start_progress)
my_button.pack(pady=10)

my_button = Button(root, text="Progress Stop", command=stop_progress)
my_button.pack(pady=10)

my_button = Button(root, text="Progress Auto", command=auto_progress)
my_button.pack(pady=10)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()