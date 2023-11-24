# Let us consider an example for handling these mouse and key events in Tkinter Python:

import tkinter as tk
from tkinter import *
window1 = tk.Tk()
window1.geometry("500x500")
def mouse_event(event):
     label1.config(text='Clicked at:'+str(event.x)+","+str(event.y))
label1 = tk.Label(window1, text='Label', bg='yellow', font=('Times',26,'normal'))
label1.grid(row=0,column=1,padx=10,pady=10)
button1 = Button(text="Click",height=5,width=10).place(x=100,y=100)
window1.bind('<Button-1>',mouse_event)   # Mouse Left click
window1.bind('<Button-2>',mouse_event)   # Mouse middle button click
window1.bind('<Button-3>',mouse_event)   # Mouse right button click
window1.bind('<B1-Motion>',mouse_event)# Mouse left btn pressed move
window1.bind('<ButtonRelease-1>',mouse_event) # Mouse left release 
window1.bind('<Double-Button-1>',mouse_event)    # Double click
label1.bind('<Enter>',lambda e:label1.config(text='Inside Window'))   # Mouse enters label
label1.bind('<Leave>',lambda e:label1.config(text='Outside Window'))    # Mouse leaves label
window1.bind('<MouseWheel>',mouse_event) # Mouse middle button click
window1.mainloop()
