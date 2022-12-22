from libraries import *
from _main import *
<<<<<<< HEAD
from ttkwidgets.autocomplete import AutocompleteCombobox
=======
<<<<<<< HEAD
from ttkwidgets.autocomplete import AutocompleteCombobox
=======

>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8

class Passanger_screen:
    def __init__(self,root,passanger_value):
        
        self.root = root
        self.passanger_value=passanger_value
    
        # self.qouta=''
        
    def passanger_screen(self):
        
<<<<<<< HEAD
        page2=Frame(self.root,bg='sky blue', width=700, height=290)
=======
<<<<<<< HEAD
        page2=Frame(self.root,bg='sky blue', width=700, height=290)
=======
        page2=Frame(self.root,bg='sky blue', width=1200, height=550)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        page2.place(x=0,y=0)
        font1=tkfont.Font(family='Helvetica', size=10, weight="bold")
        #frames
        pf1=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        pf1.place(x=0,y=0,width=165,height=290)

        l1=Label(pf1,text='Train Details',bg='light gray',foreground='white',font=font1)
        l1.place(x=0,y=0,width=150,height=30)
<<<<<<< HEAD
=======
=======
        pf1.place(x=0,y=0,width=350,height=500)

        l1=Label(pf1,text='Train Details',bg='light gray',foreground='white',font=font1)
        l1.place(x=0,y=0,width=336,height=40)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8

        p_from = StringVar()
        p_to = StringVar()
        p_date = StringVar()
        p_name = StringVar()
        p2_name = StringVar()
        p3_name = StringVar()
        p4_name = StringVar()
        p5_name = StringVar()
        p6_name = StringVar()

        p_age = StringVar()
        p2_age = StringVar()
        p3_age = StringVar()
        p4_age = StringVar()
        p5_age = StringVar()
        p6_age = StringVar()

        p_gender = StringVar()
        p2_gender = StringVar()
        p3_gender = StringVar()
        p4_gender = StringVar()
        p5_gender = StringVar()
        p6_gender = StringVar()

        p_count = StringVar()
        q_data = StringVar()
    



        p_from.set(self.passanger_value["ifrom"])
        p_to.set(self.passanger_value["ito"])
        p_date.set(self.passanger_value["date"])

        p_name.set(self.passanger_value["name"])
        p2_name.set(self.passanger_value["name2"])
        p3_name.set(self.passanger_value["name3"])
        p4_name.set(self.passanger_value["name4"])
        p5_name.set(self.passanger_value["name5"])
        p6_name.set(self.passanger_value["name6"])

        p_age.set(self.passanger_value["age"])
        p2_age.set(self.passanger_value["age2"])
        p3_age.set(self.passanger_value["age3"])
        p4_age.set(self.passanger_value["age4"])
        p5_age.set(self.passanger_value["age5"])
        p6_age.set(self.passanger_value["age6"])
    
        p_gender.set(self.passanger_value["gender"])
        p2_gender.set(self.passanger_value["gender2"])
        p3_gender.set(self.passanger_value["gender3"])
        p4_gender.set(self.passanger_value["gender4"])
        p5_gender.set(self.passanger_value["gender5"])
        p6_gender.set(self.passanger_value["gender6"])

        p_count.set(self.passanger_value["total"])
        q_data.set(self.passanger_value["qouta"])
        
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        # countries = [
        # 'Antigua and Barbuda', 'Bahamas','Barbados','Belize', 'Canada',
        # 'Costa Rica ', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador ',
        # 'Grenada', 'Guatemala ', 'Haiti', 'Honduras ', 'Jamaica', 'Mexico',
        # 'Nicaragua', 'Saint Kitts and Nevis', 'Panama ', 'Saint Lucia', 
        # 'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States of America'
        # ]
        # completevalues=countries
        #from label & entry
        from_label=Label(pf1,text='From :',bg='sky blue',font=font1)
        from_label.place(x=1,y=35,width=50,height=25)
        self.from_entry=Entry(pf1,textvariable=p_from)
        self.from_entry.place(x=50,y=35,width=100,height=25)
        
        #To label & entry
        to_label=Label(pf1,text='To :',bg='sky blue',font=font1)
        to_label.place(x=1,y=70,width=60,height=25)
        self.to_entry=Entry(pf1,textvariable=p_to)
        self.to_entry.place(x=50,y=70,width=100,height=25)

        #journey date label & entry
        date_label=Label(pf1,text='Date :',bg='sky blue',font=font1)
        date_label.place(x=1,y=105,width=50,height=25)
        self.date_entry=DateEntry(pf1,selectmode='day',date_pattern='dd/MM/yyyy',textvariable=p_date)
        self.date_entry.place(x=70,y=105,width=80,height=25)
    
        #Class label & entry
        class_label=Label(pf1,text='Class :',bg='sky blue',font=font1)
        class_label.place(x=1,y=145,width=50,height=25)
