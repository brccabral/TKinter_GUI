import tkinter as tk
import os
from tkinter import Button, messagebox


root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

def popup_info():
    messagebox.showinfo("This is my popup", "Hello")

def popup_warn():
    messagebox.showwarning("This is my popup", "Hello")

def popup_error():
    messagebox.showerror("This is my popup", "Hello")

Button(root, text="Info", command=popup_info).pack()
Button(root, text="Warning", command=popup_warn).pack()
Button(root, text="Error", command=popup_error).pack()

root.mainloop()