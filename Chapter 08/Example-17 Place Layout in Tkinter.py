# Let us consider an example for place() geometry manager:

from tkinter import *
window1 = Tk()
window1.geometry("300x300")
usernameLabel = Label(window1, text = "Username")
usernameLabel.place(x = 50,y = 50)
emailLabel = Label(window1, text = "Email").place(x = 50, y = 100)
passwordLabel = Label(window1, text = "Password").place(x = 50, y = 150)
textbox1 = Entry(window1).place(x = 130, y = 50)
textbox2 = Entry(window1).place(x = 130, y = 100)
textbox3 = Entry(window1).place(x = 130, y = 150)
button1 = Button(window1, text="Submit").place(x=100, y=210)
window1.mainloop()
