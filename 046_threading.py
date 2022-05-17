import tkinter as tk
import os
import time
from random import randint
import threading

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")

label = tk.Label(root, text="Hello")
label.pack(pady=10)


def run_thread():
    threading.Thread(target=five_seconds).start()


def five_seconds():
    time.sleep(5)
    label.config(text=f"5 seconds is up {time.time()}")


# this won't work because the thread will be called right when the
# app starts. Needs to be a def FUNC or a lambda
# button = tk.Button(root, text="5 seconds", command=threading.Thread(target=five_seconds).start())

button = tk.Button(
    root,
    text="5 seconds",
    command=lambda: threading.Thread(target=five_seconds).start(),
)
# button = tk.Button(root, text="5 seconds", command=run_thread)
button.pack(pady=10)


def get_random():
    random_label.config(text=f"Random number: {randint(1,100)}")


button2 = tk.Button(root, text="Pick random number", command=get_random)
button2.pack(pady=10)

random_label = tk.Label(root, text="")
random_label.pack(pady=10)


root.mainloop()
