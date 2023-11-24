# Sample project with solution
# Create a GUI application for a Café to order coffee for users. 
# This application uses the tkinter library along with sqlite3 for database management. 
# The application works for managing customer orders and taking their feedback for further improvements in quality. 
# The total payment to be done is calculated and filled in Entry widgets automatically on button click. 
# The user can also view the menu card with a button click. The orders are constantly visible in a tabular format on the screen:

from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *

def system():
    root = Tk()
    root.geometry("1100x500")
    root.title("Cafe Coffee Heights Order")

    def Database():
        global connectn, cursor
        connectn = sqlite3.connect("Cafe.db")
        cursor = connectn.cursor()
        # creating bill table
        cursor.execute("CREATE TABLE IF NOT EXISTS OrderRecords(ordno text,fil_cof text,cafe_lat text,cafe_moc text, cold_cof text, ct text, taxes text, tot text)")
    # variable datatype assignment
    ordernum = StringVar()
    filter_coffee = StringVar()
    cafe_latte= StringVar()
    cafe_mocha = StringVar()
    cold_coffee = StringVar()
    cost = StringVar()
    tax = StringVar()
    total = StringVar()

    # defining total function
    def tottal():
        # fetching the values from entry box
        order = (ordernum.get())
        fc = float(filter_coffee.get())
        cl = float(cafe_latte.get())
        cm = float(cafe_mocha.get())
        cc = float(cold_coffee.get())

        # computing the cost of items

        costfc = fc * 40
        costcl = cl * 110
        costcm = cm * 150
        costcc = cc * 180
     # computing the charges
        costofmeal = (costfc+costcl+costcm+costcc)
        ptax = ((costfc+costcl+costcm+costcc) * 0.20)
        paidtax = str(ptax)
        overall = str(ptax + costofmeal)
    # Displaying the values
        cost.set(costofmeal)
        total.set(overall)
        tax.set(paidtax)
    # defining reset function
    def reset():
        ordernum.set("")
        filter_coffee.set("")
        cafe_latte.set("")
        cafe_mocha.set("")
        cold_coffee.set("")
        cost.set("")
        tax.set("")
        total.set("")
    # defining exit function
    def exit():
        root.destroy()
    # Topframe
    topframe = Frame(root, bg="white", width=1600, height=50)
    topframe.pack(side=TOP)
    # Leftframe
    leftframe = Frame(root, width=1000, height=900)
    leftframe.pack(side=LEFT)
    # rightframe
    rightframe = Frame(root, width=1000, height=900)
    rightframe.pack(side=RIGHT)
# Display data
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM OrderRecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    # Create table 
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("orderNo", "filter coffee", "cafe latte", "cafe mocha", "cold coffee", "Price", "Tax", "Total")

    # create scrollbars for table 
    horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)
    vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    # defining column for table
   my_tree.column("#0", width=0, minwidth=0)
   my_tree.column("orderNo", anchor=CENTER,width=80,minwidth=25)
   my_tree.column("filtercoffee",anchor=CENTER,width=80,minwidth=25)
   my_tree.column("cafe latte", anchor=CENTER, width=80,minwidth=25)
   my_tree.column("cafe mocha",anchor=CENTER, width=80, minwidth=25)
my_tree.column("cold coffee",anchor=CENTER, width=80, minwidth=25)
my_tree.column("Price", anchor=CENTER, width=80, minwidth=25)
my_tree.column("Tax", anchor=CENTER, width=80, minwidth=25)
my_tree.column("Total", anchor=CENTER, width=80, minwidth=25)

    # defining  headings for table
my_tree.heading("orderNo", text="Order No", anchor=CENTER)
my_tree.heading("filtercoffee",text="Filter Coffee",anchor=CENTER)
my_tree.heading("cafe latte", text="Cafe Latte",anchor=CENTER)
my_tree.heading("cafe mocha", text="Cafe Mocha",anchor=CENTER)
my_tree.heading("cold coffee",text="Cold Coffee",anchor=CENTER)
my_tree.heading("Price", text="Cost", anchor=CENTER)
my_tree.heading("Tax", text="Tax", anchor=CENTER)
my_tree.heading("Total", text="Total", anchor=CENTER)
my_tree.pack()
DisplayData()
    # defining add function to add record
def add():
        Database()
      # getting  data
        orders = ordernum.get()
        fc1 = filter_coffee.get()
        cl1 = cafe_latte.get()
        cm1 = cafe_mocha.get()
        cc1 = cold_coffee.get()
        costs = cost.get()
        taxes = tax.get()
        totals = total.get()
        if orders == "" or fc1 == "" or cl1 == "" or cm1 == "" or cc1 == "" or costs == "" or taxes == "" or totals == "":
           messagebox.showinfo("Error!!","Fill all fields!!!")
           print(orders,fc1,cl1,cm1,cc1,costs,taxes,totals)
        else:
           connectn.execute('INSERT INTO OrderRecords VALUES (?,?,?,?,?,?,?,?)',(orders, fc1,cl1,cm1,cc1,costs,taxes,totals));
           connectn.commit()
           messagebox.showinfo("Message","Stored Data")
