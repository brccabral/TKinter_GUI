import tkinter as tk
import os
import tkintermapview as tkmap


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
        self.root.iconphoto(self.root._w, tk.PhotoImage(file="python3.png"))

        # frame to hold map
        self.label_frame = tk.LabelFrame(self.root)
        self.label_frame.pack(padx=10, pady=10)

        # map widget
        self.map_widget = tkmap.TkinterMapView(
            self.label_frame, width=800, height=600, corner_radius=0
        )

        # set coordinates
        # self.map_widget.set_position(36.1699, -115.1396)  # Vegas

        # set address
        self.map_widget.set_address("Space Needle, Seattle WA, US")
        # set zoom
        self.map_widget.set_zoom(10)

        self.map_widget.pack()

        self.input_frame = tk.LabelFrame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.input_frame, font=("Helvetica", 28))
        self.entry.grid(row=0, column=0, pady=20, padx=10)

        self.button = tk.Button(self.input_frame, text="Lookup", command=self.lookup)
        self.button.grid(row=0, column=1, padx=10)

    def lookup(self):
        pass

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}"
        )


def main():
    app = TkinterApp("TkinterApp", 900, 800)
    app.start()


if __name__ == "__main__":
    main()
