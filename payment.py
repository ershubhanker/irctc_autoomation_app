from libraries import *
from _main import *
<<<<<<< HEAD
mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
mycursor = mysqldb.cursor()
=======
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
method_pay={'method_p':""}
class Payment_screen:
    def __init__(self,root,upi_value,debit_value,method_pay):
        self.root = root
        self.upi_value=upi_value
        self.method_pay=method_pay
        self.debit_value=debit_value

    def payment_screen(self):
        print(self.method_pay)
        
        self.font1=tkfont.Font(family='Times', size=15, weight="bold")
<<<<<<< HEAD
        self.page3=Frame(self.root,bg='sky blue', width=700, height=290)
        self.page3.place(x=0,y=0)

        self.upibutton=Button(self.page3,text="UPI PAY",font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',width=10,command=lambda:[self.upi()])
        self.upibutton.place(x=10,y=10,height=25)

        self.Debitbutton=Button(self.page3,text="Debit PAY",font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',width=10,command=lambda:[self.debit()])
        self.Debitbutton.place(x=200,y=10,height=25)
        # self.upi()

    # def pay_method(self):
        
    #     p_method =StringVar()
    #     p_method.set(method_pay["method_p"])
        
    #     #label for num of passangers
    #     # p_method=Label(self.page3,text='payment method :',bg='sky blue',font=self.font1)
    #     # p_method.place(x=530,y=50,width=150,height=25)
    #     method = [
    #         "UPI",
    #         "DEBIT",
        
    #     ] 
    #         # Create Dropdown menu
    #     self.m1 = ttk.Combobox(self.page3,state="readonly",values=method,textvariable=p_method) #readonly
    #     self.m1.place(x=450,y=300,width=50,height=40)
    #     self.m1.current(0)
=======
        self.page3=Frame(self.root,bg='#80aaff', width=1200, height=550)
        self.page3.place(x=0,y=0)

        self.upibutton=Button(self.page3,text="UPI PAY",font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',width=30,command=lambda:[self.upi(),self.pay_method()])
        self.upibutton.place(x=70,y=10)

        self.Debitbutton=Button(self.page3,text="Debit PAY",font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',width=30,command=lambda:[self.debit(),self.pay_method()])
        self.Debitbutton.place(x=460,y=10)


    def pay_method(self):
        
        p_method =StringVar()
        p_method.set(method_pay["method_p"])
        
        #label for num of passangers
        p_method=Label(self.page3,text='payment method :',bg='#80aaff',font=self.font1)
        p_method.place(x=230,y=500,width=150,height=25)
        method = [
            "UPI",
            "DEBIT",
        
        ] 
            # Create Dropdown menu
        self.m1 = ttk.Combobox(self.page3,state="readonly",values=method,textvariable=p_method) #readonly
        self.m1.place(x=390,y=500,width=60,height=30)
        self.m1.current(0)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29

    def upi(self):
        #global self.upi_entry
        print(self.upi_value)
<<<<<<< HEAD
        p_method =StringVar()
        p_method.set(method_pay["method_p"])
        method = "UPI"
            
        
        upiframe=Frame(self.page3,bg='white',width=265, height=250,bd=5,highlightbackground="black", highlightthickness=1)
        upiframe.place(x=2,y=40)
        upi_label = Label(upiframe,text="Upi payment",font=self.font1,fg='#80aaff',bg='white')
        upi_label.place(x = 80, y = 35)
=======


        
        upiframe=Frame(self.page3,bg='white',width=550, height=400,bd=5,highlightbackground="black", highlightthickness=1)
        upiframe.place(x=10,y=60)
        upi_label = Label(upiframe,text="Upi payment",font=self.font1,fg='#80aaff',bg='white')
        upi_label.place(x = 185, y = 55)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29

        upi_name=StringVar()
        # temp_name=StringVar()
        upi_name.set(self.upi_value["upi"])
        # temp_name.set(self.upi_value["temp_name"])

<<<<<<< HEAD
        self.upi_entry=Entry(upiframe,width=15,bd=3,font=self.font1,textvariable=upi_name)
        self.upi_entry.place(x=65,y=100)

        upi_btn=Button(self.page3,text="save",width=7,font=self.font1,fg='white',bg='black',activebackground='white'
        ,activeforeground='black',command=lambda:Add())
        upi_btn.place(x=470,y=60,height=25)


        upi_del=Button(self.page3,text="Delete",width=7,font=self.font1,fg='white',bg='black',activebackground='white'
        ,activeforeground='black',command=lambda:upi_delete())
        upi_del.place(x=470,y=120,height=25)


        select_upi=Button(self.page3,text="USE",width=7,font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:[method(self)])
        select_upi.place(x=470,y=180,height=25)
=======
        self.upi_entry=Entry(upiframe,width=30,bd=2,font=self.font1,textvariable=upi_name)
        self.upi_entry.place(x=100,y=100)

        # upi_temp = Label(upiframe,text="Give a name to save",font=self.font1,fg='#80aaff',bg='white')
        # upi_temp.place(x = 105, y = 145)
        # self.temp_entry=Entry(upiframe,width=30,bd=2,font=self.font1,textvariable=temp_name)
        # self.temp_entry.place(x=100,y=180)

        upi_btn=Button(upiframe,text='Save',width=15,font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:Add())
        upi_btn.place(x=220,y=250)

        upi_del=Button(self.page3,text="Delete",width=10,font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:upi_delete())
        upi_del.place(x=600,y=450)

        upi_upd=Button(self.page3,text="update",width=10,font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:upi_update())
        upi_upd.place(x=800,y=450)

        select_upi=Button(self.page3,text="USE UPI",width=10,font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:[method(self)])
        select_upi.place(x=50,y=490)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
        # upilist=Frame(self.page3,bg='white',width=550, height=450)
        # upilist.place(x=570,y=60)
        # add user and pass in database
        
        def method(self):
            global meth
            upi = self.upi_entry.get()
            # name=self.temp_entry.get()
            self.upi_value["upi"] = upi
            # self.upi_value["temp_name"] = name
<<<<<<< HEAD
            # self.meth=self.m1.get()
            self.method_pay["method_p"]="UPI"
=======
            self.meth=self.m1.get()
            self.method_pay["method_p"]=self.meth
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
            print(self.upi_value)
            print(self.method_pay)
        def GetValue(event):
            upi = self.upi_entry.get()
            # name=self.temp_entry.get()
            self.upi_value["upi"] = upi
            # self.upi_value["temp_name"] = name
            self.upi_entry.delete(0, END)
            # self.temp_entry.delete(0, END)

            row_id=listbox.selection()[0]
            select=listbox.set(row_id)
        
            self.upi_entry.insert(0,select['upi'])
            # self.temp_entry.insert(0,select['name'])
        def Add():
            
            upi = self.upi_entry.get()
            # name=self.temp_entry.get()
            self.upi_value["upi"] = upi
            # self.upi_value["temp_name"] = name
            print(self.upi_value)
            
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()
        
            try:
                # mycursor.execute('''create table if not exists upi_data(id int(15) auto_increment ,upi text,name text,primary key(id))''')
                sql = "INSERT INTO upi_data (ID,UPI) VALUES  (%s,%s)"
                val = (0,upi)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "upi inserted successfully...")
                self.upi_entry.delete(0, END)
                self.upi_entry.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        # update user and pass in database
        def upi_update():
            upi = self.upi_entry.get()
            # name=self.temp_entry.get()
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()
        
            try:
                sql = "Update upi_data set upi= %s where id='1'"

                val = (0,upi)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "upi Updated successfully...")
                self.upi_entry.delete(0, END)
                # self.temp_entry.delete(0, END)
                self.upi_entry.focus_set()
        
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        # # delete user and pass from database
        def upi_delete():
            upi = self.upi_entry.get()
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()
            try:
                sql = "delete from upi_data where upi = %s"
                val = (upi,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "upi Deleteeeee successfully...")
                self.upi_entry.delete(0, END)
                # self.temp_entry.delete(0, END)
                self.upi_entry.focus_set()
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
<<<<<<< HEAD
                
=======
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
        cols=("id","upi")
        listbox=ttk.Treeview(self.page3,columns=cols,show='headings')
        listbox.column('id', anchor=CENTER, width=3)
        listbox.column('upi', anchor=CENTER, width=120)
        
        for col in cols:
            listbox.heading(col, text=col)
<<<<<<< HEAD
            listbox.place(x=265,y=40)
            listbox.place(width=200,height=250)
=======
            listbox.place(x=570,y=60)
            listbox.place(width=600,height=330)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
        show()
        listbox.bind("<Double-Button-1>",GetValue)
    



    def debit(self):
<<<<<<< HEAD
        p_method =StringVar()
        p_method.set(method_pay["method_p"])
        method = "DEBIT"
        #global debit_e1,debit_e2,debit_e3,debit_M,debit_Y,debit_e5,debit_e6,cvv,pass3d
        font2=tkfont.Font(family='Times New Roman', size=15, weight="bold")
        print(self.debit_value)
        Debitframe=Frame(self.page3,bg='white',width=265, height=250,bd=5,highlightbackground="black", highlightthickness=1)
        Debitframe.place(x=2,y=40)
=======
        #global debit_e1,debit_e2,debit_e3,debit_M,debit_Y,debit_e5,debit_e6,cvv,pass3d
        font2=tkfont.Font(family='Times New Roman', size=15, weight="bold")
        print(self.debit_value)
        Debitframe=Frame(self.page3,bg='white',width=550, height=400,bd=5,highlightbackground="black", highlightthickness=1)
        Debitframe.place(x=10,y=60)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29

        bank_name = StringVar()
        card_type = StringVar()
        card_no = StringVar()
        valid_M = StringVar()
        valid_Y = StringVar()
        owner = StringVar()
        cvv = StringVar()
        pass3d = StringVar()
        name = StringVar()

        #'bank name':"",'card type':"",'card number':"",'expiry month':"",'expiry year':'','owner':"",'cvv':"",'3D pass':""
        
        bank_name.set(self.debit_value["bank name"])
        card_type.set(self.debit_value["card type"])
        card_no.set(self.debit_value["card number"])
        valid_M.set(self.debit_value["expiry month"])
        valid_Y.set(self.debit_value["expiry year"])
        owner.set(self.debit_value["owner"])
        cvv.set(self.debit_value["cvv"])
        pass3d.set(self.debit_value["3D pass"])


<<<<<<< HEAD
        Bank_name = Label(Debitframe,text="Bank :",font=font2,bg='white')
        Bank_name.place(x = 5, y = 0)
        debit_e1=Entry(Debitframe,width=15,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=bank_name)
        debit_e1.place(x=100,y=0,height=25)

        Card_type = Label(Debitframe,text="C_Type :",font=font2,bg='white')
        Card_type.place(x = 5, y = 35)
        debit_e2=Entry(Debitframe,width=5,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=card_type)
        debit_e2.place(x=100,y=35,height=25)

        Card_no = Label(Debitframe,text="Card_No :",font=font2,bg='white')
        Card_no.place(x = 5, y = 70)
        debit_e3=Entry(Debitframe,width=15,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=card_no)
        debit_e3.place(x=100,y=70,height=25)

        valid = Label(Debitframe,text="mm/yy :",font=font2,bg='white')
        valid.place(x = 5, y = 105)
        debit_M=Entry(Debitframe,width=5,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=valid_M)
        debit_M.place(x=100,y=105,height=25)

        debit_Y=Entry(Debitframe,width=5,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=valid_Y)
        debit_Y.place(x=170,y=105,height=25)

        name_on_card = Label(Debitframe,text="Owner:",font=font2,bg='white')
        name_on_card.place(x = 5, y = 140)
        debit_e5=Entry(Debitframe,width=10,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=owner)
        debit_e5.place(x=100,y=140,height=25)

        Cvv = Label(Debitframe,text="CVV :",font=font2,bg='white')
        Cvv.place(x = 5, y = 175)
        debit_e6=Entry(Debitframe,width=5,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=cvv)
        debit_e6.place(x=100,y=175,height=25)

        Pass3d = Label(Debitframe,text="3D Pass :",font=font2,bg='white')
        Pass3d.place(x = 5, y = 210)
        debit_e7=Entry(Debitframe,width=7,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=pass3d)
        debit_e7.place(x=100,y=210,height=25)

        

        debit_btn=Button(self.page3,text='Save',width=7,font=self.font1,fg='white',bg='black',activebackground='white'
        ,activeforeground='black',command=lambda:add_debit())
        debit_btn.place(x=470,y=60,height=25)
        debit_del=Button(self.page3,text="Delete",width=7,font=self.font1,fg='white',bg='black',activebackground='white'
        ,activeforeground='black',command=lambda:debit_delete())
        debit_del.place(x=470,y=120,height=25)

        select_debit=Button(self.page3,text="USE",width=7,font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:method(self))

        select_debit.place(x=470,y=180,height=25)
=======
        Bank_name = Label(Debitframe,text="Bank Name :",font=font2,bg='white')
        Bank_name.place(x = 25, y = 10)
        debit_e1=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=bank_name)
        debit_e1.place(x=270,y=10)

        Card_type = Label(Debitframe,text="Card Type :",font=font2,bg='white')
        Card_type.place(x = 25, y = 50)
        debit_e2=Entry(Debitframe,width=15,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=card_type)
        debit_e2.place(x=270,y=50)

        Card_no = Label(Debitframe,text="Card Number :",font=font2,bg='white')
        Card_no.place(x = 25, y = 90)
        debit_e3=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=card_no)
        debit_e3.place(x=270,y=90)

        valid = Label(Debitframe,text="Expiry mm/yy :",font=font2,bg='white')
        valid.place(x = 25, y = 130)
        debit_M=Entry(Debitframe,width=6,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=valid_M)
        debit_M.place(x=270,y=130)

        debit_Y=Entry(Debitframe,width=6,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=valid_Y)
        debit_Y.place(x=390,y=130)

        name_on_card = Label(Debitframe,text="Name On Card :",font=font2,bg='white')
        name_on_card.place(x = 25, y = 170)
        debit_e5=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=owner)
        debit_e5.place(x=270,y=170)

        Cvv = Label(Debitframe,text="CVV :",font=font2,bg='white')
        Cvv.place(x = 25, y = 210)
        debit_e6=Entry(Debitframe,width=7,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=cvv)
        debit_e6.place(x=270,y=210)

        Pass3d = Label(Debitframe,text="3D Password :",font=font2,bg='white')
        Pass3d.place(x = 25, y = 250)
        debit_e7=Entry(Debitframe,width=10,font=font2,bd=1,highlightbackground="grey", highlightthickness=1,textvariable=pass3d)
        debit_e7.place(x=270,y=250)

        

        debit_btn=Button(Debitframe,text='Save',width=15,font=self.font1,fg='white',bg='black',activebackground='white'
        ,activeforeground='black',command=lambda:add_debit())
        debit_btn.place(x=270,y=340)

        select_debit=Button(self.page3,text="USE DEBIT",width=10,font=self.font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:method(self))
        select_debit.place(x=50,y=490)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29

        def method(self):
            e1 = debit_e1.get()
            e2=debit_e2.get()
            e3=debit_e3.get()
            month=debit_M.get()
            year=debit_Y.get()
            e5=debit_e5.get()
            e6=debit_e6.get()
            e7=debit_e7.get()
            #bank name':"",'card type':"",'card number':"",'expiry month':"",'expiry year':'','owner':"",'cvv':"",'3D pass'
            self.debit_value["bank name"] = e1
            self.debit_value["card type"] = e2
            self.debit_value["card number"] = e3
            self.debit_value["expiry month"] = month
            self.debit_value["expiry year"] = year
            self.debit_value["owner"] = e5
            self.debit_value["cvv"] = e6
            self.debit_value["3D pass"] = e7
