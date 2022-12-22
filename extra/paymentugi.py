from tkinter import *
from tkinter import font  as tkfont
from turtle import bgcolor
from PIL import ImageTk, Image
from tkinter import ttk,messagebox
import mysql.connector

#----root window----
root = Tk()
root.configure(bg='sky blue')
root.title("IRCTC")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("1200x600+200+50")



font1=tkfont.Font(family='Times', size=15, weight="bold")
page3=Frame(root,bg='#80aaff', width=1200, height=550)
page3.place(x=0,y=0)

upibutton=Button(page3,text="UPI PAY",font=font1,bg='white',activebackground='black'
,activeforeground='white',width=30,command=lambda:upi())
upibutton.place(x=70,y=10)

Debitbutton=Button(page3,text="Debit PAY",font=font1,bg='white',activebackground='black'
,activeforeground='white',width=30,command=lambda:debit())
Debitbutton.place(x=460,y=10)

def upi():
    upiframe=Frame(page3,bg='white',width=550, height=400,bd=5,highlightbackground="black", highlightthickness=1)
    upiframe.place(x=10,y=60)
    upi_label = Label(upiframe,text="Upi payment",font=font1,fg='#80aaff',bg='white')
    upi_label.place(x = 185, y = 55)

    def temp_text(e):
        upi_entry.delete(0,"end")
        upi_entry.config(fg = 'black',font=font1) #entry text color

    p_name=StringVar()

    upi_entry=Entry(upiframe,width=30,bd=2,font=font1,textvariable=p_name)
    upi_entry.insert(0, "Enter UPI address") #temp text
    upi_entry.config(fg = 'light grey') #temp text color
    upi_entry.place(x=100,y=100)
    upi_entry.bind("<FocusIn>",temp_text)

    upi_btn=Button(upiframe,text='Save',width=15,font=font1,bg='white',activebackground='black'
    ,activeforeground='white',command=lambda:Add())
    upi_btn.place(x=220,y=250)

    upi_del=Button(page3,text="Delete",width=10,font=font1,bg='white',activebackground='black'
    ,activeforeground='white',command=lambda:Add())
    upi_del.place(x=600,y=450)

    upi_upd=Button(page3,text="update",width=10,font=font1,bg='white',activebackground='black'
    ,activeforeground='white',command=lambda:Add())
    upi_upd.place(x=800,y=450)
    # upilist=Frame(page3,bg='white',width=550, height=450)
    # upilist.place(x=570,y=60)
    # add user and pass in database
    def Add():
        
        upi = upi_entry.get()
        
        print(upi)
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            mycursor.execute('''create table if not exists upi_data(id int(15) auto_increment ,upi text,primary key(id))''')
            sql = "INSERT INTO upi_data (ID,UPI) VALUES  (%s,%s)"
            val = (0,upi)
            mycursor.execute(sql,val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "upi inserted successfully...")
            upi_entry.delete(0, END)
            upi_entry.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    # show user and pass in list
    def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
        mycursor = mysqldb.cursor()
        try:
            mycursor.execute("SELECT id,upi FROM upi_data")
        except Exception as e:
            print(e)
        records = mycursor.fetchall()
        print(records)
        for i, (id,upi) in enumerate(records, start=1):
            listbox.insert("", "end", values=(id,upi))
            mysqldb.close()
    cols=("id","upi")
    listbox=ttk.Treeview(page3,columns=cols,show='headings')
    listbox.column('id', anchor=W, width=40)
    listbox.column('upi', anchor=W, width=80)
    for col in cols:
        listbox.heading(col, text=col)
        listbox.place(x=570,y=60)
        listbox.place(width=600,height=330)
    show()
    #listbox.bind("<Double-Button-1>",GetValue)