<<<<<<< HEAD
=======
=======

        #from label & entry
        from_label=Label(pf1,text='From :',bg='sky blue',font=font1)
        from_label.place(x=10,y=60,width=50,height=25)
        self.from_entry=Entry(pf1,textvariable=p_from)
        self.from_entry.place(x=120,y=60,width=200,height=25)
        
        #To label & entry
        to_label=Label(pf1,text='To :',bg='sky blue',font=font1)
        to_label.place(x=10,y=100,width=30,height=25)
        self.to_entry=Entry(pf1,textvariable=p_to)
        self.to_entry.place(x=120,y=100,width=200,height=25)

        #journey date label & entry
        date_label=Label(pf1,text='Journey Date :',bg='sky blue',font=font1)
        date_label.place(x=10,y=140,width=100,height=25)
        self.date_entry=DateEntry(pf1,selectmode='day',date_pattern='dd/MM/yyyy',textvariable=p_date)
        self.date_entry.place(x=222,y=140,width=100,height=25)
    
        #Class label & entry
        class_label=Label(pf1,text='Class :',bg='sky blue',font=font1)
        class_label.place(x=10,y=180,width=50,height=25)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
            # Dropdown class options
        class_opt = [
            "All Classes",
            "AC First Class",
            "Second Sitting 2S"
        ] 
            # Create Dropdown menu
        self.class_entry = ttk.Combobox(state="readonly",values=class_opt) #readonly
<<<<<<< HEAD
        self.class_entry.place(x=58,y=150,width=100,height=25)
=======
<<<<<<< HEAD
        self.class_entry.place(x=58,y=150,width=100,height=25)
=======
        self.class_entry.place(x=130,y=190,width=200,height=25)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        self.class_entry.current(0)

        #Quta label & entry
        Quta_label=Label(pf1,text='Quta :',bg='sky blue',font=font1)
<<<<<<< HEAD
        Quta_label.place(x=1,y=180,width=50,height=25)
=======
<<<<<<< HEAD
        Quta_label.place(x=1,y=180,width=50,height=25)
=======
        Quta_label.place(x=10,y=220,width=50,height=25)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
            # Dropdown Quta options
        Quta_opt = [
            "GENERAL",
            "LADIES",
            "LOWER BERTH/SR.CITIZEN",
            "TATKAL",
            "PREMIUM TATKAL"
        ] 
            # Create Dropdown menu
        self.Quta_entry = ttk.Combobox(state="readonly",values=Quta_opt,textvariable=q_data) #disabled
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        self.Quta_entry.place(x=58,y=185,width=100,height=25)
        self.Quta_entry.current(0)

        #Train_no label & entry
        Train_no_label=Label(pf1,text='T_no :',bg='sky blue',font=font1)
        Train_no_label.place(x=1,y=210,width=50,height=25)
        self.Train_no_entry=Entry(pf1)
        self.Train_no_entry.place(x=78,y=210,width=70,height=25)

        # #Board label & entry
        # Board_label=Label(pf1,text='Board :',bg='sky blue',font=font1)
        # Board_label.place(x=1,y=240,width=50,height=25)
        # self.Board_entry=Entry(pf1)
        # self.Board_entry.place(x=55,y=240,width=50,height=25)
        #label for num of passangers
        p_count=Label(pf1,text='P_count :',bg='sky blue',font=font1)
        p_count.place(x=1,y=240,width=65,height=25)
