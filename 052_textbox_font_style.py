import tkinter as tk
import os
from tkinter import Button, Frame, Label, PhotoImage, Scrollbar, filedialog
from tkinter.constants import END, INSERT, RIGHT, SEL_FIRST, SEL_LAST, Y
import tkinter.font as tkFont
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
import _tkinter

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("500x600")

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

textbox = tk.Text(text_frame, width=30, height=15, font=('Helvetica', 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
textbox.pack(pady=10)

# textbox already scroll with mouse wheel
text_scroll.config(command=textbox.yview)

button_frame = Frame(root)
button_frame.pack()

def open_txt():
    buffer = ''
    filename = filedialog.askopenfilename(initialdir=".", title="Open a txt file", filetypes=(("Text files", "*.txt"),))
    if not filename:
        return
    with open(filename, "r") as text_file:
        buffer = text_file.read()
    textbox.insert(END, buffer)

    root.title(f"{os.path.basename(filename)} - Textpad")

def save_txt():
    filename = filedialog.asksaveasfilename(initialdir=".", title="Save a txt file", filetypes=(("Text files", "*.txt"),))
    if not filename:
        return
    with open(filename, "w") as text_file:
        text_file.write(textbox.get(1.0, END))


open_button = Button(button_frame, text="Open text file", command=open_txt)
open_button.grid(row=0, column=0, pady=10, padx=5)

save_button = Button(button_frame, text="Save to file", command=save_txt)
save_button.grid(row=0, column=1, pady=10, padx=5)

label = Label(root, text='')
label.pack()

def add_image():
    position = textbox.index(INSERT)
    label.config(text=position)
    textbox.image_create(position, image=image)

# PhotoImage can't open .jpg, use Pillow for .jpg
image = PhotoImage(file="images/star.png")
image_button = Button(button_frame, text="Add image", command=add_image)
image_button.grid(row=0, column=2, padx=5, pady=10)

def select_text():
    selected = textbox.selection_get()
    label.config(text=selected)

select_button = Button(button_frame, text="Select text", command=select_text)
select_button.grid(row=1, column=0, padx=5, pady=10)

def change_font(tag_name):
    current_tags = textbox.tag_names(SEL_FIRST)
    if tag_name in current_tags:
        textbox.tag_remove(tag_name, SEL_FIRST, SEL_LAST)
    else:
        textbox.tag_add(tag_name, SEL_FIRST, SEL_LAST)

bold_font = tkFont.Font(weight=tkFont.BOLD, family='Helvetica', size=16)
bold_button = Button(button_frame, text="Bold", font=bold_font, command=lambda: change_font("bold"))
bold_button.grid(row=1, column=1, padx=5, pady=10)

italic_font = tkFont.Font(slant=tkFont.ITALIC, family='Helvetica', size=16)
italic_button = Button(button_frame, text="Italic", font=italic_font, command=lambda: change_font("italic"))
italic_button.grid(row=1, column=2, padx=5, pady=10)

roman_font = tkFont.Font(slant=tkFont.ROMAN, family='Helvetica', size=16)
roman_button = Button(button_frame, text="Roman", font=roman_font, command=lambda: change_font("roman"))
roman_button.grid(row=1, column=3, padx=5, pady=10)

textbox.tag_configure("bold", font=bold_font)
textbox.tag_configure("italic", font=italic_font)
textbox.tag_configure("roman", font=roman_font)


def text_undo():
    try:
        textbox.edit_undo()
    except _tkinter.TclError as e:
        logging.debug(f'{e}')

def text_redo():
    try:
        textbox.edit_redo()
    except _tkinter.TclError as e:
        logging.debug(f'{e}')

undo_button = Button(button_frame, text="Undo", command=text_undo)
undo_button.grid(row=2, column=0)
redo_button = Button(button_frame, text="Redo", command=text_redo)
redo_button.grid(row=2, column=1)

label.config(text=f"{select_button.cget('text')=}")


print(tkFont.names())
print('')
defaultFont = tkFont.nametofont('TkDefaultFont')
print(defaultFont.actual())
print('')

print(list(tkFont.families()))


root.mainloop()