def debit():
    font2=tkfont.Font(family='Times New Roman', size=15, weight="bold")
    Debitframe=Frame(page3,bg='white',width=550, height=400,bd=5,highlightbackground="black", highlightthickness=1)
    Debitframe.place(x=10,y=60)
    bank_name = StringVar()
    card_type = StringVar()
    card_no = StringVar()
    valid_M = StringVar()
    valid_y = StringVar()
    name_on_card = StringVar()
    cvv = StringVar()
    pass3d = StringVar()
    name = StringVar()

    bank_name = Label(Debitframe,text="Bank Name :",font=font2,bg='white')
    bank_name.place(x = 25, y = 10)
    debit_e1=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
    debit_e1.place(x=270,y=10)

    card_type = Label(Debitframe,text="Card Type :",font=font2,bg='white')
    card_type.place(x = 25, y = 50)
    debit_e2=Entry(Debitframe,width=15,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
    debit_e2.place(x=270,y=50)

    card_no = Label(Debitframe,text="Card Number :",font=font2,bg='white')
    card_no.place(x = 25, y = 90)
    debit_e3=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
    debit_e3.place(x=270,y=90)

    valid = Label(Debitframe,text="Expiry mm/yy :",font=font2,bg='white')
    valid.place(x = 25, y = 130)
    debit_M=Entry(Debitframe,width=6,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
    debit_M.place(x=270,y=130)

    debit_Y=Entry(Debitframe,width=6,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
    debit_Y.place(x=390,y=130)

    name_on_card = Label(Debitframe,text="Name On Card :",font=font2,bg='white')
    name_on_card.place(x = 25, y = 170)
    debit_e5=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
    debit_e5.place(x=270,y=170)

    cvv = Label(Debitframe,text="CVV :",font=font2,bg='white')
    cvv.place(x = 25, y = 210)
    debit_e6=Entry(Debitframe,width=7,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
    debit_e6.place(x=270,y=210)

    pass3d = Label(Debitframe,text="3D Password :",font=font2,bg='white')
    pass3d.place(x = 25, y = 250)
    debit_e7=Entry(Debitframe,width=10,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
    debit_e7.place(x=270,y=250)

    

    debit_btn=Button(Debitframe,text='Save',width=15,font=font1,fg='white',bg='black',activebackground='white'
    ,activeforeground='black',command=lambda:add_debit())
    debit_btn.place(x=270,y=340)
    #function for get username and password from entry
    def GetValue(event):
        
        debit_e1.delete(0, END)
        debit_e2.delete(0, END)
        debit_e3.delete(0, END)
        debit_M.delete(0, END)
        debit_Y.delete(0, END)
        debit_e5.delete(0, END)
        debit_e6.delete(0, END)
        debit_e7.delete(0, END)

        row_id=listbox.selection()[0]
        select=listbox.set(row_id)
        #Bank","Card_type","Card_num","month","year","owner","cvv","pass3d","Name
        debit_e1.insert(0,select['Bank'])
        debit_e2.insert(0,select['Card_type'])
        debit_e3.insert(0,select['Card_num'])
        debit_M.insert(0,select['month'])
        debit_Y.insert(0,select['year'])
        debit_e5.insert(0,select['owner'])
        debit_e6.insert(0,select['cvv'])
        debit_e7.insert(0,select['pass3d'])
    
    def add_debit():
        
        bank_name = debit_e1.get()
        card_type = debit_e2.get()
        card_number = debit_e3.get()
        validity_m = debit_M.get()
        validity_y = debit_Y.get()
        name_on_card = debit_e5.get()
        cvv = debit_e6.get()
        pass3d = debit_e7.get()
        
        
   
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            mycursor.execute('''create table if not exists debit_data(bank_name text,card_type text,card_number text,
            validity_m text,validity_y text,name_on_card text,cvv text,pass3d text)''')
            sql = "INSERT INTO debit_data ( BANK_NAME,CARD_TYPE,CARD_NUMBER,VALIDITY_M,VALIDITY_Y,NAME_ON_CARD,CVV,PASS3D ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (bank_name,card_type,card_number,validity_m,validity_y,name_on_card,cvv,pass3d)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "DEBIT CARD inserted successfully...launch app again to watch")
            debit_e1.delete(0, END)
            debit_e2.delete(0, END)
            debit_e3.delete(0, END)
            debit_M.delete(0, END)
            debit_Y.delete(0, END)
            debit_e5.delete(0, END)
            debit_e6.delete(0, END)
            debit_e7.delete(0, END)
            debit_e1.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def debitshow():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
        mycursor = mysqldb.cursor()
        try:
            mycursor.execute("SELECT bank_name,card_type,card_number,validity_m,validity_y,name_on_card,cvv,pass3d FROM debit_data")
        except Exception as e:
            print(e)
        records = mycursor.fetchall()
        print(records)
        for i, (bank_name,card_type,card_number,validity_m,validity_y,name_on_card,cvv,pass3d) in enumerate(records, start=1):
            listbox.insert("", "end", values=(bank_name,card_type,card_number,validity_m,validity_y,name_on_card,cvv,pass3d))
            mysqldb.close()
    cols=("Bank","Card_type","Card_num","month","year","Holder","cvv","pass3d")
    
    listbox=ttk.Treeview(page3,columns=cols,show='headings')
    listbox.column('Bank', anchor=CENTER, width=60)
    listbox.column('Card_type', anchor=CENTER, width=50)
    listbox.column('Card_num', anchor=CENTER, width=80)
    listbox.column('month', anchor=CENTER, width=30)
    listbox.column('year', anchor=CENTER, width=30)
    listbox.column('Holder', anchor=CENTER, width=80)
    listbox.column('cvv', anchor=CENTER, width=40)
    listbox.column('pass3d', anchor=CENTER, width=50)

    for col in cols:
        listbox.heading(col, text=col)
        listbox.place(x=570,y=60)
        listbox.place(width=600,height=330)
    debitshow()
    listbox.bind("<Double-Button-1>",GetValue)


root.mainloop()




