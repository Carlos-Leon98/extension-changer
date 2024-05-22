import tkinter as tk
from tkinter import filedialog

def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.*"), ("All files", "*.*")])

    if file_path:
        print("Selected file:", file_path)

root = tk.Tk()

root.geometry("800x500")
root.title("Extension Changer")

label = tk.Label(root, text="Insert your file", font=('Arial', 18))
label.pack(pady=20, padx=20)

import_button = tk.Button(root, text="Import File", font=('Arial', 10), command=import_file)
import_button.pack(pady=30)

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
frame.columnconfigure(5, weight=1)


ratio_button_jpeg = tk.Radiobutton(frame, text="JPEG", value="JPEG")
ratio_button_png = tk.Radiobutton(frame, text="PNG", value="PNG")
ratio_button_gif = tk.Radiobutton(frame, text="GIF", value="GIF")
ratio_button_pdf = tk.Radiobutton(frame, text="PDF", value="PDF")
ratio_button_svg = tk.Radiobutton(frame, text="SVG", value="SVG")
ratio_button_mp4 = tk.Radiobutton(frame, text="MP4", value="MP4")

ratio_button_jpeg.grid(row=0, column=0, sticky="news")
ratio_button_png.grid(row=0, column=1, sticky="news")
ratio_button_gif.grid(row=0, column=2, sticky="news")
ratio_button_pdf.grid(row=0, column=3, sticky="news")
ratio_button_svg.grid(row=0, column=4, sticky="news")
ratio_button_mp4.grid(row=0, column=5, sticky="news")


frame.pack(fill="x")





root.mainloop()