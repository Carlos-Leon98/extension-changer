import tkinter as tk
from tkinter import Scrollbar
from tkinter import filedialog
from pathlib import Path

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("Extension Changer")

        self.scrollbar = Scrollbar(self.root, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.label = tk.Label(self.root, text="Insert your file", font=('Arial', 18))
        self.label.pack(pady=20, padx=20)

        self.file_path = tk.StringVar()

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

        self.convert_button = tk.Button(self.root, text="Convert File", command=self.convert_file)
        self.convert_button.pack(pady=75)

        self.test_button = tk.Button(self.root, text="Test", command=self.print_message)
        self.test_button.pack(pady=80)


        self.root.mainloop()

    def print_message(self):
        print("Message")
        print(self.file_to_convert.get())
        print(self.file_path.get())

    def import_file(self):
        try:
            file_name = filedialog.askopenfilename()

            self.file_path.set(file_name)
            print(f"The value of file_path is: {file_name}")

        except Exception as e:
            print("Error getting the file path:", e)           

    def convert_file(self):
        try:
            path = Path(self.file_path.get())
            new_file = path.with_suffix('.' + self.file_to_convert.get())
            path.rename(new_file)
        except Exception as e:
            print(f"Error converting the file to .{self.file_to_convert.get()}:", e)