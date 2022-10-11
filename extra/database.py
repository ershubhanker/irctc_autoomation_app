#------------------program to create table in database mysql----------------


from tkinter import *
# def data():
# #     global v1,v2
    
#     # v1=StringVar()
#     # v2=StringVar()
    
#     # v1=e1
#     # v2=e2
    
#     # print(e1)
#     # print(e2)
    
#     e1=input('enter the usernam')
#     e2=input('password')
#     print(e1)
#     print(e2)
#     #database connection
#     import mysql.connector
#     connection=mysql.connector.connect(host='localhost',username='root',password='deol9646')
#     cursor=connection.cursor()
#     print('successfully connected')

#     #cursor.execute('''create table if not exists login(username text ,password text)''')

#     # cursor.execute('''INSERT INTO LOGIN(USERNAME, PASSWORD) 
#     # VALUES (%s ,%s)''',(v1, v2))
#     connection.commit()
#     try:  
#     #creating a new database  
#         cursor.execute("create database train_login")  
#         print('created')
#         #getting the list of all the databases which will now include the new database PythonDB  
#         dbs = cursor.execute("show databases")  
        
#     except:  
#         connection.rollback()
#         print('rollback') 
#     for x in cursor:  
#         print(x)
# data()
from tkinter import ttk,messagebox
from tkinter import font  as tkfont
from tkcalendar import DateEntry

import mysql.connector
connection=mysql.connector.connect(host='localhost',username='root',password='deol9646',database="train_login")
root = Tk()
root.configure(bg='sky blue')
root.title("IRCTC")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("1200x600+200+50")


font1=tkfont.Font(family='Times', size=15, weight="bold")
def passanger_screen():
    global p1,a2,g1,from_entry,to_entry,date_entry

    page2=Frame(root,bg='sky blue', width=1200, height=550)
    page2.place(x=0,y=0)
    font1=tkfont.Font(family='Helvetica', size=10, weight="bold")
    #frames
    pf1=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
    pf1.place(x=0,y=0,width=350,height=500)

    l1=Label(pf1,text='Train Details',bg='light gray',foreground='white',font=font1)
    l1.place(x=0,y=0,width=336,height=40)

   
    p_name = StringVar()
    p_age = StringVar()
   
    
 #frame2 passanger detail
    pf2=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
    pf2.place(x=350,y=0,width=850,height=500)

    l2=Label(pf2,text='Enter Passenger Details',bg='light gray',foreground='white',font=font1)
    l2.place(x=0,y=0,width=835,height=40)


    #Column labels 
    label1=Label(pf2,text='Passenger Name',bg='sky blue',font=font1)
    label1.place(x=20,y=60,width=120,height=25)
    p1=Entry(pf2,textvariable=p_name)
    p1.place(x=10,y=90,width=140,height=25)

    p2=Entry(pf2)
    p2.place(x=10,y=120,width=140,height=25)

    p3=Entry(pf2)
    p3.place(x=10,y=150,width=140,height=25)

    p4=Entry(pf2)
    p4.place(x=10,y=180,width=140,height=25)

    #age
    label2=Label(pf2,text='Age',bg='sky blue',font=font1)
    label2.place(x=160,y=60,width=40,height=25)
    a1=Entry(pf2,textvariable=p_age)
    a1.place(x=165,y=90,width=30,height=25)


def pass_add():
        name = p1.get()
        age = a2.get()
        gender = g1.get()
        ifrom = from_entry.get()
        ito = to_entry.get()
        date = date_entry.get()
    
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            mycursor.execute('''create table if not exists passanger_data(name text ,age text)''')
            sql = "INSERT INTO  passanger_data (NAME,AGE,GENDER,IFROM,ITO) VALUES (%s, %s)"
            val = (name,age)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "passanger data inserted successfully...")
            p1.delete(0, END)
            a2.delete(0, END)
          
            p1.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
passanger_screen()
root.mainloop()
