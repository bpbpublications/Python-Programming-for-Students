# Let us see an example using text widget to get user input and display the same on screen:

from tkinter import *
window1=Tk()
# Method to fetch user input from text widget and display on screen.
def retrieve_userinput():
    inputVal=textBox1.get("1.0","end-1c")
    print(inputVal)
# Define text widget and button
textBox1=Text(window1, height=5, width=20)
button1=Button(window1, height=1, width=10, text="Display", command=retrieve_userinput)
# Add and arrange widgets on window
textBox1.pack()
button1.pack()
window1.mainloop()
