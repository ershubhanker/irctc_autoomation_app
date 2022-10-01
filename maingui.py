from tkinter import *
import tkinter as tk
from turtle import heading, width 
from PIL import Image, ImageTk
from tkinter.messagebox import askyesno
from tkinter import font  as tkfont

#----window----
root = tk.Tk()
root.configure(bg='sky blue')
root.title("IRCTC")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("900x600+200+50")
#root.resizable(False,False)



page1=Frame(root,bg='sky blue')
page2=Frame(root,bg='sky blue')
page3=Frame(root)
page4=Frame(root)

for frame in (page1,page2,page3,page4):
    frame.grid(row=0, column=0, sticky='nsew') 

def show_frame(frame):
    frame.tkraise()
show_frame(page1)

def one():
#---Page-------
    label1=tk.Label(page1,text='first page',font=('orbitron',45,'bold'),background='#3d3d5c')
    label1.place(x=10,y=565,width=324,height=30)
    Button1=tk.Button(label1,text='first page',command=lambda:show_frame(page1))
    Button1.grid(row=10,column=1)
    Button2=tk.Button(label1,text='IDS page',command=lambda:show_frame(page2))
    Button2.grid(row=10,column=2)
    Button3=tk.Button(label1,text='PASSSENGER page',command=lambda:show_frame(page3))
    Button3.grid(row=10,column=3)
    Button3=tk.Button(label1,text='PAYMENT page',command=lambda:show_frame(page4))
    Button3.grid(row=10,column=4)
one()
def two():
    #---Page-------
    
    #font
    font1=tkfont.Font(family='Times', size=15, weight="bold")

    #frames
    f1=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=1)
    f1.place(x=10,y=20,width=880,height=200)



    #labels
    label1=Label(page2,text='IRCTC ID',bg='sky blue',font=font1)
    label1.place(x=17, y=17)
    label2=Label(f1,text='Irstc ID :',bg='sky blue',font=("Times",12,"bold"))
    label2.place(x=100, y=10)
    label3=Label(f1,text='Password :',bg='sky blue',font=("Times",12,"bold"))
    label3.place(x=400, y=10)

    #entry
    username = StringVar()
    e1=Entry(f1,font=("Times",12,"bold"),textvariable=username).place(x=180, y=10,width=200,height=30)
    password = StringVar()
    e2=Entry(f1,font=("Times",12,"bold"),textvariable=password).place(x=490, y=10,width=200,height=30)

    #save button
    save = Button(f1, text = 'Save',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : askyesno('Confirm', 'Do you want to save?'))
    save.place(x=330, y=70,width=200,height=30)
    
    #frame 2 data show
    
    f2=Frame(page2)
    f2.place(x=165,y=220,width=580,height=340)
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

    #Bottom buttons
    label1=tk.Label(page2,text='first page',font=('orbitron',45,'bold'),background='#3d3d5c')
    label1.place(x=10,y=565,width=324,height=30)
    Button1=tk.Button(label1,text='first page',command=lambda:show_frame(page1))
    Button1.grid(row=10,column=1)
    Button2=tk.Button(label1,text='IDS page',command=lambda:show_frame(page2))
    Button2.grid(row=10,column=2)
    Button3=tk.Button(label1,text='PASSSENGER page',command=lambda:show_frame(page3))
    Button3.grid(row=10,column=3)
    Button3=tk.Button(label1,text='PAYMENT page',command=lambda:show_frame(page4))
    Button3.grid(row=10,column=4)
one()
two()
def three():
    #---Page-------
    label2=tk.Label(page3,text='3 page',font=('orbitron',45,'bold'),foreground='#ffffff',background='#3d3d5c')
    label2.pack(pady=25)
    Button1=tk.Button(page3,text='first page',command=lambda:show_frame(page1))
    Button1.pack(pady=25)
    Button2=tk.Button(page3,text='IDS page',command=lambda:show_frame(page2))
    Button2.pack(pady=25)
    Button3=tk.Button(page3,text='PASSSENGER page',command=lambda:show_frame(page3))
    Button3.pack(pady=25)
    Button3=tk.Button(page3,text='PAYMENT page',command=lambda:show_frame(page4))
    Button3.pack(pady=25)
three()
def fourth():
    #---Page-------
    label2=tk.Label(page4,text='4 page',font=('orbitron',45,'bold'),foreground='#ffffff',background='#3d3d5c')
    label2.pack(pady=25)
fourth()
    



root.mainloop()