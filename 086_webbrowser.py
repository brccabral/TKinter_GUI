import tkinter as tk
import os
import webbrowser


class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, height=400):
        self.appname = appname
        self.width = width
        self.height = height

        self.root = tk.Tk()

        self.root.title(self.appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))

        self.button = tk.Button(self.root, text='Open web browser', command=lambda: self.open_web_browser(None))
        self.button.pack(padx=5, pady=5)
        self.button.config(cursor="fleur")

        self.label = tk.Label(self.root, text='Open web browser')
        self.label.pack(padx=5, pady=5)
        self.label.config(font="-size 24", fg="blue", cursor="fleur")
        self.label.bind("<Button-1>", self.open_web_browser)
        
        self.button = tk.Button(self.root, text='Open Firefox', command=lambda: self.open_firefox(None))
        self.button.pack(padx=5, pady=5)
        self.button.config(cursor="fleur")

    def open_web_browser(self, event: tk.Event):
        webbrowser.open_new("http://github.com")

    def open_firefox(self, event: tk.Event):
        if os.name == "nt":
            webbrowser.get('C:/Program Files/Mozilla Firefox/firefox.exe %s').open_new("http://github.com")
        else:
            webbrowser.get('firefox').open_new("http://github.com")


    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}")


def main():
    app = TkinterApp("TkinterApp", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
