from libraries import *
from _main import *
from login import *

class Keys_screen:
    def __init__(self,root,login):
        self.root = root
        self.login=login
       

    def key_screen(self):
        
        keyframe=Frame(self.root,bg="white")
        keyframe.place(x=400,y=200,width=400,height=200)
        keylabel=Label(keyframe,text='Enter Key ',bg='white',font= ("Courier", 10))
        keylabel.place(x=0,y=60)
        
        keyentry=Entry(keyframe,bd=2,font= ("Courier", 12))
        keyentry.place(x=150,y=60,width=150,height=25)
        keysubmit=Button(keyframe,text="Submit",font= ("Courier", 12),bg='sky blue',activebackground="black"
        ,activeforeground='sky blue', relief="ridge",command=lambda:submitkey(self))
        keysubmit.place(x=150,y=100,width=90,height=30)

        def submitkey(self):
            k1='sarb'
            if keyentry.get()==k1:
                print('login success')
                
                self.login.login_screen()
            else:
                print('key error')
            
            L_key=keyentry.get()
            print(L_key)
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()

            try:
                # mycursor.execute('''create table if not exists licence_key(id int(15) auto_increment,L_key text, primary key(id))''')
                sql = "INSERT INTO  licence_key (ID,L_KEY) VALUES (%s,%s)"
                val = (0,L_key)
                mycursor.execute(sql, val)
                mysqldb.commit()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()