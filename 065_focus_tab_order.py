import tkinter as tk
import os


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

        # without "focus()", the definition order, not the pack(), is
        # the focus order
        self.white = tk.Entry(self.root, bg="white", font=('DejaVu Sans', 20))
        self.red = tk.Entry(self.root, bg="red", font=('DejaVu Sans', 20))
        self.blue = tk.Entry(self.root, bg="blue", font=('DejaVu Sans', 20))

        self.white.pack(pady=10)
        self.red.pack(pady=10)
        self.blue.pack(pady=10)

        # this sets the first focus, but the order is still the definition order
        self.red.focus()
        
        # use liff() to set the order you need
        self.set_focus_order()

    def set_focus_order(self):
        order = [self.red, self.white, self.blue]
        w: tk.Widget
        for w in order:
            w.lift()

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("TkinterApp", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
