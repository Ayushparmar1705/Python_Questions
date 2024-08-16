from tkinter import *

win = Tk()

height = win.winfo_screenheight()
width = win.winfo_screenwidth()

win.geometry("{}x{}".format(width,height))
menubar = Menu(win)



filem = Menu(menubar)




menubar.add_cascade(label="File",menu=filem)
menubar.add_cascade(label="Edit")
menubar.add_cascade(label="Help")

def Newfile():
    newwin = Toplevel()
filem.add_cascade(label="New",command=Newfile)
filem.add_cascade(label="Save")



filem.add_cascade(label="SaveAs")
filem.add_separator()
filem.add_cascade(label="Exit")
win.config(menu=menubar)
win.mainloop()