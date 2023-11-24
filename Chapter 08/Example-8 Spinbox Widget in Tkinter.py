
# Let  us  consider  the  following  example  to  demonstrate  the  working  of  a  Spinboxspinbox:

from  tkinter  import  *
#  Use  widget  config  method  to  update  widget  settings  such  as  text    
def  show_selected():
        lb2.config(text=f'You  selected  {var.get()}',  bg='yellow')

window1  =  Tk()
window1.geometry("200x200")
lb1=  Label(window1,  text="Select  your  age:  ")
var  =  StringVar()
spin  =  Spinbox(window1,  from_=1,  to=100,  textvariable=var, command=show_selected)
lb2=  Label(window1,  text="")
lb1.pack()
spin.pack()
lb2.pack()
window1.mainloop()
