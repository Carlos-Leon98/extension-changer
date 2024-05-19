import tkinter as tk
from tkinter import filedialog

def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_path:
        print("Selected file:", file_path)

root = tk.Tk()
root.title("Extension changer")

import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack(pady=100)

root.mainloop()