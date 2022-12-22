from libraries import *
from frame1 import *
from frame2 import *
from frame3 import *
from frame4 import *
from frame5 import *
from passanger import *


class Login_screen(Passanger_screen):
    def __init__(self,root):
        self.root = root
        
        
        self.username = ""
        self.password = ""
        Passanger_screen.__init__(self,root,passanger_value)
        
        # self.qouta=Passanger_screen.qouta
         
    
    def login_screen(self):
        # print()
        #print("Quta_entry :",Passanger_screen._qouta)
<<<<<<< HEAD
        page1=Frame(self.root,bg='sky blue', width=700, height=290)
=======
<<<<<<< HEAD
        page1=Frame(self.root,bg='sky blue', width=700, height=290)
=======
        page1=Frame(self.root,bg='sky blue', width=1200, height=550)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        page1.place(x=0,y=0)
        font1=tkfont.Font(family='Times', size=15, weight="bold")

        #frame 1 for username and password detail
        f1=Frame(page1 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=1)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        f1.place(x=10,y=15,width=555,height=50)
        #labels
        label1=Label(page1,text='Login Details',bg='sky blue',font=font1)
        label1.place(x=15, y=5,height=22)
        label2=Label(f1,text='Irctc ID :',bg='sky blue',font=("Times",12,"bold"))
        label2.place(x=25, y=7)
        label3=Label(f1,text='Password :',bg='sky blue',font=("Times",12,"bold"))
        label3.place(x=200, y=7)
<<<<<<< HEAD
=======
=======
        f1.place(x=140,y=20,width=880,height=200)
        #labels
        label1=Label(page1,text='Login Details',bg='sky blue',font=font1)
        label1.place(x=170, y=10)
        label2=Label(f1,text='Irctc ID :',bg='sky blue',font=("Times",12,"bold"))
        label2.place(x=100, y=10)
        label3=Label(f1,text='Password :',bg='sky blue',font=("Times",12,"bold"))
        label3.place(x=400, y=10)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        temp = StringVar()
        
        # temp_entry=Entry(f1,font=("Times",11,"bold"),textvariable=temp)
        # temp_entry.place(x=350,y=70)

        self.username = StringVar()
        self.password = StringVar()
        #username entry
        self.e1=Entry(f1,font=("Times",12,"bold"),textvariable=self.username)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        self.e1.place(x=90, y=6,width=100,height=25)
        #password entry
        self.e2=Entry(f1,font=("Times",12,"bold"),textvariable=self.password)
        self.e2.place(x=280, y=6,width=100,height=25)
        #save button
        save = Button(f1, text = 'Add',bg='#FFA500',activebackground='black',font=("Times",10,"bold"),command=lambda:[self.Add()])
        save.place(x=400, y=6,width=100,height=25)

        
       

        #frame 2 button delete update login 
        delb = Button(self.root, text = 'Delete',bg='#FFA500',activebackground='black',font=("Times",10,"bold"),command=lambda:[self.delete()])
        delb.place(x=420, y=120,width=120,height=30)
        # upd = Button(self.root, text = 'Update',bg='#FFA500',activebackground='black',font=("Times",10,"bold"),command=lambda:[self.update()])
        # upd.place(x=420, y=170,width=120,height=30)
        login = Button(self.root, text = 'LOGIN',bg='#FFA500',activebackground='black',font=("Times",10,"bold"),command=lambda:[self.getrow(),self.book()])
        login.place(x=420, y=220,width=120,height=30)

        cols=("No.","username","password")
        self.listbox=ttk.Treeview(self.root,columns=cols,show='headings')
<<<<<<< HEAD
=======
=======
        self.e1.place(x=180, y=10,width=200,height=30)
        #password entry
        self.e2=Entry(f1,font=("Times",12,"bold"),textvariable=self.password)
        self.e2.place(x=490, y=10,width=200,height=30)
        #save button
        save = Button(f1, text = 'Add',bg='#FFA500',activebackground='black',font=("Times",10,"bold"),command=lambda:[self.Add()])
        save.place(x=330, y=120,width=200,height=30)

        
        # frame 2 for list view for login data
        f2=Frame(page1,bg='sky blue')
        f2.place(x=250,y=220,width=740,height=330)

        #frame 2 button delete update login 
        delb = Button(f2, text = 'Delete',bg='#FFA500',activebackground='black',font=("Times",10,"bold"),command=lambda:[self.delete()])
        delb.place(x=530, y=80,width=150,height=30)
        upd = Button(f2, text = 'Update',bg='#FFA500',activebackground='black',font=("Times",10,"bold"),command=lambda:[self.update()])
        upd.place(x=530, y=140,width=150,height=30)
        login = Button(f2, text = 'LOGIN',bg='#FFA500',activebackground='black',font=("Times",10,"bold"),command=lambda:[self.getrow(),self.book()])
        login.place(x=530, y=200,width=150,height=30)

        cols=("No.","username","password")
        self.listbox=ttk.Treeview(f2,columns=cols,show='headings')
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        self.listbox.column('username', anchor=CENTER, width=50)
        self.listbox.column('password', anchor=CENTER, width=50)
        self.listbox.column('No.', anchor=CENTER, width=20)
        for col in cols:
            self.listbox.heading(col, text=col)
