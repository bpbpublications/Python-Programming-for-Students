# Let us consider an example to highlight the working of label widget:

from tkinter import *
window1 = Tk()
# Create a control variable named cvar and set its value
cvar = StringVar()
cvar.set("This is a label widget text!!")
# Assign value of cvar to textvariable property of label
label1 = Label(window1, textvariable=cvar, relief=RIDGE)
# pack() is a geometry manager that adds and arranges widgets to a window
label1.pack()
window1.title('Tkinter Window')
window1.geometry("200x100+10+10")
window1.mainloop()