# refresh table data
        DisplayData()
        connectn.close()
# defining function to access data from sqlite database
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor=connectn.execute("SELECT * FROM OrderRecords")
        fetch=cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()
# defining function to delete record
    def Delete():
# open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Error!!","No Data selected to Delete!!")
        else:
            result = messagebox.askquestion('Confirmation','Confirm to delete the record?',icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor = connectn.execute("DELETE FROM OrderRecords WHERE ordno= %d" % selecteditem[0])
            connectn.commit()
            cursor.close()
            connectn.close()
# Top heading
    main_lbl = Label(topframe, font=('Calibri', 30, 'bold'), text="**** Cafe Coffee Heights Order System ****", fg="navy blue", anchor=W)
    main_lbl.grid(row=0, column=0)
    labelframe=LabelFrame(leftframe,text="Fill Order Details")
    labelframe.grid(column=50, row=50)
    ordlbl = Label(labelframe, text="Order No.", fg="black", bd=5, anchor=W).grid(row=1,column=0)
    ordtxt = Entry(labelframe, insertwidth=4, justify='left', bd=5,text=num, textvariable=ordernum).grid(row=1, column=1)
    filtercoffeelbl = Label(labelframe, text="Filter Coffee", bd=5,fg="black", anchor=W).grid(row=3,column=0)
    filtercoffeetxt = Entry(labelframe, insertwidth=4, bd=5,justify='left', textvariable=filter_coffee).grid(row=3, column=1)
    cafelattelbl = Label(labelframe, text="Cafe Latte", bd=5,fg="black", anchor=W).grid(row=4,column=0)
    cafelattetxt = Entry(labelframe, insertwidth=4, bd=5,justify='left',textvariable=cafe_latte).grid(row=4, column=1)
    cafemochalbl = Label(labelframe, text="Cafe Mocha",bd=5, fg="black", anchor=W).grid(row=5,column=0)
    cafemochatxt = Entry(labelframe, insertwidth=4, bd=5,justify='left', textvariable=cafe_mocha).grid(row=5, column=1)
    coldcoffeelbl = Label(labelframe, text="Cold Coffee", bd=5,fg="black", anchor=W).grid(row=6,column=0)
    coldcoffeetxt = Entry(labelframe, insertwidth=4,bd=5, justify='left',textvariable=cold_coffee).grid(row=6, column=1)
    costlbl = Label(labelframe, text="Cost", bd=5, anchor=W).grid(row=7, column=0)
    costtxt = Entry(labelframe, bd=5,justify='left',textvariable=cost).grid(row=7, column=1)
    taxlbl = Label(labelframe, text="Tax", bd=5,anchor=W).grid(row=9, column=0)
    taxtxt = Entry(labelframe, bd=5,justify='left',textvariable=tax).grid(row=9, column=1)
    totallbl = Label(labelframe, text="Total", bd=5,anchor=W).grid(row=11,column=0)
    totaltxt = Entry(labelframe, bd=5,justify='left',textvariable=total).grid(row=11, column=1)
    totbtn = Button(labelframe,text="Calculate",bd=10,bg="Lightgrey",command=tottal, width=15).grid(row=23, column=0)
    resetbtn = Button(labelframe,text="Reset",bd=10,bg="lightgrey",command=reset, width=15).grid(row=23,column=2)
    exitbtn = Button(labelframe,text="Exit", bd=10,bg="lightgrey",command=exit, width=15).grid(row=24, column=0)
    addbtn = Button(labelframe, text="Add Order",bd=10,bg="lightgrey",command=add, width=15).grid(row=24, column=2)
    deletebtn = Button(labelframe,text="Delete Record", bd=10,bg="lightgrey",command=Delete, width=15).grid(row=25, column=1)
# feedback form
    def feedbackk():
        feed = Tk()
        feed.geometry("600x500")
        feed.title("Submit Feedback form")
        connectn = sqlite3.connect("Cafe.db")
        cursor = connectn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS CustomerFeedback(n text,eid text,feedback5 text,com text)")
        name = StringVar()
        email = StringVar()
        comments = StringVar()
 # defining submit function
        def submit():
            n = name.get()
            eid = email.get()
            com = txt.get('1.0', END)
            feedback1 = ""
            feedback2 = ""
            feedback3 = ""
            feedback4 = ""
            if (checkvar1.get() == "1"):
                feedback1 = "Excellent"
            if (checkvar2.get() == "1"):
                feedback2 = "Good"
            if (checkvar3.get() == "1"):
                feedback2 = "Average"
            if (checkvar4.get() == "1"):
                feedback2 = "Poor"
            feedback5=feedback1+" "+feedback2+" "+feedback3+" " + feedback4
            conn = sqlite3.connect("Cafe.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO CustomerFeedback VALUES ('" + n + "','" + eid + "','" + com + "','" + feedback5 + "')")
            messagebox.showinfo("Information", "Your Feedback Saved Successfully!")
            feed.destroy()
# defining cancel button
        def cancel():
            feed.destroy()
# label#
        lb1 = Label(feed, font=("vardana", 15, "bold"), text="We appreciate your feedback!", fg="red").pack(side=TOP)
        lbl2 = Label(feed, font=("vardana", 15), text="Spare some time to fill the form",fg="navy blue").pack(side=TOP)
        Cnamelbl = Label(feed, font=('vardana', 15), text="Customer Name:", fg="black", bd=10, anchor=W).place(x=10, y=150)
        Cnametxt=Entry(feed,font=('vardana',15),bd=6,insertwidth=2,bg="white",justify='left',textvariable=name).place(x=15, y=185)
        Cemaillbl = Label(feed, font=('vardana', 15), text="Contact No:", fg="black", bd=10, anchor=W).place(x=280, y=150)
        Cemailtxt=Entry(feed,font=('vardana',15),bd=6,bg="white",justify='left',textvariable=email).place(x=285,y=185)
        Cratelbl = Label(feed, font=('vardana', 15), text="How was your coffee?", fg="black", bd=10, anchor=W).place(x=10, y=220)
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        c1 = Checkbutton(feed, font=('Calibri', 15, "bold"), text="Awesome", variable=checkvar1)
        c1.deselect()
        c1.place(x=15, y=265)
        c2 = Checkbutton(feed, font=('Calibri', 15, "bold"), text="Good",variable=checkvar2, )
        c2.deselect()
        c2.place(x=150, y=265)
        c3 = Checkbutton(feed, font=('Calibri', 15, "bold"), text="Average",  variable=checkvar3, )
        c3.deselect()
        c3.place(x=250, y=265)
        c4 = Checkbutton(feed, font=('Calibri', 15, "bold"), text="Needs Improvement", variable=checkvar4, )
        c4.deselect()
        c4.place(x=370, y=265)
# Add special comments"
        commentslbl = Label(feed, font=('Calibri', 15), text="Special Comments", fg="black", bd=10, anchor=W).place(x=10, y=300)
        txt = Text(feed, width=50, height=5)
        txt.place(x=15, y=335)
        # button
        submit = Button(feed, font=("Calibri", 15), text="Submit", fg="black", bd=2, command=submit).place(
            x=145, y=430)
        cancel = Button(feed, font=("Calibri", 15), text="Cancel", fg="black", bd=2, command=cancel).place(
            x=245, y=430)
        feed.mainloop()
# Feedbackbutton
    feedbtn = Button(labelframe, text="Feedback Form",fg="black", bg="lightgrey",command=feedbackk, bd=10, width=15).grid(row=23,column=1)
# Menu card
    def menu():
        roott = Tk()
        roott.title("Cafe Price Menu")
        roott.geometry("300x300")
        lbliinfo = Label(roott, font=("Calibri", 20, "bold"), text="Favourites", fg="red", bd=10)
        lbliinfo.grid(row=0, column=0)
        lblcprice = Label(roott, font=("Calibri", 20, "bold"), text="Prices", fg="blue", bd=10)
        lblcprice.grid(row=0, column=3)
        lblfc = Label(roott, font=("Calibri", 20, "bold"), text="Filter Coffee", fg="black", bd=10)
        lblfc.grid(row=1, column=0)
        lblfcp = Label(roott, font=("Calibri", 20, "bold"), text="40/-", fg="black", bd=10)
        lblfcp.grid(row=1, column=3)
        lblcl = Label(roott, font=("Calibri", 20, "bold"), text="Cafe Latte", fg="black", bd=10)
        lblcl.grid(row=3, column=0)
        lblclp = Label(roott, font=("Calibri", 20, "bold"), text="110/-", fg="black", bd=10)
        lblclp.grid(row=3, column=3)
        lblcm = Label(roott, font=("Calibri", 20, "bold"), text="Cafe Mocha", fg="black", bd=10)
        lblcm.grid(row=4, column=0)
        lblcmp = Label(roott, font=("Calibri", 20, "bold"), text="150/-", fg="black", bd=10)
        lblcmp.grid(row=4, column=3)
        lblcc = Label(roott, font=("Calibri", 20, "bold"), text="Cold Coffee", fg="black", bd=10)
        lblcc.grid(row=5, column=0)
        lblccp = Label(roott, font=("Calibri", 20, "bold"), text="180/-", fg="black", bd=10)
        lblccp.grid(row=5, column=3)
        roott.mainloop()
# menubutton
    menubtn = Button(labelframe, text="Coffee Menu", bg="lightgrey", command=menu, width=15, bd=10).grid(row=24, column=1)
    root.mainloop()
system()
