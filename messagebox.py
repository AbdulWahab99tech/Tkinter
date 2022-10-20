from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root=Tk()
root.title("Easy to Learn Tkinter")
root.iconbitmap("icon_img.ico")
def popup():
    messagebox.showinfo("This is popup", "Invalid Information")


b=Button(root, text="click", command=popup)
b.pack()

root.mainloop()