<<<<<<< HEAD
            self.method_pay["method_p"]="DEBIT"
        
            print(self.method_pay)
           
            print(self.debit_value)
        #function for get username and password from entry
        def debit_delete(self):
            pass
        
        def GetValue(event):
            mycursor.execute(f"SELECT BANK_NAME,CARD_TYPE,CARD_NUMBER,VALIDITY_M,VALIDITY_Y,HOLDER,CVV,PASS3D FROM debit_data ")
            value = mycursor.fetchall()
            e1=value[0][0]
            e2=value[0][1]
            e3=value[0][2]
            month=value[0][3]
            year=value[0][4]
            e5=value[0][5]
            e6=value[0][6]
            e7=value[0][7]
            
=======
            self.meth=self.m1.get()
            method_pay["method_p"]=self.meth
            print(method_pay)
            print(self.debit_value)
        #function for get username and password from entry
        def GetValue(event):
            e1 = debit_e1.get()
            e2=debit_e2.get()
            e3=debit_e2.get()
            month=debit_M.get()
            year=debit_Y.get()
            e5=debit_e5.get()
            e6=debit_e6.get()
            e7=debit_e7.get()
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
            #bank name':"",'card type':"",'card number':"",'expiry month':"",'expiry year':'','owner':"",'cvv':"",'3D pass'
            self.debit_value["bank name"] = e1
            self.debit_value["card type"] = e2
            self.debit_value["card number"] = e3
            self.debit_value["expiry month"] = month
            self.debit_value["expiry year"] = year
            self.debit_value["owner"] = e5
            self.debit_value["cvv"] = e6
            self.debit_value["3D pass"] = e7

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
<<<<<<< HEAD
            debit_e1.insert(0,e1)
            debit_e2.insert(0,e2)
            debit_e3.insert(0,e3)
            debit_M.insert(0,month)
            debit_Y.insert(0,year)
            debit_e5.insert(0,e5)
            debit_e6.insert(0,e6)
            debit_e7.insert(0,e7)
