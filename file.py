import tkinter as tk
import os
from tkinter import filedialog

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")


root.filename = filedialog.askopenfilename(initialdir="images", title="Select a file", filetypes=(("png files","*.png"),("all files", "*.*")))



root.mainloop()