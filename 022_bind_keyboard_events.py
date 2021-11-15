import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

def resize_root(newLabel: tk.Button):
    if not newLabel.winfo_ismapped():
        root.geometry(f"400x{root.winfo_height()+50}+{root.winfo_x()}+{root.winfo_y()-35}")

def clicker(event: tk.Event):
    myLabel = tk.Label(root, text=f"You clicked left button {event.x=} {event.y}")
    myLabel.pack()
    myLabel.after(1, resize_root, myLabel)

def clickerRight(event: tk.Event):
    myLabel = tk.Label(root, text=f"You clicked right button {event.x=} {event.y}")
    myLabel.pack()
    myLabel.after(1, resize_root, myLabel)

def enterButton(event: tk.Event):
    myLabel = tk.Label(root, text=f"You entered button {event.x=} {event.y}")
    myLabel.pack()
    myLabel.after(1, resize_root, myLabel)

def leaveButton(event: tk.Event):
    myLabel = tk.Label(root, text=f"You left button {event.x=} {event.y}")
    myLabel.pack()
    myLabel.after(1, resize_root, myLabel)

def focusInButton(event: tk.Event):
    myLabel = tk.Label(root, text=f"You focus in button 1")
    myLabel.pack()
    myLabel.after(1, resize_root, myLabel)

def focusOutButton(event: tk.Event):
    myLabel = tk.Label(root, text=f"You focus out button 1")
    myLabel.pack()

def returnButton(event: tk.Event):
    myLabel = tk.Label(root, text=f"You pressed enter button 1")
    myLabel.pack()
    myLabel.after(1, resize_root, myLabel)

def keyButton(event: tk.Event):
    myLabel = tk.Label(root, text=f"You pressed enter button 1 {event.keycode=} {event.char=} {event.keysym=}")
    myLabel.pack()
    myLabel.after(1, resize_root, myLabel)

myButton = tk.Button(root, text="Click me")
myButton.bind("<Button-1>", clicker)
myButton.bind("<Button-3>", clickerRight)
myButton.bind("<Enter>", enterButton)
myButton.bind("<Leave>", leaveButton)
myButton.bind("<FocusIn>", focusInButton)
myButton.bind("<FocusOut>", focusOutButton)
myButton.bind("<Return>", returnButton)
myButton.bind("<Key>", keyButton)
myButton.pack(pady=20)

myButton2 = tk.Button(root, text="Click me 2")
myButton2.pack(pady=20)

def resize_window(event: tk.Event):
    # pass
    print(f'{event.width=} {event.height=} {event.widget.__class__=}')

root.bind("<Configure>", resize_window)

root.mainloop()