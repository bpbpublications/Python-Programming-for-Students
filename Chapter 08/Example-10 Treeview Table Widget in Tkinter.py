# To demonstrate the working of the Treeview table widget, we have the following syntax:

import tkinter as tk
from tkinter import ttk, PhotoImage
window1 = tk.Tk()
# Specify image path for first column having folder icon
file_img_folder = r"D:/images_folder/folder1.png"
# Load and convert image to a PhotoImage object that tkinter can use
tk_img_folder = PhotoImage(file=file_img_folder)
# Define column names for reference the columns.
column_names = ("product_name_col", "price_col")
# Assign the column names when making the treeview table of products
treeview_products = ttk.Treeview(columns=column_names)
# Assign text values for headings of treeview table treeview_products
treeview_products.heading("product_name_col", text="Shape")
treeview_products.heading("price_col", text="Price")
# Insert the parent rows
treeview_products.insert(parent="", iid="electronics", index="end", image=tk_img_folder, values=("Electronics",))
treeview_products.insert(parent="", iid="mobile", index="end", image=tk_img_folder, values=("Mobile",))
treeview_products.insert(parent="", iid="laptops", index="end", image=tk_img_folder, values=("Laptops",))
# Insert sub-rows for Electronics
treeview_products.insert(parent="electronics", index="end", values=("T.V.","Rs.20K"))
treeview_products.insert(parent="electronics", index="end", values=("Refrigerator","Rs.15K"))
# Insert sub-rows for Mobile
treeview_products.insert(parent="mobile", index="end", values=("Apple", "Rs.70K"))
treeview_products.insert(parent="mobile", index="end", values=("Samsung", "Rs.20K"))
# Insert sub-rows for Laptops
treeview_products.insert(parent="laptops", index="end", values=("Dell", "Rs.30K"))
treeview_products.insert(parent="laptops", index="end", values=("HP", "Rs.35K"))
# Make the image column's width 70 pixels wide, so it looks nicer.
treeview_products.column("#0", width=70)
treeview_products.pack()
window1.mainloop()
