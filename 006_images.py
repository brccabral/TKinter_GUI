import tkinter as tk
import os
from tkinter.constants import ACTIVE, DISABLED, E, SUNKEN, W

# tkinter doesn't work with jpg
from PIL import ImageTk, Image

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")

my_img1 = ImageTk.PhotoImage(Image.open("images/0.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/4.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

current_index = 0

# use a Frame() with pack_propagate() to avoid shrinking window
frame = tk.Frame(root, width=320, height=320)
frame.grid(row=0, column=0, columnspan=3)
frame.pack_propagate(False)
image_holder = tk.Label(frame, image=image_list[current_index])
image_holder.pack()

# relief=SUNKEN - give a look of is going inside the screen
# anchor=E - puts text aligned to the East
status_label = tk.Label(
    root,
    text=f"Image {current_index+1} of {len(image_list)}",
    bd=1,
    relief=SUNKEN,
    anchor=E,
)
# sticky=W+E - stretches the label on both directions West and East
status_label.grid(row=2, column=0, columnspan=3, sticky=W + E)


def image_loop(index):
    global current_index
    current_index += index
    button_back.config(state=ACTIVE)
    button_next.config(state=ACTIVE)

    if current_index <= 0:
        current_index = 0
        button_back.config(state=DISABLED)

    if current_index >= len(image_list) - 1:
        current_index = len(image_list) - 1
        button_next.config(state=DISABLED)

    # # apply new image
    image_holder.config(image=image_list[current_index])

    # # change status text
    status_label.config(text=f"Image {current_index+1} of {len(image_list)}")
    status_label.grid_propagate(False)


button_back = tk.Button(root, text="<<", command=lambda: image_loop(-1), state=DISABLED)
button_quit = tk.Button(root, text="Exit program", command=root.quit)
button_next = tk.Button(root, text=">>", command=lambda: image_loop(1))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()
