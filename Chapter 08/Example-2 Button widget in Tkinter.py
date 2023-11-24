# Let us consider an example to demonstrate the working of the Button widget in Tkinter:

import tkinter as tkn
from tkinter import *
from tkinter import messagebox
def func():   # display message box on button click
    messagebox.showinfo(title="Information",message="Buttonclicked")   # change button state to DISABLED
    if (btn['state'] == tkn.NORMAL):   
        btn['state'] = tkn.DISABLED
window=Tk()
btn=Button(window, text="Click Me!", command=func, fg='black', bg='white')
btn.place(x=100, y=100)
window.title('Tkinter Window')
window.geometry("300x200+10+10")
window.mainloop()
