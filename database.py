from tkinter import *
def data():
    global v1,v2
    
    # v1=StringVar()
    # v2=StringVar()
    
    # v1=e1
    # v2=e2
    
    # print(e1)
    # print(e2)
    
    e1=input('enter the usernam')
    e2=input('password')
    print(e1)
    print(e2)
    #database connection
    import mysql.connector
    connection=mysql.connector.connect(host='localhost',username='root',password='deol9646')
    cursor=connection.cursor()
    print('successfully connected')

    #cursor.execute('''create table if not exists login(username text ,password text)''')

    # cursor.execute('''INSERT INTO LOGIN(USERNAME, PASSWORD) 
    # VALUES (%s ,%s)''',(v1, v2))
    connection.commit()
    try:  
    #creating a new database  
        cursor.execute("create database train_login")  
        print('created')
        #getting the list of all the databases which will now include the new database PythonDB  
        dbs = cursor.execute("show databases")  
        
    except:  
        connection.rollback()
        print('rollback') 
    for x in cursor:  
        print(x)
data()