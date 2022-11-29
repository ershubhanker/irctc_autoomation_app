from libraries import *
from _main import *

mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
mycursor = mysqldb.cursor()

class Tickets_screen:
    def __init__(self,root,passanger_value):
        self.root = root
        self.passanger_value=passanger_value

    def tickets_screen(self):
        self.root.title("Total Tickets")
        page4=Frame(self.root,bg='sky blue', width=1200, height=550)
        page4.place(x=0,y=0)
        font1=tkfont.Font(family='Times', size=20, weight="bold")
        t1=Label(page4,text="SAVE TICKETS",font=font1,bg='sky blue',fg='grey',bd=10)
        t1.place(x=500,y=100,width=200,height=40)
        #frame 1 
        f1=Frame(page4 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=1)
        f1.place(x=220,y=150,width=780,height=300)
        def get1(event):
            row_id1=listbox.selection()[0]
            select=listbox.set(row_id1)
            print(select["SLOT"])
            mycursor.execute(f"SELECT name,ifrom,ito,age,gender,date,qouta,counter_tatkal,total FROM tatkal_data where counter_tatkal={select['SLOT']}")
            self.value = mycursor.fetchall()
            print(self.value[0])
            try:
                self.name1=self.value[0][0]
                print('name',self.name1)
                self.passanger_value["name"] = self.name1
            except:
                print('name1 not defind')
            try:
                self.name2=self.value[1][0]
                print('name 2',self.name2)
                self.passanger_value["name2"] = self.name2
            except:
                print('name2 not defind')
            try:
                self.name3=self.value[2][0]
                self.passanger_value["name3"] = self.name3
                print('name 3',self.name3)
            except:
                print('name3 not defind')
            try:    
                self.name4=self.value[3][0]
                self.passanger_value["name4"] = self.name4
                print('name',self.name4)
            except:
                print('name4 not defind')
            try:
                self.name5=self.value[4][0]
                self.passanger_value["name5"] = self.name5
                print('name 5',self.name5)
            except:
                print('name5 not defind')
            try:
                self.name6=self.value[5][0]
                self.passanger_value["name6"] = self.name6
                print('name',self.name6)
                
            except Exception as e:
                print(e)
            
            try:
                self.age1=self.value[0][3]
                self.passanger_value["age"] = self.age1
                print('age',self.age1)
            except:
                print('age 1 not defined')
            try:
                self.age2=self.value[1][3]
                self.passanger_value["age2"] = self.age2
                print('age',self.age2)
            except:
                print('age 2 not defined')
            try:
                self.age3=self.value[2][3]
                self.passanger_value["age3"] = self.age3
                print('age',self.age3)
            except:
                print('age 3 not defined')
            try:
                self.age4=self.value[3][3]
                self.passanger_value["age4"] = self.age4
                print('age',self.age4)
            except:
                print('age 4 not defined')
            try:
                self.age5=self.value[4][3]
                self.passanger_value["age5"] = self.age5
                print('age',self.age5)
            except:
                print('age 5 not defined')
            try:
                self.age6=self.value[5][3]
                self.passanger_value["age6"] = self.age6
                print('age',self.age6)
            except:
                print('age 6 not defined')
            

            try:
                self.gender1=self.value[0][4]
                self.passanger_value["gender"] = self.gender1
                # gender2=self.value[1][4]
                # gender3=self.value[2][4]
                # gender4=self.value[3][4]
                # gender5=self.value[4][4]
                # gender6=self.value[5][4]
                print('gender',self.gender1)
            except Exception as e:
                print(e)

            self.date=self.value[0][5]
            print(self.date)
            self.ifrom=self.value[0][1]
            self.ito=self.value[0][2]
            print('from',self.ifrom)
            print('to',self.ito)
            self.qouta=self.value[0][6]
            print('qouta',self.qouta)
            self.count=self.value[0][8]

            self.passanger_value["ifrom"] = self.ifrom
            self.passanger_value["ito"] = self.ito
            self.passanger_value["date"] = self.date
            self.passanger_value["total"]=self.count
            self.passanger_value["qouta"]=self.qouta
            print(self.passanger_value)
        #labels
        cols=("SLOT","FROM","TO","DATE","QOUTA","TOTAL TICKETS")
        listbox=ttk.Treeview(f1,columns=cols,show='headings')
        listbox.column('FROM', anchor=CENTER, width=50,)
        listbox.column('TO', anchor=CENTER, width=50)
        listbox.column('DATE', anchor=CENTER, width=50)
        listbox.column('QOUTA', anchor=CENTER, width=50)
        listbox.column('SLOT', anchor=CENTER, width=50)
        listbox.column('TOTAL TICKETS', anchor=CENTER, width=50)
        for col in cols:
            listbox.heading(col, text=col)
            listbox.place(width=770,height=290)
        
        def show1():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT counter_tatkal,ifrom,ito,date,qouta,Count(*) FROM train_login.tatkal_data group by counter_tatkal Having Count(*) >0")
            record = mycursor.fetchall()
            print(self.passanger_value)
            
            for i, (counter_tatkal,ifrom,ito,date,qouta,count) in enumerate(record, start=1):
                listbox.insert("", "end", values=(counter_tatkal,ifrom,ito,date,qouta,count))
                
                mysqldb.close()
        show1()
        
        
        listbox.bind("<Double-Button-1>",get1)
