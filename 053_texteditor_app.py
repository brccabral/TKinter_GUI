import tkinter as tk
import os, sys
from tkinter import Button, Event, Frame, Label, Menu, PhotoImage, Scrollbar, filedialog, colorchooser
from tkinter.constants import BOTTOM, E, END, HORIZONTAL, INSERT, NONE, RIGHT, SEL, SEL_FIRST, SEL_LAST, SUNKEN, X, Y
import tkinter.font as tkFont
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
import _tkinter

root = tk.Tk()
appname = "Textpad"
root.title(appname)
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
    import win32print
    import win32api
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("1200x660")

def clear():
    # here is different from others
    # it starts with 1.0 not 0
    textbox.delete(1.0, END)

buttons_frame = Frame(root)
buttons_frame.pack(pady=5)

text_frame = Frame(root)
text_frame.pack(pady=5)

text_scroll = Scrollbar(text_frame)
text_scroll.pack(side=RIGHT, fill=Y)
horizontal_scroll = Scrollbar(text_frame, orient=HORIZONTAL)
horizontal_scroll.pack(side=BOTTOM, fill=X)

textbox = tk.Text(text_frame, 
                width=97, 
                height=25, 
                font=('Helvetica', 16), 
                selectbackground="yellow", 
                selectforeground="black", 
                yscrollcommand=text_scroll.set, 
                undo=True, 
                wrap=NONE, 
                xscrollcommand=horizontal_scroll.set)
textbox.pack()

# textbox already scroll with mouse wheel
text_scroll.config(command=textbox.yview)
horizontal_scroll.config(command=textbox.xview)


original_font = tkFont.Font(root, textbox.cget('font'))

bold_font = tkFont.Font(root, textbox.cget('font'))
bold_font.configure(weight=tkFont.BOLD)
italic_font = tkFont.Font(root, textbox.cget('font'))
italic_font.configure(slant=tkFont.ITALIC)
roman_font = tkFont.Font(root, textbox.cget('font'))
roman_font.configure(slant=tkFont.ROMAN, size=14)

color_font = tkFont.Font(root, textbox.cget('font'))

textbox.tag_configure("bold", font=bold_font)
textbox.tag_configure("italic", font=italic_font)
textbox.tag_configure("roman", font=roman_font)

menu = Menu(root)
root.config(menu=menu)

def new_txt(event):
    textbox.delete(1.0, END)
    root.title(f'New file - {appname}')
    status_bar.config(text="New file        ")
    return "break" # this avoids default textbox behavior

def open_txt(event):
    buffer = ''
    filename = filedialog.askopenfilename(initialdir=".", title="Open a txt file", filetypes=(("Text files", "*.txt"),("HTML files", "*.html"),("Python files", "*.py"),("All files", "*.*")))
    if not filename:
        return
    textbox.delete("1.0", END)
    with open(filename, "r") as text_file:
        buffer = text_file.read()
    textbox.insert(END, buffer)
    status_bar.config(text=f"{filename}        ")
    root.title(f"{os.path.basename(filename)} - {appname}")
    return "break" # this avoids default textbox behavior

def save_txt(event):
    status_text = str(status_bar.cget('text')).strip()
    if status_text == "New file" or status_text == "Ready":
        return save_as_txt()
    filename = status_text.replace("Saved ", "")
    if not filename:
        return
    logging.debug(f'{filename}')
    with open(filename, "w") as text_file:
        text_file.write(textbox.get(1.0, END))
    status_bar.config(text=f"Saved {filename}        ")
    root.title(f"{os.path.basename(filename)} - {appname}")
    return "break" # this avoids default textbox behavior

def save_as_txt():
    # I didn't get how defaultextension= works
    filename = filedialog.asksaveasfilename(initialdir=".", title="Save file", filetypes=(("Text files", "*.txt"),("HTML files", "*.html"),("Python files", "*.py"),("All files", "*.*")))
    if not filename:
        return
    with open(filename, "w") as text_file:
        text_file.write(textbox.get(1.0, END))
    status_bar.config(text=f"Saved {filename}        ")
    root.title(f"{os.path.basename(filename)} - {appname}")

def print_file(event):
    filename = filedialog.askopenfilename(initialdir=".", title="Open a txt file", filetypes=(("Text files", "*.txt"),("HTML files", "*.html"),("Python files", "*.py"),("All files", "*.*")))
    if not filename:
        logging.debug(f'no file selected to print')
    if os.name == "nt":
        printer_name = win32print.GetDefaultPrinter()
        if not printer_name:
            logging.debug(f'printer not found')
            return
        win32api.ShellExecute(0, "print", filename, None, ".", 0)
    else:
        os.system(f"lpr {filename}")
        

    return "break" # this avoids default textbox behavior

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: new_txt(False), accelerator="Ctrl+n")
file_menu.add_command(label="Open", command=lambda: open_txt(False), accelerator="Ctrl+o")
file_menu.add_command(label="Save", command=lambda: save_txt(False), accelerator="Ctrl+s")
file_menu.add_command(label="Save as", command=save_as_txt)
file_menu.add_separator()
file_menu.add_command(label="Print file", command=lambda: print_file(False))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

