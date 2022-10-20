from tkinter import *
root=Tk()
label1=Label(root, text="First Label")
label2=Label(root, text="2nd Label")
label3=Label(root, text="3nd Label")
label1.grid(row=0,column=1)
label2.grid(row=1,column=2)
label3.grid(row=2,column=4)

root.mainloop()