<<<<<<< HEAD
=======
=======
        self.Quta_entry.place(x=130,y=230,width=200,height=25)
        self.Quta_entry.current(0)

        #Train_no label & entry
        Train_no_label=Label(pf1,text='Train_no :',bg='sky blue',font=font1)
        Train_no_label.place(x=10,y=260,width=70,height=25)
        self.Train_no_entry=Entry(pf1)
        self.Train_no_entry.place(x=120,y=260,width=200,height=25)

        #Board label & entry
        Board_label=Label(pf1,text='Board :',bg='sky blue',font=font1)
        Board_label.place(x=10,y=300,width=50,height=25)
        self.Board_entry=Entry(pf1)
        self.Board_entry.place(x=120,y=300,width=200,height=25)

        #search button
        def go():
            messagebox.showinfo("information", "passanger data inserted successfully...")
            self.passanger_screen()
            
        search_b = Button(pf1, text = 'save',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda :[self.pass_add(),go()])
        search_b.place(x=120, y=340,width=150,height=30)

        #frame2 passanger detail
        pf2=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
        pf2.place(x=350,y=0,width=850,height=500)

        l2=Label(pf2,text='Enter Passenger Details',bg='light gray',foreground='white',font=font1)
        l2.place(x=0,y=0,width=835,height=40)


        #Column labels 
        label1=Label(pf2,text='Passenger Name',bg='sky blue',font=font1)
        label1.place(x=20,y=60,width=120,height=25)
        self.p1=Entry(pf2,textvariable=p_name)
        self.p1.place(x=10,y=90,width=140,height=25)

        self.p2=Entry(pf2,textvariable=p2_name)
        self.p2.place(x=10,y=120,width=140,height=25)

        self.p3=Entry(pf2,textvariable=p3_name)
        self.p3.place(x=10,y=150,width=140,height=25)

        self.p4=Entry(pf2,textvariable=p4_name)
        self.p4.place(x=10,y=180,width=140,height=25)

        self.p5=Entry(pf2,textvariable=p5_name)
        self.p5.place(x=10,y=210,width=140,height=25)

        self.p6=Entry(pf2,textvariable=p6_name)
        self.p6.place(x=10,y=240,width=140,height=25)

        #age
        label2=Label(pf2,text='Age',bg='sky blue',font=font1)
        label2.place(x=160,y=60,width=40,height=25)
        self.a1=Entry(pf2,textvariable=p_age)
        self.a1.place(x=165,y=90,width=30,height=25)

        self.a2=Entry(pf2,textvariable=p2_age)
        self.a2.place(x=165,y=120,width=30,height=25)

        self.a3=Entry(pf2,textvariable=p3_age)
        self.a3.place(x=165,y=150,width=30,height=25)

        self.a4=Entry(pf2,textvariable=p4_age)
        self.a4.place(x=165,y=180,width=30,height=25)

        self.a5=Entry(pf2,textvariable=p5_age)
        self.a5.place(x=165,y=210,width=30,height=25)

        self.a6=Entry(pf2,textvariable=p6_age)
        self.a6.place(x=165,y=240,width=30,height=25)
        #Gender
        label3=Label(pf2,text='Gender',bg='sky blue',font=font1)
        label3.place(x=213,y=60,width=60,height=25)
        gender = [
            "M",
            "F",
        ] 
        # Create Dropdown menu
        self.g1 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p_gender) #readonly
        self.g1.place(x=220,y=90,width=40,height=25)
        self.g1.current(0)

        self.g2 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p2_gender) #readonly
        self.g2.place(x=220,y=120,width=40,height=25)
        self.g2.current(0)

        self.g3 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p3_gender) #readonly
        self.g3.place(x=220,y=150,width=40,height=25)
        self.g3.current(0)

        self.g4 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p4_gender) #readonly
        self.g4.place(x=220,y=180,width=40,height=25)
        self.g4.current(0)

        self.g5 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p5_gender) #readonly
        self.g5.place(x=220,y=210,width=40,height=25)
        self.g5.current(0)

        self.g6 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p6_gender) #readonly
        self.g6.place(x=220,y=240,width=40,height=25)
        self.g6.current(0)


        #berth
        label4=Label(pf2,text='Berth',bg='sky blue',font=font1)
        label4.place(x=277,y=60,width=80,height=25)
        berth = [
            "No Choice",
            " ",
        ] 
            # Create Dropdown menu
        self.b1 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b1.place(x=275,y=90,width=100,height=25)
        self.b1.current(0)

        self.b2 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b2.place(x=275,y=120,width=100,height=25)
        self.b2.current(0)

        self.b3 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b3.place(x=275,y=150,width=100,height=25)
        self.b3.current(0)

        self.b4 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b4.place(x=275,y=180,width=100,height=25)
        self.b4.current(0)

        #food
        label5=Label(pf2,text='Food',bg='sky blue',font=font1)
        label5.place(x=345,y=60,width=120,height=25)
        food = [
            "Veg",
            "Non-Veg",
        ] 
            # Create Dropdown menu
        self.food1 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.food1.place(x=385,y=90,width=60,height=25)
        self.food1.current(0)

        self.food2 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.food2.place(x=385,y=120,width=60,height=25)
        self.food2.current(0)
        self.f3 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.f3.place(x=385,y=150,width=60,height=25)
        self.f3.current(0)

        self.f4 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.f4.place(x=385,y=180,width=60,height=25)
        self.f4.current(0)

        #Nationality
        label6=Label(pf2,text='Nationality',bg='sky blue',font=font1)
        label6.place(x=455,y=60,width=100,height=25)
        Nationality = [
            "India",
            "Foreigner",
        ] 
            # Create Dropdown menu
        self.n1 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n1.place(x=460,y=90,width=100,height=25)
        self.n1.current(0)

        self.n2 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n2.place(x=460,y=120,width=100,height=25)
        self.n2.current(0)

        self.n3 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n3.place(x=460,y=150,width=100,height=25)
        self.n3.current(0)

        self.n4 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n4.place(x=460,y=180,width=100,height=25)
        self.n4.current(0)

        
        
        #label for num of passangers
        p_count=Label(pf2,text='Total passanger',bg='sky blue',font=font1)
        p_count.place(x=10,y=270,width=120,height=25)
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        num_of_passanger = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6"
        ] 
            # Create Dropdown menu
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        self.c1 = ttk.Combobox(pf1,state="readonly",values=num_of_passanger,textvariable=p_count) #readonly
        self.c1.place(x=100,y=240,width=50,height=25)
        self.c1.current(0)
        #search button
        def go():
            messagebox.showinfo("information", "passanger data inserted successfully...")
            self.passanger_screen()
            
        

        #-----------------------frame2 passanger detail--------------------------------
        pf2=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
        pf2.place(x=165,y=0,width=410,height=290)

        l2=Label(pf2,text='Enter Passenger Details',bg='light gray',foreground='white',font=font1)
        l2.place(x=0,y=0,width=395,height=30)

    
        #Column labels 
        label1=Label(pf2,text='Name',bg='sky blue',font=font1)
        label1.place(x=10,y=40,width=70,height=25)
        self.p1=Entry(pf2,textvariable=p_name)
        self.p1.place(x=5,y=70,width=70,height=25)

        self.p2=Entry(pf2,textvariable=p2_name)
        self.p2.place(x=5,y=100,width=70,height=25)

        self.p3=Entry(pf2,textvariable=p3_name)
        self.p3.place(x=5,y=130,width=70,height=25)

        self.p4=Entry(pf2,textvariable=p4_name)
        self.p4.place(x=5,y=160,width=70,height=25)

        self.p5=Entry(pf2,textvariable=p5_name)
        self.p5.place(x=5,y=190,width=70,height=25)

        self.p6=Entry(pf2,textvariable=p6_name)
        self.p6.place(x=5,y=220,width=70,height=25)

        #age
        label2=Label(pf2,text='Age',bg='sky blue',font=font1)
        label2.place(x=85,y=40,width=30,height=25)
        self.a1=Entry(pf2,textvariable=p_age)
        self.a1.place(x=85,y=70,width=30,height=25)

        self.a2=Entry(pf2,textvariable=p2_age)
        self.a2.place(x=85,y=100,width=30,height=25)

        self.a3=Entry(pf2,textvariable=p3_age)
        self.a3.place(x=85,y=130,width=30,height=25)

        self.a4=Entry(pf2,textvariable=p4_age)
        self.a4.place(x=85,y=160,width=30,height=25)

        self.a5=Entry(pf2,textvariable=p5_age)
        self.a5.place(x=85,y=190,width=30,height=25)

        self.a6=Entry(pf2,textvariable=p6_age)
        self.a6.place(x=85,y=220,width=30,height=25)
        #Gender
        label3=Label(pf2,text='Gender',bg='sky blue',font=font1)
        label3.place(x=120,y=40,width=60,height=25)
        gender = [
            "M",
            "F",
        ] 
        # Create Dropdown menu
        self.g1 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p_gender) #readonly
        self.g1.place(x=125,y=70,width=35,height=25)
        self.g1.current(0)

        self.g2 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p2_gender) #readonly
        self.g2.place(x=125,y=100,width=35,height=25)
        self.g2.current(0)

        self.g3 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p3_gender) #readonly
        self.g3.place(x=125,y=135,width=35,height=25)
        self.g3.current(0)

        self.g4 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p4_gender) #readonly
        self.g4.place(x=125,y=160,width=35,height=25)
        self.g4.current(0)

        self.g5 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p5_gender) #readonly
        self.g5.place(x=125,y=190,width=35,height=25)
        self.g5.current(0)

        self.g6 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p6_gender) #readonly
        self.g6.place(x=125,y=220,width=35,height=25)
        self.g6.current(0)


        #berth
        label4=Label(pf2,text='Berth',bg='sky blue',font=font1)
        label4.place(x=180,y=40,width=40,height=25)
        berth = [
            "No Choice",
            " ",
        ] 
            # Create Dropdown menu
        self.b1 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b1.place(x=170,y=70,width=60,height=25)
        self.b1.current(0)

        self.b2 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b2.place(x=170,y=100,width=60,height=25)
        self.b2.current(0)

        self.b3 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b3.place(x=170,y=130,width=60,height=25)
        self.b3.current(0)

        self.b4 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b4.place(x=170,y=160,width=60,height=25)
        self.b4.current(0)

        self.b5 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b5.place(x=170,y=190,width=60,height=25)
        self.b5.current(0)

        self.b6 = ttk.Combobox(pf2,state="readonly",values=berth) #readonly
        self.b6.place(x=170,y=220,width=60,height=25)
        self.b6.current(0)

        #food
        label5=Label(pf2,text='Food',bg='sky blue',font=font1)
        label5.place(x=225,y=40,width=50,height=25)
        food = [
            "Veg",
            "N-Veg",
        ] 
            # Create Dropdown menu
        self.food1 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.food1.place(x=240,y=70,width=45,height=25)
        self.food1.current(0)

        self.food2 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.food2.place(x=240,y=100,width=45,height=25)
        self.food2.current(0)
        self.f3 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.f3.place(x=240,y=130,width=45,height=25)
        self.f3.current(0)

        self.f4 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.f4.place(x=240,y=160,width=45,height=25)
        self.f4.current(0)

        self.f5 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.f5.place(x=240,y=190,width=45,height=25)
        self.f5.current(0)

        self.f6 = ttk.Combobox(pf2,state="readonly",values=food) #readonly
        self.f6.place(x=240,y=220,width=45,height=25)
        self.f6.current(0)

        #Nationality
        label6=Label(pf2,text='Nationality',bg='sky blue',font=font1)
        label6.place(x=290,y=40,width=100,height=25)
        Nationality = [
            "India",
            "Foreigner",
        ] 
            # Create Dropdown menu
        self.n1 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n1.place(x=295,y=70,width=100,height=25)
        self.n1.current(0)

        self.n2 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n2.place(x=295,y=100,width=100,height=25)
        self.n2.current(0)

        self.n3 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n3.place(x=295,y=130,width=100,height=25)
        self.n3.current(0)

        self.n4 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n4.place(x=295,y=160,width=100,height=25)
        self.n4.current(0)

        self.n5 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n5.place(x=295,y=190,width=100,height=25)
        self.n5.current(0)

        self.n6 = ttk.Combobox(pf2,state="readonly",values=Nationality) #readonly
        self.n6.place(x=295,y=220,width=100,height=25)
        self.n6.current(0)

        

        save_b = Button(pf2, text = 'Save Ticket',bg='#FFA500',activebackground='black',font=("Times",12,"bold"), command = lambda :[self.pass_add(),go()])
        save_b.place(x=5, y=250,width=100,height=25)

