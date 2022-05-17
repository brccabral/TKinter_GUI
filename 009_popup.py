import tkinter as tk
import os
from tkinter import Button, messagebox


root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")


def popup_info():
    # ok="ok" ESC="ok"
    response = messagebox.showinfo("This is my popup", "Hello")
    print(f"{response}")


def popup_warn():
    # ok="ok" ESC="ok"
    response = messagebox.showwarning("This is my popup", "Hello")
    print(f"{response}")


def popup_error():
    # ok="ok" ESC="ok"
    response = messagebox.showerror("This is my popup", "Hello")
    print(f"{response}")


def popup_askquestion():
    # yes="yes" or no="no", can't ESC to cancel
    response = messagebox.askquestion("Question", "Go forward?")
    print(f"{response}")


def popup_askokcancel():
    # ok=True or cancel=False, ESC=False
    response = messagebox.askokcancel("Question", "Accept change?")
    print(f"{response}")


def popup_askretrycancel():
    # retry=True or cancel=False, ESC=False
    # it plays warning sound
    response = messagebox.askretrycancel("Question", "Can't open")
    print(f"{response}")


def popup_askyesno():
    # yes=True or no=False, can't ESC to cancel
    response = messagebox.askyesno("Question", "Go left?")
    print(f"{response}")


def popup_askyesnocancel():
    # yes=True or no=False or cancel=None
    response = messagebox.askyesnocancel("Question", "Yes, no or cancel?")
    print(f"{response}")


Button(root, text="Info", command=popup_info).pack()
Button(root, text="Warning", command=popup_warn).pack()
Button(root, text="Error", command=popup_error).pack()
Button(root, text="Ask question", command=popup_askquestion).pack()
Button(root, text="Ask ok or cancel", command=popup_askokcancel).pack()
Button(root, text="Ask retry or cancel", command=popup_askretrycancel).pack()
Button(root, text="Ask yes or no", command=popup_askyesno).pack()
Button(root, text="Ask yes or no or cancel", command=popup_askyesnocancel).pack()

root.mainloop()
