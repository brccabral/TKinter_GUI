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

def popup_askquestion():
    # yes or no
    messagebox.askquestion("Question", "Go forward?")

def popup_askokcancel():
    # ok or cancel
    messagebox.askokcancel("Question", "Accept change?")

def popup_askretrycancel():
    # retry or cancel
    messagebox.askretrycancel("Question", "Can't open")

def popup_askyesno():
    # yes or no
    messagebox.askyesno("Question", "Go left?")

def popup_askyesnocancel():
    # yes or no or cancel
    messagebox.askyesnocancel("Question", "Yes, no or cancel?")

Button(root, text="Info", command=popup_info).pack()
Button(root, text="Warning", command=popup_warn).pack()
Button(root, text="Error", command=popup_error).pack()
Button(root, text="Ask question", command=popup_askquestion).pack()
Button(root, text="Ask ok or cancel", command=popup_askokcancel).pack()
Button(root, text="Ask retry or cancel", command=popup_askretrycancel).pack()
Button(root, text="Ask yes or no", command=popup_askyesno).pack()
Button(root, text="Ask yes or no or cancel", command=popup_askyesnocancel).pack()

root.mainloop()