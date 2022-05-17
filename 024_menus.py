import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("400x400")

my_menu = tk.Menu(root)
root.config(menu=my_menu)


def our_command():
    tk.Label(root, text="You clicked").pack()


def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    tk.Label(file_new_frame, text="You file new").pack()


def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    tk.Label(edit_cut_frame, text="You edit cut").pack()


def hide_all_frames():
    # remove anything inside the frame
    for widget in file_new_frame.winfo_children():
        widget.destroy()
    for widget in edit_cut_frame.winfo_children():
        widget.destroy()

    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_command)

file_new_frame = tk.Frame(root, width=350, height=350, bg="red")
edit_cut_frame = tk.Frame(root, width=350, height=350, bg="blue")

root.mainloop()
