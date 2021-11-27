import tkinter as tk
import os
from PIL import ImageTk, Image


class AppNewWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TKinter GUI Window")
        self.root.geometry("400x400")

        button = tk.Button(self.root, text="Open new window",
                           command=self.open_window)
        button.pack()

        # maximize
        button2 = tk.Button(self.root, text='zoomed',
                            command=self.window_zoomed)
        button2.pack(padx=5, pady=5)

        # hidden
        button3 = tk.Button(self.root, text='withdrawn',
                            command=self.window_withdrawn)
        button3.pack(padx=5, pady=5)

        # minimized
        button4 = tk.Button(self.root, text='iconic',
                            command=self.window_iconic)
        button4.pack(padx=5, pady=5)

        # normal
        button5 = tk.Button(self.root, text='normal',
                            command=self.window_normal)
        button5.pack(padx=5, pady=5)

        # minimizes
        button6 = tk.Button(self.root, text='iconify',
                            command=self.window_iconify)
        button6.pack(padx=5, pady=5)

        # minimizes
        button7 = tk.Button(self.root, text='deiconify',
                            command=self.window_deiconify)
        button7.pack(padx=5, pady=5)

        self.image = ImageTk.PhotoImage(Image.open("images/0.jpg"))

    def window_zoomed(self):
        self.top.state('zoomed') # Windows only

    def window_withdrawn(self):
        self.top.withdraw()

    def window_iconic(self):
        self.top.iconwindow()

    def window_normal(self):
        self.top.state('normal')

    def window_iconify(self):
        self.top.iconify() # doesn't work Ubuntu

    def window_deiconify(self):
        self.top.deiconify() # doesn't work Ubuntu

    def open_window(self):
        self.top = tk.Toplevel()
        self.top.wm_attributes()
        self.top.title("New window")
        if os.name == "nt":
            self.top.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.top.wm_iconbitmap(bitmap="@python3.xbm")
        self.top.iconphoto(self.top._w, tk.PhotoImage(file='python3.png'))

        label = tk.Label(self.top, text="Hello top")
        label.pack()

        img_holder = tk.Label(self.top, image=self.image)
        img_holder.pack()

        # top.destroy, not quit
        button = tk.Button(self.top, text="Close", command=self.top.destroy)
        button.pack()

    def start(self):
        self.root.mainloop()


def main():
    app = AppNewWindow()
    app.start()

if __name__ == "__main__":
    main()