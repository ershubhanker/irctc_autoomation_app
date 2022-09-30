from tkinter import *
import tkinter as tk
from turtle import heading, width 
from PIL import Image, ImageTk
from tkinter.messagebox import askyesno
from tkinter import font  as tkfont

#----window----
root = tk.Tk()
root.configure(bg='sky blue')
root.title("Register Here")
root.geometry("900x600+200+50")
#root.resizable(False,False)

#font
font1=tkfont.Font(family='Times', size=15, weight="bold")

#frames
f1=Frame(root ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=1)
f1.place(x=10,y=20,width=880,height=200)

f2=Frame(root)
f2.place(x=165,y=220,width=580,height=370)

#labels
label1=Label(root,text='IRCTC ID',bg='sky blue',font=font1)
label1.place(x=17, y=17)
label2=Label(f1,text='Irstc ID :',bg='sky blue',font=("Times",12,"bold")).place(x=100, y=10)
label3=Label(f1,text='Password :',bg='sky blue',font=("Times",12,"bold")).place(x=400, y=10)

#entry
username = StringVar()
e1=Entry(f1,font=("Times",12,"bold"),textvariable=username).place(x=180, y=10,width=200,height=30)
password = StringVar()
e2=Entry(f1,font=("Times",12,"bold"),textvariable=password).place(x=490, y=10,width=200,height=30)

#save button
save = Button(root, text = 'Save',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : askyesno('Confirm', 'Do you want to save?'))
save.pack(side = TOP , pady = 120 ,ipadx=60,ipady=5)


#frame 2 data show

e1=Label(f2,width=30,text='Username',borderwidth=2,font=("Times",10,"bold"), relief='ridge',anchor='s',bg='yellow')
e1.grid(row=0,column=0)
e2=Label(f2,width=30,text='Password',borderwidth=2,font=("Times",10,"bold"), relief='ridge',anchor='s',bg='yellow')
e2.grid(row=0,column=1)
b1=Label(f2,width=19,text='Login',borderwidth=2,font=("Times",10,"bold"), relief='ridge',anchor='s',bg='yellow')
b1.grid(row=0,column=2)

import mysql.connector
connection=mysql.connector.connect(host='localhost',username='root',password='deol9646',database="train_login")

print('successfully connected')
####### end of connection ####
my_cursor = connection.cursor()

my_conn = connection.cursor()
my_conn.execute("SELECT * FROM login limit 0,10")
i=1 
for student in my_conn: 
    for j in range(len(student)):
        e = Label(f2,width=30, text=student[j],
	borderwidth=2,relief='ridge', anchor="w") 
        e.grid(row=i, column=j) 
        e = Button(f2,text='Login',width=18, 
	borderwidth=2,relief='ridge', anchor="w") 
        e.grid(row=i, column=2)
        #e.insert(END, student[j])
    i=i+1
    print()# line break at the end of one row

    

root.mainloop()

    # my_cursor = connection.cursor()
    # my_cursor.execute("SELECT * FROM login ")
#     rows=my_cursor.fetchall()
#     for row in rows:
#         print(row)
#         tree.insert("",tk.END,values=row)
#     my_cursor.close()

# tree=ttk.Treeview(f2,column=("c1","c2","c2"),show="headings")
# tree.column("#1",anchor=CENTER)
# tree.heading("#1", text="username")
# tree.column("#2",anchor=CENTER)
# tree.heading("#2", text="Password")
# tree.column("#3",anchor=CENTER)
# tree.heading("#3", text="LOGIN")
# tree.pack()

# but=Button(text='Login',command=lambda:Views())

# but.pack()