# Example to demonstrate various types of messagebox:

from tkinter.messagebox import *

# Showing various messages in messagebox

print(askokcancel("askokcancel Demo", "Ok or Cancel"))
print(askquestion("askquestion Demo", "Answer this Question?"))
print(askretrycancel("askretrycancel Demo", "Retry or Cancel"))
print(askyesno("askyesno Demo", "Yes or No"))
print(askyesnocancel("askyesnocancel Demo", "Yes or No or Cancel"))
print(showerror("showerror Demo", "Error Message"))
print(showinfo("showinfo Demo", "Information Message"))
print(showwarning("showwarning Demo", "Warning Message!!"))