textbox.bind("<Control-Key-n>", new_txt)
textbox.bind("<Control-Key-o>", open_txt)
textbox.bind("<Control-Key-s>", save_txt)
textbox.bind("<Control-Key-p>", print_file)

selected = None
def cut_txt(event):
    global selected
    if textbox.tag_ranges(SEL):
        selected = textbox.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
        textbox.delete(SEL_FIRST, SEL_LAST)
    return "break" # this avoids default textbox behavior

def copy_txt(event):
    global selected
    if textbox.tag_ranges(SEL):
        selected = textbox.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
    return "break" # this avoids default textbox behavior

def paste_txt(event):
    global selected
    selected = root.clipboard_get()
    textbox.insert(textbox.index(INSERT), selected)
    return "break" # this avoids default textbox behavior

def text_undo(event):
    try:
        textbox.edit_undo()
    except _tkinter.TclError as e:
        logging.debug(f'{e}')
    return "break" # this avoids default textbox behavior

def text_redo(event):
    try:
        textbox.edit_redo()
    except _tkinter.TclError as e:
        logging.debug(f'{e}')
    return "break" # this avoids default textbox behavior

def select_all(event):
    textbox.tag_add(SEL, 1.0, END)
    return "break" # this avoids default textbox behavior

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_txt(False), accelerator="Ctrl+x")
edit_menu.add_command(label="Copy", command=lambda: copy_txt(False), accelerator="Ctrl+c")
edit_menu.add_command(label="Paste", command=lambda: paste_txt(False), accelerator="Ctrl+v")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=lambda: text_undo(False), accelerator="Ctrl+z")
edit_menu.add_command(label="Redo", command=lambda: text_redo(False), accelerator="Ctrl+y")

textbox.bind("<Control-Key-x>", cut_txt)
textbox.bind("<Control-Key-c>", copy_txt)
textbox.bind("<Control-Key-v>", paste_txt)
textbox.bind("<Control-Key-a>", select_all)
textbox.bind("<Control-Key-z>", text_undo)
textbox.bind("<Control-Key-y>", text_redo)

def font_event(event: Event):
    if event.keysym == "b":
        change_font("bold")
    elif event.keysym == "i":
        change_font("italic")
    elif event.keysym == "r":
        change_font("roman")
    return "break" # this avoids default textbox behavior

def change_font(tag_name, color_hex=None):
    if not textbox.tag_ranges(SEL):
        logging.debug(f'no text selected')
        return
    current_tags = textbox.tag_names(SEL_FIRST)
    if tag_name == "colored":
        textbox.tag_add(color_hex, SEL_FIRST, SEL_LAST)
    elif tag_name in current_tags:
        textbox.tag_remove(tag_name, SEL_FIRST, SEL_LAST)
    else:
        textbox.tag_add(tag_name, SEL_FIRST, SEL_LAST)

def color_text():
    rgb, color_hex = colorchooser.askcolor()
    if color_hex:
        textbox.tag_configure(color_hex, foreground=color_hex)
        change_font("colored", color_hex)

def color_all_text():
    rgb, color_hex = colorchooser.askcolor()
    if color_hex:
        textbox.config(foreground=color_hex)

def color_background():
    rgb, color_hex = colorchooser.askcolor()
    if color_hex:
        textbox.config(background=color_hex)

font_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Bold", command=lambda: change_font("bold"))
font_menu.add_command(label="Italic", command=lambda: change_font("italic"))
font_menu.add_command(label="Roman", command=lambda: change_font("roman"))
font_menu.add_separator()
font_menu.add_command(label="Color selected", command=color_text)
font_menu.add_command(label="Color all", command=color_all_text)
font_menu.add_command(label="Color background", command=color_background)

textbox.bind("<Control-Key-b>", font_event)
textbox.bind("<Control-Key-i>", font_event)
textbox.bind("<Control-Key-r>", font_event)

bold_button = Button(buttons_frame, font=bold_font, text="B", command=lambda: change_font("bold"))
bold_button.grid(row=0, column=0, padx=5)
italic_button = Button(buttons_frame, font=italic_font, text="I", command=lambda: change_font("italic"))
italic_button.grid(row=0, column=1, padx=5)
roman_button = Button(buttons_frame, font=roman_font, text="R", command=lambda: change_font("roman"))
roman_button.grid(row=0, column=2, padx=5)
undo_button = Button(buttons_frame, text="Undo", command=lambda: text_undo(False))
undo_button.grid(row=0, column=3, padx=5)
redo_button = Button(buttons_frame, text="Redo", command=lambda: text_redo(False))
redo_button.grid(row=0, column=4, padx=5)
color_text_button = Button(buttons_frame, text="Color selected", command=color_text)
color_text_button.grid(row=0, column=5, padx=5)

# PhotoImage can't open .jpg, use Pillow for .jpg
image = PhotoImage(file="images/star.png")

def add_image():
    position = textbox.index(INSERT)
    textbox.image_create(position, image=image)


status_bar = Label(root, text='Ready        ', relief=SUNKEN, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

print(tkFont.names())
print('')
defaultFont = tkFont.nametofont('TkDefaultFont')
print(defaultFont.actual())
print('')

print(list(tkFont.families()))


root.mainloop()