<<<<<<< HEAD
=======
=======
        self.c1 = ttk.Combobox(pf2,state="readonly",values=num_of_passanger,textvariable=p_count) #readonly
        self.c1.place(x=10,y=290,width=40,height=25)
        self.c1.current(0)

        
>>>>>>> 41690c6f99fe67aaf4f1663d1e6c82eb59dfbd29
>>>>>>> 1f7b9bd93eb137a10a592b9a9ba6e517c4a5b3c8
        print(self.passanger_value)

    def pass_add(self):
        #global date,count,qouta
        name = self.p1.get()
        name2 = self.p2.get()
        name3 = self.p3.get()
        name4 = self.p4.get()
        name5 = self.p5.get()
        name6 = self.p6.get()
    

        age = self.a1.get()
        age2 = self.a2.get()
        age3 = self.a3.get()
        age4 = self.a4.get()
        age5 = self.a5.get()
        age6 = self.a6.get()

        gender = self.g1.get()
        gender2 = self.g2.get()
        gender3 = self.g3.get()
        gender4 = self.g4.get()
        gender5 = self.g5.get()
        gender6 = self.g6.get()

        ifrom = self.from_entry.get()
        ito = self.to_entry.get()
        date = self.date_entry.get()
        self.count=self.c1.get()
        self.qouta=self.Quta_entry.get()
    
        self.passanger_value["name"] = name
        self.passanger_value["name2"] = name2
        self.passanger_value["name3"] = name3
        self.passanger_value["name4"] = name4
        self.passanger_value["name5"] = name5
        self.passanger_value["name6"] = name6

        self.passanger_value["age"] = age
        self.passanger_value["age2"] = age2
        self.passanger_value["age3"] = age3
        self.passanger_value["age4"] = age4
        self.passanger_value["age5"] = age5
        self.passanger_value["age6"] = age6

        self.passanger_value["gender"] = gender
        self.passanger_value["gender2"] = gender2
        self.passanger_value["gender3"] = gender3
        self.passanger_value["gender4"] = gender4
        self.passanger_value["gender5"] = gender5
        self.passanger_value["gender6"] = gender6

        self.passanger_value["ifrom"] = ifrom
        self.passanger_value["ito"] = ito
        self.passanger_value["date"] = date
        self.passanger_value["total"]=self.count
        self.passanger_value["qouta"]=self.qouta
        print("Quta_entry :", self.qouta)
        print(self.passanger_value)
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
        counter_tatkal=1
        
        # print(counter_value)
        if self.qouta =='TATKAL':

            try:
                query='SELECT counter_tatkal from tatkal_data '
                try:
                    mycursor.execute(query)
                    all=mycursor.fetchall()
                    counter_tatkal=int(all[-1][0])
                    counter_tatkal=counter_tatkal+1
                    print(counter_tatkal)
                except:
                    print(counter_tatkal)
                
                # mycursor.execute('''create table if not exists tatkal_data(name text ,age text ,gender text ,
                # ifrom text ,ito text ,date text ,qouta text, counter_tatkal text )''')

                sql = '''INSERT INTO  tatkal_data (NAME,AGE,GENDER,
                IFROM,ITO,DATE,qouta,counter_tatkal,total) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)'''
                
                if self.count=='1':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                elif self.count=='2':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                elif self.count=='3':
                    
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val2 = (name3,age3,gender3,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                    mycursor.execute(sql, val2)
                    
                elif self.count=='4':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val2 = (name3,age3,gender3,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val3 = (name4,age4,gender4,ifrom,ito,date,self.qouta,counter_tatkal,self.count)

                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                    mycursor.execute(sql, val2)
                    mycursor.execute(sql, val3)
                    
                elif self.count=='5':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val2 = (name3,age3,gender3,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val3 = (name4,age4,gender4,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val4 = (name5,age5,gender5,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                    mycursor.execute(sql, val2)
                    mycursor.execute(sql, val3)
                    mycursor.execute(sql, val4)
                    
                elif self.count=='6':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val2 = (name3,age3,gender3,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val3 = (name4,age4,gender4,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val4 = (name5,age5,gender5,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val5 = (name6,age6,gender6,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                    mycursor.execute(sql, val2)
                    mycursor.execute(sql, val3)
                    mycursor.execute(sql, val4)
                    mycursor.execute(sql, val5)
                
                print('counter_tatkal:',counter_tatkal)
            
                
                
                
                mysqldb.commit()
                lastid = mycursor.lastrowid
                # def go():
                #     messagebox.showinfo("information", "passanger data inserted successfully...")
                #     passanger_screen()
                print(date)
                self.p1.delete(0, END)
                self.a1.delete(0, END)
                self.g1.delete(0, END)

                self.p2.delete(0, END)
                self.a2.delete(0, END)
                self.g2.delete(0, END)

                self.p3.delete(0, END)
                self.a3.delete(0, END)
                self.g3.delete(0, END)

                self.p4.delete(0, END)
                self.a4.delete(0, END)
                self.g4.delete(0, END)

                self.p5.delete(0, END)
                self.a5.delete(0, END)
                self.g5.delete(0, END)

                self.p6.delete(0, END)
                self.a6.delete(0, END)
                self.g6.delete(0, END)

                self.from_entry.delete(0, END)
                self.to_entry.delete(0, END)
                self.date_entry.delete(0, END)
                self.Quta_entry.delete(0, END)
                self.p1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        elif self.qouta =='GENERAL':
            try:
                query='SELECT counter_tatkal from tatkal_data '
                try:
                    mycursor.execute(query)
                    all=mycursor.fetchall()
                    counter_tatkal=int(all[-1][0])
                    counter_tatkal=counter_tatkal+1
                    print(counter_tatkal)
                except:
                    print(counter_tatkal)
                
                # mycursor.execute('''create table if not exists tatkal_data(name text ,age text ,gender text ,
                # ifrom text ,ito text ,date text ,qouta text, counter_tatkal text )''')

                sql = '''INSERT INTO  tatkal_data (NAME,AGE,GENDER,
                IFROM,ITO,DATE,qouta,counter_tatkal,total) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)'''
                
                if self.count=='1':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                elif self.count=='2':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                elif self.count=='3':
                    
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val2 = (name3,age3,gender3,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                    mycursor.execute(sql, val2)
                    
                elif self.count=='4':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val2 = (name3,age3,gender3,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val3 = (name4,age4,gender4,ifrom,ito,date,self.qouta,counter_tatkal,self.count)

                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                    mycursor.execute(sql, val2)
                    mycursor.execute(sql, val3)
                    
                elif self.count=='5':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val2 = (name3,age3,gender3,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val3 = (name4,age4,gender4,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val4 = (name5,age5,gender5,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                    mycursor.execute(sql, val2)
                    mycursor.execute(sql, val3)
                    mycursor.execute(sql, val4)
                    
                elif self.count=='6':
                    val = (name,age,gender,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val1 = (name2,age2,gender2,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val2 = (name3,age3,gender3,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val3 = (name4,age4,gender4,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val4 = (name5,age5,gender5,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    val5 = (name6,age6,gender6,ifrom,ito,date,self.qouta,counter_tatkal,self.count)
                    mycursor.execute(sql, val)
                    mycursor.execute(sql, val1)
                    mycursor.execute(sql, val2)
                    mycursor.execute(sql, val3)
                    mycursor.execute(sql, val4)
                    mycursor.execute(sql, val5)
                
                print('counter_tatkal:',counter_tatkal)
            
                
                
                
                mysqldb.commit()
                lastid = mycursor.lastrowid
                # def go():
                #     messagebox.showinfo("information", "passanger data inserted successfully...")
                #     passanger_screen()
                print(date)
                self.p1.delete(0, END)
                self.a1.delete(0, END)
                self.g1.delete(0, END)

                self.p2.delete(0, END)
                self.a2.delete(0, END)
                self.g2.delete(0, END)

                self.p3.delete(0, END)
                self.a3.delete(0, END)
                self.g3.delete(0, END)

                self.p4.delete(0, END)
                self.a4.delete(0, END)
                self.g4.delete(0, END)

                self.p5.delete(0, END)
                self.a5.delete(0, END)
                self.g5.delete(0, END)

                self.p6.delete(0, END)
                self.a6.delete(0, END)
                self.g6.delete(0, END)

                self.from_entry.delete(0, END)
                self.to_entry.delete(0, END)
                self.date_entry.delete(0, END)
                self.Quta_entry.delete(0, END)
                self.p1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        