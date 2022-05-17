import tkinter as tk
import os
import platform

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

        info = f"System: {platform.system()}\n \
        User Name: {platform.node()}\n \
        Release: {platform.release()}\n \
        Version: {platform.version()}\n \
        Machine: {platform.machine()}\n \
        Processor: {platform.processor()}\n \
        Python Version: {platform.python_version()}\n \
        Platform: {platform.platform()}\n \
        Build: {platform.python_build()}\n \
        Compiler: {platform.python_compiler()}\n \
        Branch: {platform.python_branch()}\n \
        Revision: {platform.python_revision()}\n \
        Implementation: {platform.python_implementation()}\n \
        "

        self.label = tk.Label(self.root, text=info, font="-size 14")
        self.label.pack(padx=5, pady=5)
        

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
