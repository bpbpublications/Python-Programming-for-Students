# Let us demonstrate the working of grid() layout with an example:

import tkinter as tk
window1 = tk.Tk()
for i in range(3):
    for j in range(3):
        frame = tk.Frame(window1, borderwidth=1, relief='sunken')
        frame.grid(row=i, column=j, padx=2, pady=2)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
window1.mainloop()
