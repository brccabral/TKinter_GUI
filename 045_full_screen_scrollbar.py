import tkinter as tk
from tkinter import Button, Canvas, Event, Frame, ttk
import os
from tkinter.constants import BOTH, LEFT, NW, RIGHT, VERTICAL, Y
import logging

logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("500x400")

# Create a main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a Canvas
canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)


def scroll_canvas(x, y, z=None):
    logging.debug(f"{x=} {y=} {z=}")
    canvas.yview(x, y, z)


def mouse_wheel_pages(event: Event):
    logging.debug(f"mousewheel {event=}")
    canvas.yview("scroll", -1 if event.num == 4 else 1, "pages")


def mouse_wheel_units(event: Event):
    logging.debug(f"mousewheel {event=}")
    canvas.yview("scroll", -1 if event.num == 4 else 1, "units")


# Add a scrollbar to the Canvas
scrollbar = ttk.Scrollbar(canvas, orient=VERTICAL, command=scroll_canvas)
scrollbar.pack(side=RIGHT, fill=Y)


# Configure the Canvas
canvas.config(yscrollcommand=scrollbar.set)
canvas.configure(scrollregion=canvas.bbox("all"))
canvas.bind(
    "<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
)
if os.name == "nt":
    canvas.bind("<MouseWheel>", mouse_wheel_units)
else:
    canvas.bind("<Button-4>", mouse_wheel_units)
    canvas.bind("<Button-5>", mouse_wheel_units)

# Create ANOTHER Frame inside the Canvas
work_frame = Frame(canvas, background="red")

# Add that new Frame to a window in the Canvas
canvas.create_window((0, 0), window=work_frame, anchor=NW)

for i in range(100):
    Button(work_frame, text=f"Button {i}").grid(row=i, column=0, pady=10, padx=10)


root.mainloop()
