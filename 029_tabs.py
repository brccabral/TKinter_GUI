import tkinter as tk
from tkinter import Button, Frame, Label, ttk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

def hide_frame():
    my_notebook.hide(1)

def show_frame():
    my_notebook.add(my_frame2, text="Red tab")

def select_frame():
    my_notebook.select(1)

def add_label():
    my_label = Label(my_frame2, text="This is tab 2")
    my_label.pack()

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
# https://stackoverflow.com/questions/563827/how-to-stop-tkinter-frame-from-shrinking-to-fit-its-contents
# pack_propagate(False) = when we pack a label into a frame, the frame shrinks
# use pack_propagate() or grid_propagate() to avoid it
my_frame1.pack_propagate(False)
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")
my_frame2.pack_propagate(False)

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Blue tab")
my_notebook.add(my_frame2, text="Red tab")


my_button = Button(my_frame1, text="Hide tab 2", command=hide_frame).pack()
my_button2 = Button(my_frame1, text="Show tab 2", command=show_frame).pack(pady=10)
my_button3 = Button(my_frame1, text="Navigate to tab 2", command=select_frame).pack(pady=10)
my_button4 = Button(my_frame1, text="Add label to 2", command=add_label).pack(pady=10)

root.mainloop()