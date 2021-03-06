import tkinter as tk
import os
from tkinter import Button, Frame, Label, PhotoImage, Scrollbar, filedialog
from tkinter.constants import END, INSERT, RIGHT, Y

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x600")


def clear():
    # here is different from others
    # it starts with 1.0 not 0
    textbox.delete(1.0, END)


def get_text():
    label.config(text=f"{textbox.get(1.0, END)}")


def get_lines():
    # get line 1.0 until 3.0 not included
    label.config(text=f"{textbox.get(1.0, 3.0)}")


text_frame = Frame(root)
text_frame.pack(pady=10)

text_scroll = Scrollbar(text_frame)
text_scroll.pack(side=RIGHT, fill=Y)

textbox = tk.Text(
    text_frame,
    width=30,
    height=15,
    font=("Helvetica", 16),
    selectbackground="yellow",
    selectforeground="black",
    yscrollcommand=text_scroll.set,
)
textbox.pack(pady=10)

# textbox already scroll with mouse wheel
text_scroll.config(command=textbox.yview)

button_frame = Frame(root)
button_frame.pack()


def open_txt():
    buffer = ""
    filename = filedialog.askopenfilename(
        initialdir=".", title="Open a txt file", filetypes=(("Text files", "*.txt"),)
    )
    if not filename:
        return
    with open(filename, "r") as text_file:
        buffer = text_file.read()
    textbox.insert(END, buffer)


def save_txt():
    filename = filedialog.asksaveasfilename(
        initialdir=".", title="Save a txt file", filetypes=(("Text files", "*.txt"),)
    )
    if not filename:
        return
    with open(filename, "w") as text_file:
        text_file.write(textbox.get(1.0, END))


open_button = Button(button_frame, text="Open text file", command=open_txt)
open_button.grid(row=0, column=0, pady=10, padx=10)

save_button = Button(button_frame, text="Save to file", command=save_txt)
save_button.grid(row=0, column=1, pady=10, padx=10)

label = Label(root, text="")
label.pack()


def add_image():
    position = textbox.index(INSERT)
    label.config(text=position)
    textbox.image_create(position, image=image)


# PhotoImage can't open .jpg, use Pillow for .jpg
image = PhotoImage(file="images/star.png")
image_button = Button(button_frame, text="Add image", command=add_image)
image_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
