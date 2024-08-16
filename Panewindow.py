from tkinter import *

win = Tk()

height = win.winfo_screenheight()
width = win.winfo_screenwidth()

win.geometry("{}x{}".format(width,height))
pw = PanedWindow(win,height=height,width=width,bg="black",orient=HORIZONTAL)
pw.place(x=0,y=0)

f1 = Frame(win,bg="pink",width=300)
pw.add(f1)

f2 = Frame(win,bg="green")
pw.add(f2)



main_frame = Frame(f2,height=500,width=500,bg="orange")
main_frame.pack()
l = Label(main_frame,text="This is the Add frame")
l.pack()


b1 = Button(f1,text="ADD")
b1.place(x=0,y=0)
b2 = Button(f1,text="UPDATE")
b2.place(x=0,y=50)
b3 = Button(f1,text="SHOW")
b3.place(x=0,y=100)
b4 = Button(f1,text="DELETE")
b4.place(x=0,y=150)
win.mainloop()

