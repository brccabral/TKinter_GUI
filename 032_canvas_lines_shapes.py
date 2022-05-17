import tkinter as tk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("500x500")

my_canvas = tk.Canvas(root, width=300, height=200, bg="white")
my_canvas.pack(pady=20)

my_canvas.create_rectangle(50, 150, 250, 50, fill="pink")

# x1,y1,x2,y2 are the circle's outside rectangle
my_canvas.create_oval(50, 150, 250, 50, fill="cyan")
my_canvas.create_oval(50, 50, 150, 150, fill="yellow")

my_canvas.create_line(10, 100, 290, 100, fill="red")
my_canvas.create_line(150, 10, 150, 190, fill="blue")


root.mainloop()
