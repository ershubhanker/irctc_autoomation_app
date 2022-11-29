from libraries import  *
from login import *
from passanger import *
from payment import *
from tickets import *
from key_screen import *

mysqldb=mysql.connector.connect(host='localhost',username='root',password='deol9646',database="train_login")
#database connect
mycursor = mysqldb.cursor()
#create database
mycursor.execute('''create database if not exists train_login''')
# create login table
mycursor.execute('''create table if not exists login(id int(15) auto_increment,username text ,password text ,primary key(id))''')

mycursor.execute('''create table if not exists tatkal_data(name text ,age text ,gender text ,
                ifrom text ,ito text ,date text ,qouta text, counter_tatkal text,total text )''')


mycursor.execute('''create table if not exists debit_data(bank_name text,card_type text,card_number text,
                validity_m text,validity_y text,holder text,cvv text,pass3d text)''')

mycursor.execute('''create table if not exists upi_data(id int(15) auto_increment ,upi text,primary key(id))''')

mycursor.execute('''create table if not exists licence_key(id int(15) auto_increment,L_key text, primary key(id))''')
# Bottom keys
def navigate():
    global keys
    login = Login_screen(root)
   
    passanger=Passanger_screen(root,passanger_value)
    payment=Payment_screen(root,upi_value,debit_value,method_pay)
    tickets=Tickets_screen(root,passanger_value)
    
    Button1=Button(root,text='LOGIN',command=lambda:login.login_screen())
    Button1.place(x=10,y=570)
    Button2=Button(root,text='PASSSENGER',command=lambda:passanger.passanger_screen())
    Button2.place(x=65,y=570)
    Button3=Button(root,text='PAYMENT',command=lambda:payment.payment_screen())
    Button3.place(x=155,y=570)
    Button3=Button(root,text='TICKETS',command=lambda:tickets.tickets_screen())
    Button3.place(x=230,y=570)

    

if __name__ == "__main__":
    # ----root window----
    
    root = Tk()
    root.configure(bg='sky blue')
    root.title("IRCTC")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.geometry("1200x600+200+50")
    icon=PhotoImage(file='icon.png')
    root.iconphoto(False,icon)

    mycursor.execute('''create table if not exists licence_key(id int(15) auto_increment,L_key text, primary key(id))''')
    query="SELECT L_key FROM licence_key" 
    mycursor.execute(query)
    rows=mycursor.fetchall()
    for row in rows:
        print('data',row[0])
    try:
        if row[0] =="sarb":
            print('log in ')
            navigate()
    except:
        print('not found')
        
        l1 = Login_screen(root)
        
        keys= Keys_screen(root,l1)
        keys.key_screen()

    navigate()
    

    
    
        
    root.mainloop()

    