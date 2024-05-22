import tkinter as tk
from tkinter import filedialog

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("Extension Changer")

        self.label = tk.Label(self.root, text="Insert your file", font=('Arial', 18))
        self.label.pack(pady=20, padx=20)

        self.import_button = tk.Button(self.root, text="Import File", font=('Arial', 10))
        self.import_button.pack(pady=30)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)

        self.ratio_jpeg = tk.StringVar()
        self.ratio_png = tk.StringVar()
        self.ratio_pdf = tk.StringVar()
        self.ratio_svg = tk.StringVar()
        self.ratio_mp4 = tk.StringVar()


        self.ratio_button_jpeg = tk.Radiobutton(self.frame, text="JPEG", value="JPEG", variable=self.ratio_jpeg)
        self.ratio_button_png = tk.Radiobutton(self.frame, text="PNG", value="PNG", variable=self.ratio_png)
        self.ratio_button_pdf = tk.Radiobutton(self.frame, text="PDF", value="PDF", variable=self.ratio_pdf)
        self.ratio_button_svg = tk.Radiobutton(self.frame, text="SVG", value="SVG", variable=self.ratio_svg)
        self.ratio_button_mp4 = tk.Radiobutton(self.frame, text="MP4", value="MP4", variable=self.ratio_mp4)

        self.ratio_button_jpeg.grid(row=0, column=0, sticky="news")
        self.ratio_button_png.grid(row=0, column=1, sticky="news")
        self.ratio_button_pdf.grid(row=0, column=2, sticky="news")
        self.ratio_button_svg.grid(row=0, column=3, sticky="news")
        self.ratio_button_mp4.grid(row=0, column=4, sticky="news")


        self.frame.pack(fill="x")


        self.convert_button = tk.Button(self.root, text="Convert File")
        self.convert_button.pack(pady=75)


        self.root.mainloop()