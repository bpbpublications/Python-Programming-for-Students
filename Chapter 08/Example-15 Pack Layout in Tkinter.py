# Pack Layout in Tkinter

import tkinter as tk
window1 = tk.Tk()
window1.title('Pack Demo')
window1.geometry("300x200")
# First place widgets top down vertically
label1 = tk.Label(window1, text='Top Block', bg="red")
label1.pack(ipadx= 10, ipady= 10, fill=tk.X)
label2 = tk.Label(window1, text='Center Block', bg="yellow")
label2.pack(ipadx= 10, ipady= 10, fill=tk.X)
label3 = tk.Label(window1, text='Lower Block', bg="cyan")
label3.pack(ipadx= 10, ipady= 10, fill=tk.X)
# Next place widgets side by side horizontally
label4 = tk.Label(window1, text='Left Block', bg="green")
label4.pack(ipadx=10,ipady=10,expand=True,fill=tk.BOTH,side=tk.LEFT)
label5 = tk.Label(window1, text='Center Block', bg="blue",)
label5.pack(ipadx=10,ipady=10,expand=True,fill=tk.BOTH,side=tk.LEFT)
label6 = tk.Label(window1, text='Right Block', bg="orange")
label6.pack(ipadx=10,ipady=10,expand=True,fill=tk.BOTH,side=tk.LEFT)
window1.mainloop()
