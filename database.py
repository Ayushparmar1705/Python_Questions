from tkinter import *
import mysql.connector as mysql

win = Tk()



conn = mysql.connect(host="localhost",user="root",password = "Ayush#2004",db="sample")


l1 = Label(win,text="Enter name")
l1.place(x=0,y=0)
e1 = Entry(win,width=20)
e1.place(x=100,y=0)


l2 = Label(win,text="Enter email")
l2.place(x=0,y=50)
e2 = Entry(win,width=20)
e2.place(x=100,y=50)



def add():
    cursor = conn.cursor()

    id = "insert into sample(name,email) values('"+e1.get()+"' , '"+e2.get()+"')"

    cursor.execute(id)


    conn.commit()
    print("inserted...")
b1 = Button(win,text="add",command=add)
b1.place(x=0,y=100)
win.mainloop()