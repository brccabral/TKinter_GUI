import tkinter as tk
from tkinter.constants import DISABLED

root = tk.Tk()
root.geometry("400x900")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))

def myClick():
    myLabel = tk.Label(root, text="You clicked")
    myLabel.pack()

myButton = tk.Button(root, text="Click me!")
myButton.pack()
myButton2 = tk.Button(root, text="Can't click me!", state=DISABLED)
myButton2.pack()

myButton3 = tk.Button(root, text="Click me!", padx=50, pady=25, command=myClick)
myButton3.pack()
myButton4 = tk.Button(root, text="Click me!", padx=50, pady=25, foreground="blue", background="green", highlightbackground="yellow", highlightcolor="white")
myButton4.pack()
myButton5 = tk.Button(root, text="Click me!", padx=50, pady=25, fg="white", bg="red", highlightbackground="magenta", highlightcolor="#00FFFF", highlightthickness=5)
myButton5.pack()

buttons_styles = ["flat", "groove", "raised", "ridge", "solid", "sunken"]
for s in buttons_styles:
    tk.Button(root, text=f"Style {s}", relief=s, overrelief=s, font=('Helvetica',20)).pack()

root.mainloop()