=======
            debit_e1.insert(0,select['Bank'])
            debit_e2.insert(0,select['Card_type'])
            debit_e3.insert(0,select['Card_num'])
            debit_M.insert(0,select['month'])
            debit_Y.insert(0,select['year'])
            debit_e5.insert(0,select['Holder'])
            debit_e6.insert(0,select['cvv'])
            debit_e7.insert(0,select['pass3d'])
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
            
        def add_debit():
            
            bank_name = debit_e1.get()
            card_type = debit_e2.get()
            card_number = debit_e3.get()
            validity_m = debit_M.get()
            validity_y = debit_Y.get()
            holder = debit_e5.get()
            cvv = debit_e6.get()
            pass3d = debit_e7.get()
            
            
    
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()
        
            try:
                # mycursor.execute('''create table if not exists debit_data(bank_name text,card_type text,card_number text,
                # validity_m text,validity_y text,holder text,cvv text,pass3d text)''')
                sql = "INSERT INTO debit_data ( BANK_NAME,CARD_TYPE,CARD_NUMBER,VALIDITY_M,VALIDITY_Y,HOLDER,CVV,PASS3D ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (bank_name,card_type,card_number,validity_m,validity_y,holder,cvv,pass3d)
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
<<<<<<< HEAD
                mycursor.execute("SELECT bank_name,card_number FROM debit_data")
