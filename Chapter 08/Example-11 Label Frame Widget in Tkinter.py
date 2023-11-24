
# Let us demonstrate Labelframe with an example:

import tkinter as tk
from tkinter import *
window1 = tk.Tk()
lf1 = LabelFrame(window1, text="Mark Gender")
lf1.pack()
val = IntVar()
Radiobutton(lf1, text="Male", variable=val, value=1).pack()
Radiobutton(lf1, text="Female", variable=val, value=2).pack()
lf2 = LabelFrame(window1, text="Choose Hobbies")
lf2.pack()
Checkbutton(lf2, text="Reading").pack()
Checkbutton(lf2, text="Cooking").pack()
Checkbutton(lf2, text="Swimming").pack()
window1.mainloop()
