import tkinter as tk
# tkinter doesn't work with jpg
from PIL import ImageTk, Image
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

#

my_img1 = ImageTk.PhotoImage(Image.open("images/0.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/1.jpg"))

my_label = tk.Label(root, image=my_img1)
my_label.pack(pady=20)

def hover_in(event: tk.Event):
    my_label.config(image=my_img2)

def hover_out(event: tk.Event):
    my_label.config(image=my_img1)

my_label.bind("<Enter>", hover_in)
my_label.bind("<Leave>", hover_out)

root.mainloop()