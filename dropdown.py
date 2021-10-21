import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

str_value = tk.StringVar()
str_value.set("Tuesday") # if don't set, no value will be selected when start

drop = tk.OptionMenu(root, str_value, "Monday", "Tuesday", "Wednesday")
drop.pack()

root.mainloop()