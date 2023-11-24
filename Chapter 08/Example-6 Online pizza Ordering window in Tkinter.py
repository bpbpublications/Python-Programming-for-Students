# In  this  example,  we  try  to  create  a  sample  window  for  the Pizza  online  order  system:
	
import  tkinter
from  tkinter  import  *
from  tkinter  import  messagebox
from  tkinter.ttk  import  *

#  A  sample  window  for  Online  pizza  Ordering

window1  =  Tk()
var1  =  StringVar()
var1.set("one")
label0  =  Label(text="Pizza  Order  Online")
label0.place(x=80,  y=100)
v0  =  IntVar()
v0.set(1)

#  Add  Radio  buttons

r1  =  Radiobutton(window1,  text="Dine-in",  variable=v0,  value=1)
r2  =  Radiobutton(window1,  text="Delivery",  variable=v0,  value=2)
r1.place(x=150,  y=50)
r2.place(x=250,  y=50)

#  Add  ComboBox  to  select  only  one  option

label1  =  Label(text="Choose  your  outlet  :")
label1.place(x=80,  y=100)
data1  =  ("North  Region",  "East  Region",  "West  Zone",  "South  Extension",  "Country  Side")
cbox  =  tkinter.ttk.Combobox(window1,  values=data1)
cbox.place(x=220,  y=100)

#  Add  listbox  to  select  multiple  options

label2  =  Label(text="Choose  your  Pizza  :")
label2.place(x=80,  y=150)
lbox  =  Listbox(window1,  height=10,  selectmode='multiple')
data2  =  ("Veg-Delight",  "Farmhouse",  "Indo-Italian",  "Margherita",  "Cheese  &  Corn",  "Pasta-Pizza")
for  values  in  data2:
        lbox.insert(END,  values)
lbox.place(x=220,  y=150)

#  Add  checkbuttons  to  check  multiple  values

label3  =  Label(text="Choose  your  Add-Ons  :")
label3.place(x=80,  y=350)
v1  =  IntVar()
v2  =  IntVar()
v3  =  IntVar()
C1  =  Checkbutton(window1,  text="Cheese",  variable=v1)
C2  =  Checkbutton(window1,  text="Jalapeno",  variable=v2)
C3  =  Checkbutton(window1,  text="Olive",  variable=v3)
C1.place(x=220,  y=350)
C2.place(x=290,  y=350)
C3.place(x=370,  y=350)

#  Add  button  and  message  box
def  func():      #  display  message  box  on  button  click
        messagebox.showinfo(title="Order  Confirmation",message="Thank  you!!  \n  Your  Order  will  be  ready  soon!!.")

btn=Button(window1,  text="Place  Order!",  command=func)
btn.place(x=200,  y=400)
window1.title('Selection  Widgets')
window1.geometry("400x300+10+10")
window1.mainloop()
