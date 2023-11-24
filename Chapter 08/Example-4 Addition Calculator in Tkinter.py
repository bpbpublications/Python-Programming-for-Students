# Let  us  consider  an  example  to  create  a  calculator  that  takes  user  input  and  produces  results  after  doing  specified  calculation:.

from  tkinter  import  *
#  Syntax  to  create  a  Window
window1  =  Tk()
window1.title('Entry  Widget  Demo')  #  To  give  the  title  of  the  window
window1.geometry("500x500")  #  To  initialize  the  size  of  the  window.
n1  =  IntVar()  #  initialize  the  first  Integer  variable
n2  =  IntVar()  #  initialize  the  second  Integer  variable
#  Label  Heading
heading1=Label(window1,text="Addition  Calculator",font=("Arial",25))
heading1.place(x=100,  y=50)  #  Used  to  place  label  at  a  position
#  Labels  for  Inputs
num1  =  Label(window1,text="Enter  first  number:  ",font=("Arial",  10))
num1.place(x=80,  y=100)
num2  =  Label(window1,text="Enter  second  number:  ",font=("Arial",10))
num2.place(x=80,  y=150)
outputLabel  =  Label(window1,  text="Output:",  font=("Arial",  10))
outputLabel.place(x=150,  y=300)
#  Use  functions  to  give  action  to  the  button.
def  addCalc():
        sum  =  n1.get()  +  n2.get()
        addEntry.delete(0,  END)
        addEntry.insert(0,  str(sum))
#  Entries  text  boxes  Syntax
inputentry1  =  Entry(window1,  textvariable=n1)
inputentry1.place(x=230,  y=100,  height=25,  width=143)
inputentry2  =  Entry(window1,  textvariable=n2)
inputentry2.place(x=230,  y=150,  height=25,  width=143)
#  Result  text  entry
addEntry  =  Entry(window1)
addEntry.place(x=230,  y=300,  height=25,  width=143)
#  Use  command  to  call  the  functions  in  Add  button.
buttonAdd  =  Button(window1,  text="ADD  (+)",  fg="black",  bg="cyan",  font=("Arial",  15),  command=addCalc)
buttonAdd.place(x=210,  y=200,  height=50,  width=100)
window1.mainloop()
