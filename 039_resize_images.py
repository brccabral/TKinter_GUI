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
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")


my_img1 = ImageTk.PhotoImage(Image.open("images/0.jpg"))
# original is 320x320

# this just crop image on screen, but doesn't resize it
my_label = tk.Label(root, image=my_img1, height=160, width=160)
my_label.pack(pady=20)

# below here we resize the image on the fly
my_pic = Image.open("images/0.jpg")
resized = my_pic.resize((160, 160), Image.ANTIALIAS)

my_img2 = ImageTk.PhotoImage(resized)
my_label2 = tk.Label(root, image=my_img2)
my_label2.pack(pady=20)

root.mainloop()
