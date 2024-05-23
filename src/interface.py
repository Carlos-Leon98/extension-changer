import tkinter as tk
from tkinter import filedialog
from pathlib import Path

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("Extension Changer")

        self.label = tk.Label(self.root, text="Insert your file", font=('Arial', 18))
        self.label.pack(pady=20, padx=20)

        self.import_button = tk.Button(self.root, text="Import File", font=('Arial', 10), command=self.import_file)
        self.import_button.pack(pady=30)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)

        self.file_to_convert = tk.StringVar()

        self.ratio_button_jpeg = tk.Radiobutton(self.frame, text="JPEG", value="jpeg", variable=self.file_to_convert)
        self.ratio_button_png = tk.Radiobutton(self.frame, text="PNG", value="png", variable=self.file_to_convert)
        self.ratio_button_pdf = tk.Radiobutton(self.frame, text="PDF", value="pdf", variable=self.file_to_convert)
        self.ratio_button_svg = tk.Radiobutton(self.frame, text="SVG", value="svg", variable=self.file_to_convert)
        self.ratio_button_mp4 = tk.Radiobutton(self.frame, text="MP4", value="mp4", variable=self.file_to_convert)

        self.ratio_button_jpeg.grid(row=0, column=0, sticky="news")
        self.ratio_button_png.grid(row=0, column=1, sticky="news")
        self.ratio_button_pdf.grid(row=0, column=2, sticky="news")
        self.ratio_button_svg.grid(row=0, column=3, sticky="news")
        self.ratio_button_mp4.grid(row=0, column=4, sticky="news")


        self.frame.pack(fill="x")


        self.convert_button = tk.Button(self.root, text="Convert File", command=self.print_message)
        self.convert_button.pack(pady=75)


        self.root.mainloop()

    def print_message(self):
        print("Message")
        print(self.file_to_convert.get())

    def import_file(self):
        file_name = filedialog.askopenfile()
        print(f"Selected: ${file_name}")

    def convert_file(self, file_path, file_type):
        path = Path(file_path)
        new_file = path.with_suffix('.' + file_type)
        return new_file