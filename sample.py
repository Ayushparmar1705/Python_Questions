from tkinter import *

from tkinter import PhotoImage
win = Tk()
image = PhotoImage(file="Phone1.png")

f1 = Frame(win,width=1000,height=500)
f1.place(x=100,y=100)
label = Label(f1,image=image)
label.place(x=0,y=0)



text = Label(f1,text="Iphone's with high usesablity")
text.place(x=600,y=0)


b1 = Button()
win.mainloop()