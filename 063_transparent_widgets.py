import tkinter as tk
import os
from tkinter import Button, Toplevel, ttk
from tkinter.constants import HORIZONTAL


class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, heigth=400):
        self.root = tk.Tk()
        self.appname = appname
        self.root.title(appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(
            f"{width}x{heigth}+{screen_width//2-width//2}+{screen_height//2-heigth//2}")

        self.label = tk.Label(self.root, text="My Label")
        self.label.pack(pady=10)

        self.set_alpha(1.0)

        # -transparentcolor only works on Windows
        self.transparentcolor = "#123456"
        self.root.wm_attributes('-transparentcolor', self.transparentcolor)

        self.slider = ttk.Scale(self.root, from_=0.1, to=1.0, value=0.7,
                                orient=HORIZONTAL, command=lambda alpha: self.set_alpha(self.slider.get()), length=200)
        self.slider.pack(pady=10)

        self.button = Button(self.root, text="New Window",
                             command=self.new_window)
        self.button.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.configure(bg="blue")
        # can't configure heigth= or width= on Windows Python 3.6
        # can't configure heigth= or width= on Linux Python 3.8
        # need to use dict[''] to configure them
        # self.frame.configure(heigth=200, width=200, bg="blue")
        # self.frame.config(heigth=200, width=200, bg="blue")
        self.frame['height'] = 200
        self.frame['width'] = 200
        self.frame.pack(pady=10)

        self.frame_transparent = tk.Frame(self.root)
        self.frame_transparent.configure(bg=self.transparentcolor)
        self.frame_transparent['height'] = 200
        self.frame_transparent['width'] = 200
        self.frame_transparent.pack_propagate(False)
        self.frame_transparent.pack(pady=10, ipadx=5, ipady=5)

        self.label_frame = tk.Label(self.frame_transparent, text="Hello Transparent")
        self.label_frame.pack(pady=10)

    def set_alpha(self, alpha: float):
        # for some reason, wm_attributes() needs to be called before setting attributes()
        # Linux =   ('-alpha', 1.0, '-topmost', 0, '-zoomed', 0, '-fullscreen', 0, '-type', '')
        # Windows = ('-alpha', 1.0, '-transparentcolor', '', '-disabled', 0, '-fullscreen', 0, '-toolwindow', 0, '-topmost', 0)
        self.root.wm_attributes()
        self.root.attributes('-alpha', alpha)
        self.label.config(text=round(alpha, 2))

    def new_window(self):
        pop = Toplevel()
        pop.wm_attributes()
        pop.attributes('-alpha', 0.5)
        pop.bind("<Button-1>", lambda event: pop.attributes('-alpha', 1.0))

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("TkinterApp", 500, 800)
    app.start()


if __name__ == "__main__":
    main()
