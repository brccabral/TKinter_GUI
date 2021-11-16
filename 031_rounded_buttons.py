# there is no rounded buttons
# we need to use an image
import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("900x400")

def clicked():
    my_label.config(text="You clicked")

login_img = tk.PhotoImage(file="images/login.png")

img_label = tk.Label(image=login_img)
# img_label.pack(pady=20)

my_button = tk.Button(root, image=login_img, command=clicked, relief="flat", activebackground="#d9d9d9")
my_button.pack(pady=20)

my_label = tk.Label(root, text='')
my_label.pack(pady=20)

root.mainloop()