from tkinter import *
from tkinter import messagebox

win = Tk()

height = win.winfo_screenheight()
width = win.winfo_screenwidth()

win.geometry("{}x{}".format(width,height))


l1 = Label(win,text="Admin name")
l1.place(x=0 , y=0)

e1 = Entry(win,width=20)
e1.place(x=100,y=0)


def Login_check():
    name = e1.get()
    if(name == "admin"):
       
        messagebox.askyesnocancel("Login","Do you want to Login Now")
    elif(name == ""):
        messagebox.showwarning("warning","The name cant empty")
    
    
b1 = Button(win,text="Login",command=Login_check)
b1.place(x=0 , y = 100)
win.mainloop()