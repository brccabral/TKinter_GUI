import tkinter as tk
import os
from tkinter import Button, Frame, Label, Menu, PhotoImage, Scrollbar, filedialog
from tkinter.constants import BOTTOM, E, END, INSERT, RIGHT, SEL_FIRST, SEL_LAST, SUNKEN, X, Y
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
root.geometry("1200x660")

def clear():
    # here is different from others
    # it starts with 1.0 not 0
    textbox.delete(1.0, END)

text_frame = Frame(root)
text_frame.pack(pady=5)

text_scroll = Scrollbar(text_frame)
text_scroll.pack(side=RIGHT, fill=Y)

textbox = tk.Text(text_frame, width=97, height=25, font=('Helvetica', 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
textbox.pack()

# textbox already scroll with mouse wheel
text_scroll.config(command=textbox.yview)

bold_font = tkFont.Font(weight=tkFont.BOLD, family='Helvetica', size=16)
italic_font = tkFont.Font(slant=tkFont.ITALIC, family='Helvetica', size=16)
roman_font = tkFont.Font(slant=tkFont.ROMAN, family='Helvetica', size=14)

textbox.tag_configure("bold", font=bold_font)
textbox.tag_configure("italic", font=italic_font)
textbox.tag_configure("roman", font=roman_font)

menu = Menu(root)
root.config(menu=menu)

def new_txt():
    pass

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

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_txt)
file_menu.add_command(label="Open", command=open_txt)
file_menu.add_command(label="Save", command=save_txt)

def cut_txt():
    pass

def copy_txt():
    pass

def paste_txt():
    pass

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

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_txt)
edit_menu.add_command(label="Copy", command=copy_txt)
edit_menu.add_command(label="Paste", command=paste_txt)
edit_menu.add_command(label="Undo", command=text_undo)
edit_menu.add_command(label="Redo", command=text_redo)

def change_font(tag_name):
    current_tags = textbox.tag_names(SEL_FIRST)
    if tag_name in current_tags:
        textbox.tag_remove(tag_name, SEL_FIRST, SEL_LAST)
    else:
        textbox.tag_add(tag_name, SEL_FIRST, SEL_LAST)

font_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Bold", command=lambda: change_font("bold"))
font_menu.add_command(label="Italic", command=lambda: change_font("italic"))
font_menu.add_command(label="Roman", command=lambda: change_font("roman"))

# PhotoImage can't open .jpg, use Pillow for .jpg
image = PhotoImage(file="images/star.png")

def add_image():
    position = textbox.index(INSERT)
    textbox.image_create(position, image=image)

def select_text():
    selected = textbox.selection_get()

status_bar = Label(root, text='Ready ', relief=SUNKEN, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

print(tkFont.names())
print('')
defaultFont = tkFont.nametofont('TkDefaultFont')
print(defaultFont.actual())
print('')

print(list(tkFont.families()))


root.mainloop()