from tkinter import font  as tkfont
from tkinter import  *
from tkinter import ttk,messagebox
import mysql.connector
connection=mysql.connector.connect(host='localhost',username='root',password='deol9646',database="train_login")
from tkcalendar import DateEntry
import extra.login as login



def passanger_f(page2):
    #
    font1=tkfont.Font(family='Helvetica', size=10, weight="bold")
    #frames
    pf1=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
    pf1.place(x=0,y=0,width=350,height=500)

    l1=Label(pf1,text='Train Details',bg='light gray',foreground='white',font=font1)
    l1.place(x=0,y=0,width=336,height=40)
    #from label & entry
    from_label=Label(pf1,text='From :',bg='sky blue',font=font1)
    from_label.place(x=10,y=60,width=50,height=25)
    from_entry=Entry(pf1)
    from_entry.place(x=120,y=60,width=200,height=25)

    #To label & entry
    to_label=Label(pf1,text='To :',bg='sky blue',font=font1)
    to_label.place(x=10,y=100,width=30,height=25)
    to_entry=Entry(pf1)
    to_entry.place(x=120,y=100,width=200,height=25)

    #journey date label & entry
    to_label=Label(pf1,text='Journey Date :',bg='sky blue',font=font1)
    to_label.place(x=10,y=140,width=100,height=25)
    to_entry=DateEntry(pf1,selectmode='day',date_pattern='dd/MM/yyyy')
    to_entry.place(x=222,y=140,width=100,height=25)

    #Class label & entry
    class_label=Label(pf1,text='Class :',bg='sky blue',font=font1)
    class_label.place(x=10,y=180,width=50,height=25)
        # Dropdown class options
    class_opt = [
        "All Classes",
        "AC First Class",
        "Second Sitting 2S"
    ] 
        # Create Dropdown menu
    class_entry = ttk.Combobox(state="readonly",values=class_opt) #readonly
    class_entry.place(x=130,y=190,width=200,height=25)
    class_entry.current(0)

    #Quta label & entry
    Quta_label=Label(pf1,text='Quta :',bg='sky blue',font=font1)
    Quta_label.place(x=10,y=220,width=50,height=25)
        # Dropdown Quta options
    Quta_opt = [
        "Tatkal",
        
    ] 
        # Create Dropdown menu
    Quta_entry = ttk.Combobox(state="disabled",values=Quta_opt) #readonly
    Quta_entry.place(x=130,y=230,width=200,height=25)
    Quta_entry.current(0)

    #Train_no label & entry
    Train_no_label=Label(pf1,text='Train_no :',bg='sky blue',font=font1)
    Train_no_label.place(x=10,y=260,width=70,height=25)
    Train_no_entry=Entry(pf1)
    Train_no_entry.place(x=120,y=260,width=200,height=25)

    #Board label & entry
    Board_label=Label(pf1,text='Board :',bg='sky blue',font=font1)
    Board_label.place(x=10,y=300,width=50,height=25)
    Board_entry=Entry(pf1)
    Board_entry.place(x=120,y=300,width=200,height=25)

    #search button
    
    search_b = Button(pf1, text = 'Fill Passanger detail',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : login.start())
    search_b.place(x=120, y=3400,width=150,height=30)
    #frame2 passanger detail
    pf2=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
    pf2.place(x=350,y=0,width=850,height=500)

    l2=Label(pf2,text='Enter Passenger Details',bg='light gray',foreground='white',font=font1)
    l2.place(x=0,y=0,width=835,height=40)


    #Column labels 
    label1=Label(pf2,text='Passenger Name',bg='sky blue',font=font1)
    label1.place(x=20,y=60,width=120,height=25)
    p1=Entry(pf2)
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
    a1=Entry(pf2)
    a1.place(x=165,y=90,width=30,height=25)

    a2=Entry(pf2)
    a2.place(x=165,y=120,width=30,height=25)

    a3=Entry(pf2)
    a3.place(x=165,y=150,width=30,height=25)
    a4=Entry(pf2)
    a4.place(x=165,y=180,width=30,height=25)
    #Gender
    label3=Label(pf2,text='Gender',bg='sky blue',font=font1)
    label3.place(x=213,y=60,width=60,height=25)
    gender = [
        "M",
        "F",
    ] 
    # Create Dropdown menu
    g1 = ttk.Combobox(pf2,state="readonly",values=gender) #readonly
    g1.place(x=220,y=90,width=40,height=25)
    g1.current(0)

    g2 = ttk.Combobox(pf2,state="readonly",values=gender) #readonly
    g2.place(x=220,y=120,width=40,height=25)
    g2.current(0)

    g3 = ttk.Combobox(pf2,state="readonly",values=gender) #readonly
    g3.place(x=220,y=150,width=40,height=25)
    g3.current(0)

    g4 = ttk.Combobox(pf2,state="readonly",values=gender) #readonly
    g4.place(x=220,y=180,width=40,height=25)
    g4.current(0)


    #berth
    label4=Label(pf2,text='Berth',bg='sky blue',font=font1)
    label4.place(x=277,y=150,width=80,height=25)
    berth = [
        "No Choice",
        " ",
    ] 
        # Create Dropdown menu
    b1 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
    b1.place(x=275,y=90,width=100,height=25)
    b1.current(0)

    b2 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
    b2.place(x=275,y=120,width=100,height=25)
    b2.current(0)

    b3 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
    b3.place(x=275,y=150,width=100,height=25)
    b3.current(0)

    b4 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
    b4.place(x=275,y=180,width=100,height=25)
    b4.current(0)

    #food
    label5=Label(pf2,text='Food',bg='sky blue',font=font1)
    label5.place(x=345,y=60,width=120,height=25)
    food = [
        "Veg",
        "Non-Veg",
    ] 
        # Create Dropdown menu
    food1 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
    food1.place(x=385,y=90,width=60,height=25)
    food1.current(0)

    food2 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
    food2.place(x=385,y=120,width=60,height=25)
    food2.current(0)
    f3 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
    f3.place(x=385,y=150,width=60,height=25)
    f3.current(0)

    f4 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
    f4.place(x=385,y=180,width=60,height=25)
    f4.current(0)

    #Nationality
    label6=Label(pf2,text='Nationality',bg='sky blue',font=font1)
    label6.place(x=455,y=60,width=100,height=25)
    Nationality = [
        "India",
        "Foreigner",
    ] 
        # Create Dropdown menu
    n1 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
    n1.place(x=460,y=90,width=100,height=25)
    n1.current(0)

    n2 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
    n2.place(x=460,y=120,width=100,height=25)
    n2.current(0)

    n3 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
    n3.place(x=460,y=150,width=100,height=25)
    n3.current(0)

    n4 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
    n4.place(x=460,y=180,width=100,height=25)
    n4.current(0)

    #label3 bank details
    l2=Label(pf2,text='Enter Bank & Other Details',bg='light gray',foreground='white',font=font1)
    l2.place(x=0,y=260,width=835,height=40)
    
    
#three()