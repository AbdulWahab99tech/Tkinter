from tkinter import *
root=Tk()
def click_button():
    label=Label(root,text="you clicked the button")
    label.pack()

button=Button(root,text="Button 1",command=click_button)
button.pack()


root.mainloop()