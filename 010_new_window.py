import tkinter as tk
import os
from PIL import ImageTk, Image

root = tk.Tk()
root.title("TKinter GUI Window")
root.geometry("400x400")

image = 0
def open_window():
    # image needs to be global for python garbage collection
    # doesn't delete this
    global image
    top = tk.Toplevel()
    top.title("New window")
    if os.name == "nt":
        top.wm_iconbitmap(bitmap="python3.ico")
    else:
        top.wm_iconbitmap(bitmap="@python3.xbm")
    top.iconphoto(top._w, tk.PhotoImage(file='python3.png'))

    label = tk.Label(top, text="Hello top")
    label.pack()

    image = ImageTk.PhotoImage(Image.open("images/0.jpg"))
    img_holder = tk.Label(top, image=image)
    img_holder.pack()

    # top.destroy, not quit
    button = tk.Button(top, text="Close", command=top.destroy)
    button.pack()



button = tk.Button(root, text="Open new window", command=open_window)
button.pack()

root.mainloop()