import tkinter as tk
from tkinter import filedialog
filepath = filedialog.askopenfilename(initialdir="/", title="Select a file to open",filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
