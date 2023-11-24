# To demonstrate the working of the hierarchical Treeview widget, we have the following syntax:

import tkinter as t
from tkinter import ttk
# Creating a top level window
window1 = t.Tk()
window1.title('Treeview widget Demo')
window1.geometry('500x200')
ttk.Label(window1, text="Demo Hierarchical Treeview").pack()
# Creating treeview window
treehierarchy = ttk.Treeview(window1)
# Inserting Parent Node
treehierarchy.insert('','0','item1', text='Programming Language')
# Inserting child nodes (Sub-files) under parent node
treehierarchy.insert('', '1', 'item2', text='Python')
treehierarchy.insert('', '2', 'item3', text='Java')
treehierarchy.insert('', '3', 'item4', text='C++')
# Inserting more than one attribute of an item
treehierarchy.insert('item2', 'end', 'List', text='List')
treehierarchy.insert('item2', 'end', 'Tuple', text='Tuple')
treehierarchy.insert('item2','end','Dictionary',text='Dictionary')
treehierarchy.insert('item3', 'end', 'J2SE', text='J2SE')
treehierarchy.insert('item3', 'end', 'J2EE', text='J2EE')
treehierarchy.insert('item4', 'end', 'Class', text='Class')
treehierarchy.insert('item4', 'end', 'Object', text='Object')

# Placing each child items in parent widget
treehierarchy.move('item2', 'item1', 'end')
treehierarchy.move('item3', 'item1', 'end')
treehierarchy.move('item4', 'item1', 'end')
# Calling pack method on the treeview
treehierarchy.pack()
window1.mainloop()
