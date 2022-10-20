from tkinter import *
root=Tk()
def click_button():
    label=Label(root,text="you clicked the button",bg="red",padx=50,pady=50)
    label.pack()

button=Button(root,text="Button 1",padx=50,pady=50,bg="blue",fg="black",command=click_button)
button.pack()


root.mainloop()