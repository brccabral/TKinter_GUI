import tkinter as tk
import os
from tkinter import Button, Label, filedialog
from PIL import ImageTk, Image

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")

my_image = 0


def open_file():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="images",
        title="Select a file",
        filetypes=(("png files", "*.png"), ("all files", "*.*")),
    )

    my_label = Label(root, text=root.filename)
    my_label.grid(row=1, column=0)

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.grid(row=2, column=0)


button = Button(root, text="Open file", command=open_file)
button.grid(row=0, column=0)

root.mainloop()
