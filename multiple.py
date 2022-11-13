# from ast import Delete
from cProfile import label
from tkinter import *
#import tkinter as tk
from tkinter import ttk,messagebox
# from turtle import heading, width 
#from PIL import Image, ImageTk
# from tkinter.messagebox import askyesno
from tkinter import font  as tkfont
from functools import partial
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
import time
import PIL.Image
from PIL import Image,ImageFilter,ImageTk
from functools import partial
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import mysql.connector
connection=mysql.connector.connect(host='localhost',username='root',password='deol9646',database="train_login")
from tkcalendar import DateEntry
import multiprocessing
from ttkwidgets import CheckboxTreeview
#database connect
my_conn = connection.cursor()
# create login table
my_conn.execute('''create table if not exists login(username text ,password text ,name text)''')



#passanger value dictionary
passanger_value={'name':"",'age':"",'gender':"",'name2':"",'age2':"",'gender2':"",'name3':"",'age3':"",'gender3':"",'name4':"",
'age4':"",'gender4':"",'name5':"",'age5':"",'gender5':"",'name6':"",'age6':"",'gender6':"",'ifrom':"",'ito':"",'date':"",'total':"",'qouta':""}
payment_value={'upi':"",'temp_name':""}
debit_value={'bank name':"",'card type':"",'card number':"",'expiry month':"",'expiry year':'','owner':"",'cvv':"",'3D pass':""}
method_pay={'method_p':""}
# print("File location using os.getcwd():", os.getcwd())
var=os.getcwd()
# a=f"{var}\logo.png"
# print(a)
#irctc website fuction
root = Tk()
root.configure(bg='sky blue')
root.title("IRCTC")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("1200x600+200+50")
icon=PhotoImage(file='icon.png')
root.iconphoto(False,icon)

#irctc login screen

global e1,e2
page1=Frame(root,bg='sky blue', width=1200, height=550)
page1.place(x=0,y=0)
font1=tkfont.Font(family='Times', size=15, weight="bold")

#frame 1 for username and password detail
f1=Frame(page1 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=1)
f1.place(x=140,y=20,width=880,height=200)
#labels
label1=Label(page1,text='Login Details',bg='sky blue',font=font1)
label1.place(x=170, y=10)
label2=Label(f1,text='Irctc ID :',bg='sky blue',font=("Times",12,"bold"))
label2.place(x=100, y=10)
label3=Label(f1,text='Password :',bg='sky blue',font=("Times",12,"bold"))
label3.place(x=400, y=10)
temp = StringVar()
temp_lbl=Label(f1,text='Give a name to store',fg='white',bg='sky blue',font=("Times",11,'bold'))
temp_lbl.place(x=365, y=50)
temp_entry=Entry(f1,font=("Times",11,"bold"),textvariable=temp)
temp_entry.place(x=350,y=70)


username = StringVar()
password = StringVar()
#username entry
e1=Entry(f1,font=("Times",12,"bold"),textvariable=username)
e1.place(x=180, y=10,width=200,height=30)
#password entry
e2=Entry(f1,font=("Times",12,"bold"),textvariable=password)
e2.place(x=490, y=10,width=200,height=30)
#save button
save = Button(f1, text = 'Add',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : [Add()])
save.place(x=330, y=120,width=200,height=30)


# frame 2 for list view for login data
f2=Frame(page1,bg='sky blue')
f2.place(x=250,y=220,width=740,height=330)

#frame 2 button delete update login 
delb = Button(f2, text = 'Delete',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : [delete()])
delb.place(x=530, y=80,width=150,height=30)
upd = Button(f2, text = 'Update',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : [update()])
upd.place(x=530, y=140,width=150,height=30)
login = Button(f2, text = 'LOGIN',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : update())
login.place(x=530, y=200,width=150,height=30)
login = Button(f2, text = 'get data',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : getrow())
login.place(x=530, y=260,width=150,height=30)


im_checked=ImageTk.PhotoImage(Image.open('checked.png'))
im_unchecked=ImageTk.PhotoImage(Image.open('unchecked.png'))


cols=("No.","username","password")
listbox=ttk.Treeview(f2,columns=cols)
style=ttk.Style(listbox)
style.configure("Treeview",rowheight=30)

listbox.tag_configure("checked",image=im_checked)
listbox.tag_configure("unchecked",image=im_unchecked)




listbox.column('username', anchor=CENTER, width=50)
listbox.column('password', anchor=CENTER, width=50)
listbox.column('No.', anchor=CENTER, width=20)



for col in cols:
    
    listbox.heading(col, text=col)
    
    listbox.place(width=500,height=330)

    

def togglecheck(event):
    rowid=listbox.identify_row(event.y) #got row id
    tag=listbox.item(rowid,"tags")[0]  # call tag current state 0 index
    tags=list(listbox.item(rowid,"tags")) # call all the tags & covert to list
    tags.remove(tag)
    listbox.item(rowid,tags=tags) #reset tag
    if tag=="checked":
        listbox.item(rowid,tags="unchecked")

    else:
        listbox.item(rowid,tags="checked")
        

def getrow():
    row_id=listbox.selection()
    #select=listbox.set(row_id)
    for item in row_id:
        c1=listbox.item(item)
        value=c1.get("values")
        print(value)

   




#function for get username and password from entry
def GetValue(event):
    
    e1.delete(0,END)
    e2.delete(0,END)
    temp_entry.delete(0,END)
    row_id=listbox.selection()[0]
    select=listbox.set(row_id)
    e1.insert(0,select['username'])
    e2.insert(0,select['password'])
    temp_entry.insert(0,select['No.'])

# add user and pass in database
def Add():
    username = e1.get()
    password = e2.get()
    name=temp_entry.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO  login (username,password,name) VALUES (%s, %s,%s)"
        val = (username,password,name)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "agent id inserted successfully...launch app again to watch")
        e1.delete(0, END)
        e2.delete(0, END)
        temp_entry.delete(0,END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

# update user and pass in database
def update():
    username = e1.get()
    password = e2.get()
    name=temp_entry.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
    mycursor=mysqldb.cursor()

    try:
        sql = "Update login set username= %s , password= %s where name =%s"

        val = (username,password,name)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updateddddd successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

# # delete user and pass from database
def delete():
    username = e1.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
    mycursor=mysqldb.cursor()
    try:
        sql = "delete from login where username = %s"
        val = (username,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

# show user and pass in list
def show():
    
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT name,username,password FROM login")
    records = mycursor.fetchall()
    

    print(records)
    for i, (name,username,password) in enumerate(records, start=1):
        
        
        listbox.insert("", "end", values=(name,username,password),tags="unchecked")
        
        connection.close()

show()
listbox.bind("<Double-Button-1>",GetValue)
#listbox.bind("<Button-1>",togglecheck)





#----root window----

root.mainloop()

