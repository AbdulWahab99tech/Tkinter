#install pillow library using following command
#pip install pillow
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Easy to Learn Tkinter")
root.iconbitmap("icon_img.ico")
img=ImageTk.PhotoImage(Image.open("cat.jpg"))
label=Label(image=img)
label.pack()
root.mainloop()