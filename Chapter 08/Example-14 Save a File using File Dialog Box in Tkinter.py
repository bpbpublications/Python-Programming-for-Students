# To save a file at a particular place, use the asksaveasfile() function, we have the following syntax:

import tkinter as tk
from tkinter import filedialog
filepath = filedialog.asksaveasfile(initialdir="/", title="Select to Save file",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
print(filepath.read())