=======
                mycursor.execute("SELECT bank_name,card_type,card_number,validity_m,validity_y,holder,cvv,pass3d FROM debit_data")
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
            except Exception as e:
                print(e)
            records = mycursor.fetchall()
            print(records)
<<<<<<< HEAD
            for i, (bank_name,card_number) in enumerate(records, start=1):
                listbox.insert("", "end", values=(bank_name,card_number))
                mysqldb.close()
        cols=("Bank","Card_num")
        
        listbox=ttk.Treeview(self.page3,columns=cols,show='headings')
        listbox.column('Bank', anchor=CENTER, width=60)
        listbox.column('Card_num', anchor=CENTER, width=80)

        for col in cols:
            listbox.heading(col, text=col)
            listbox.place(x=265,y=40)
            listbox.place(width=200,height=250)
=======
            for i, (bank_name,card_type,card_number,validity_m,validity_y,holder,cvv,pass3d) in enumerate(records, start=1):
                listbox.insert("", "end", values=(bank_name,card_type,card_number,validity_m,validity_y,holder,cvv,pass3d))
                mysqldb.close()
        cols=("Bank","Card_type","Card_num","month","year","Holder","cvv","pass3d")
        
        listbox=ttk.Treeview(self.page3,columns=cols,show='headings')
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
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
        debitshow()
        listbox.bind("<Double-Button-1>",GetValue)
