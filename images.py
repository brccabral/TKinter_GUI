import tkinter as tk
import os
from tkinter.constants import DISABLED, E, SUNKEN, W
from PIL import ImageTk, Image

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

my_img1 = ImageTk.PhotoImage(Image.open("images/0.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/4.jpg"))

image_list = [
    my_img1,
    my_img2,
    my_img3,
    my_img4,
    my_img5
    ]

current_index = 0

image_holder: tk.Label = tk.Label(image=image_list[current_index])
image_holder.grid(row=0, column=0, columnspan=3)

# relief=SUNKEN - give a look of is going inside the screen
# anchor=E - puts text aligned to the East
status_label = tk.Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
# sticky=W+E - stretches the label on both directions West and East
status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)

def image_loop(index):
    global current_index, image_holder, button_back, button_next, status_label
    current_index += index
    
    button_back = tk.Button(root, text="<<", command=lambda: image_loop(-1))
    button_next = tk.Button(root, text=">>", command=lambda: image_loop(1))

    if current_index <= 0:
        current_index = 0
        button_back = tk.Button(root, text="<<", command=lambda: image_loop(-1), state=DISABLED)
        
    if current_index >= len(image_list)-1:
        current_index = len(image_list) - 1
        button_next = tk.Button(root, text=">>", command=lambda: image_loop(1), state=DISABLED)
    
    # need to grid button again
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    
    # apply new image
    image_holder.grid_forget()
    image_holder = tk.Label(image=image_list[current_index])
    image_holder.grid(row=0, column=0, columnspan=3)

    # change status text
    status_label = tk.Label(root, text=f"Image {current_index+1} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = tk.Button(root, text="<<", command=lambda: image_loop(-1), state=DISABLED)
button_quit = tk.Button(root, text="Exit program", command=root.quit)
button_next = tk.Button(root, text=">>", command=lambda: image_loop(1))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()