<<<<<<< HEAD
            self.listbox.place(x=10,y=65)
            self.listbox.place(width=400,height=220)
=======
<<<<<<< HEAD
            self.listbox.place(x=10,y=65)
            self.listbox.place(width=400,height=220)
=======
            self.listbox.grid(row=0,column=0,columnspan=1)
            self.listbox.place(width=500,height=330)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        
        self.show()
        
        

    
        def GetValue(event):
            
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            
            row_id=self.listbox.selection()[0]
            select=self.listbox.set(row_id)
            print(select)
            self.e1.insert(0,select['username'])
            self.e2.insert(0,select['password'])
        self.listbox.bind("<Button-1>",GetValue)
        
        
    
    def Add(self):
        #print(self.username)
        self.username = self.e1.get()
        self.password = self.e2.get()
        # name=temp_entry.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            sql = "INSERT INTO  login (username,password) VALUES ( %s,%s)"
            val = (self.username,self.password)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "agent id inserted successfully...launch app again to watch")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            
            self.e1.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
        
    # show user and pass in list
    def show(self):
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,username,password FROM login")
        records = mycursor.fetchall()
        print(records)
        
        for i, (id,username,password) in enumerate(records, start=1):
            self.listbox.insert("", "end", values=(id,username,password))
            
            mysqldb.close()
       
    #function for get username and password from entry
    
        
    def delete(self):
        self.username = self.e1.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
        try:
            sql = "delete from login where username = %s"
            val = (self.username,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record Deleteeeee successfully...")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e1.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    
    def update(self):
        self.username = self.e1.get()
        self.password = self.e2.get()
        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            sql = "Update login set username= %s , password= %s where username =%s"

            val = (self.username,self.password,self.username)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record Updateddddd successfully...")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e1.focus_set()
    
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def getrow(self):
        # global user1,user2,user3,user4,user5
        # global user1_pass,user2_pass,user3_pass,user4_pass,user5_pass
        row_id=self.listbox.selection()
        self.user_list=[]
        self.pass_list=[]
        for item in row_id:
            c1=self.listbox.item(item)
            login_users=c1.get("values") 
            self.user_list.append(login_users[1]) 
            self.pass_list.append(login_users[2]) 

        try:
            self.user1=self.user_list[0]
            self.user1_pass=self.pass_list[0]
            print(self.user1)
        except:
            print("not select user 1")

        try:
            self.user2=self.user_list[1]
            self.user2_pass=self.pass_list[1]
            print(self.user2)
        except:
            print("not select user 2")
        try:
            self.user3=self.user_list[2]
            self.user3_pass=self.pass_list[2]
            print(self.user3)
        except:
            print("not select user 3")
        try:
            self.user4=self.user_list[3]
            self.user4_pass=self.pass_list[3]
            print(self.user4)
        except:
            print("not select user 4")
        try:
            self.user5=self.user_list[4]
            self.user5_pass=self.pass_list[4]
            print(self.user5)
        except:
            print("not select user 5")

        return self.user_list


    def book(self):
        print('book')
        
        if passanger_value['qouta']=='TATKAL':
            print(passanger_value)
            thread1=multiprocessing.Process(target=start1,args=(self.user1,self.user1_pass,passanger_value,upi_value,method_pay,debit_value))
            thread2=multiprocessing.Process(target=start2,args=(self.user2,self.user2_pass,passanger_value,upi_value,method_pay,debit_value))
            # thread3=multiprocessing.Process(target=start3,args=(self.user3,self.user3_pass,passanger_value,upi_value,method_pay,debit_value))
            # thread4=multiprocessing.Process(target=start4,args=(self.user4,self.user4_pass,passanger_value,upi_value,method_pay,debit_value))
            # thread5=multiprocessing.Process(target=start5,args=(self.user5,self.user5_pass,passanger_value,upi_value,method_pay,debit_value))
            thread1.start()
            thread2.start()
            # thread3.start()
            # thread4.start()
            # thread5.start()

            thread1.join()
            thread2.join()  
            # thread3.join()  
            # thread4.join()
            # thread5.join()


        
        elif passanger_value['qouta']=='GENERAL':
            start1(self.user1,self.user1_pass,passanger_value,upi_value,method_pay,debit_value)

    
    
     

        