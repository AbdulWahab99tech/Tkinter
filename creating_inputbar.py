from tkinter import *
root=Tk()
input=Entry(root,width=50)
input.pack()
input.insert(0,"Enter your name here")
def click():
    name="My name is "+input.get()
    label=Label(root,text=name)
    label.pack()


button = Button(root,text="Get Your Name" +" ",command=click)
button.pack()

root.mainloop()

