# Let  us  consider  an  example  to  create  top-level  menus  along  with  submenus:

from  tkinter  import  Tk,  Menu,  messagebox
	
#  root  window

window1  =  Tk()
window1.geometry('400x400')
window1.title('Menu  Widget  Demo')

#  create  a  top  level  menubar

menubar  =  Menu(window1)
window1.config(menu=menubar)

#  create  the  File  Menu  option

file_menu1  =  Menu(menubar,  tearoff=0)

#  add  menu  items  to  the  File  menu

file_menu1.add_command(label='New  File')
file_menu1.add_command(label='Open  File')
file_menu1.add_command(label='Close')
file_menu1.add_separator()

#  add  a  submenu  to  File  Menu

sub_menu  =  Menu(file_menu1,  tearoff=0)
sub_menu.add_command(label='Keyboard  Shortcuts')
sub_menu.add_command(label='Color  Themes')

#  add  the  File  menu  to  the  menubar

file_menu1.add_cascade(label="Preferences",  menu=sub_menu)

#  add  a  separator  and  add  Exit  menu  item

file_menu1.add_separator()
file_menu1.add_command(label='Exit',  command=window1.destroy)
menubar.add_cascade(label="File",  menu=file_menu1,  underline=0)

#  Adding  Group  By  Menu

search  =  Menu(menubar,  tearoff  =  0)
menubar.add_cascade(label  ='Search',  menu  =  search)

#  Adding  Checkbuttons  to  Search  Menu

search.add_checkbutton(label="By  Name")
search.add_checkbutton(label="By  Date  Modified")
search.add_checkbutton(label="By  Type")
search.add_checkbutton(label="By  Size")
def  about():
        messagebox.showinfo('About  Editor',  'Sample  Text  Editor  displaying  Menu  widget!!')

#  create  the  Help  menu

help_menu1  =  Menu(menubar,  tearoff=0)
help_menu1.add_command(label='About  Editor',  command=about)

#  add  the  Help  menu  to  the  menubar

menubar.add_cascade(label="Help",  menu=help_menu1,underline=0)
window1.mainloop()
