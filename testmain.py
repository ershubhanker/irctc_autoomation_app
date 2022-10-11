# from ast import Delete
from tkinter import *
#import tkinter as tk
from tkinter import ttk,messagebox
# from turtle import heading, width 
#from PIL import Image, ImageTk
# from tkinter.messagebox import askyesno
from tkinter import font  as tkfont
from functools import partial
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
import PIL.Image
from PIL import Image,ImageFilter
from functools import partial
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import mysql.connector
connection=mysql.connector.connect(host='localhost',username='root',password='deol9646',database="train_login")
from tkcalendar import DateEntry


my_conn = connection.cursor()
my_conn.execute('''create table if not exists login(username text ,password text)''')

#----window----
root = Tk()
root.configure(bg='sky blue')
root.title("IRCTC")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("1200x600+200+50")

passanger_value={'name':"",'age':"",'gender':"",'ifrom':"",'ito':"",'date':""}


def start():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.irctc.co.in/nget/train-search")

    
    # get element of ok 
    element = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button")
    element.click()
    time.sleep(1)
    
    #tap on date 
    date = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input")
    date.click()
    time.sleep(1)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = date)
    action.double_click(on_element = date)
    # send keys
    
    action.send_keys("12/10/2022")
    action.perform()
    time.sleep(2)
    #tap on from route
    loc = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
    loc.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = loc)
    # send keys
    
    action.send_keys(from_entry.get())
    action.perform()
    time.sleep(2)
    #from location
    loc1 = driver.find_element(By.XPATH, '//*[@id="pr_id_1_list"]/li/span')
    loc1.click()
    time.sleep(2)
    #tap on from route
    loc3 = driver.find_element(By.XPATH, '//*[@id="destination"]/span/input')
    loc3.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = loc3)
    # send keys
    action.send_keys(to_entry.get())

    action.perform()
    time.sleep(2)
    #destination location
    loc4 = driver.find_element(By.XPATH, '//*[@id="pr_id_2_list"]/li[1]')
    loc4.click()
    time.sleep(2)
    #SEARCH
    search = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button')
    search.click()
    time.sleep(2)
    #refresh
    choose = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]/span')
    choose.click()
    time.sleep(2)
    #choose train
    choose = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[7]/div[1]/div[3]/table/tr/td[2]/div/div[2]')
    choose.click()
    time.sleep(2)

    #book
    book = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button')
    book.click()
    time.sleep(2)
    #agree
    agree = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/p-confirmdialog[1]/div/div/div[3]/button[1]/span[2]')
    agree.click()
    time.sleep(4)

    # #get element for login button
    # element2 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]')
    # element2.click()
    # time.sleep(3)
    # get element for usernme
    element3 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/input')

    # create action chain object
    action = ActionChains(driver)

    # click the item
    action.click(on_element = element3)

    # send keys
    action.send_keys(e1.get())

    # perform the operation
    action.perform()
    time.sleep(3)
    print('username entered')
    # get element for password
    element4 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/input')

    # create action chain object
    action = ActionChains(driver)

    # click the item
    action.click(on_element = element4)

    # send keys
    action.send_keys(e2.get())

    # perform the operation
    action.perform()
    print('password entered')

    img=driver.find_element(By.ID, "nlpImgContainer")

    img.screenshot("logo.png")
    im = PIL.Image.open('logo.png')
    left = 0
    top = 250
    right = 300
    bottom = 270

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im1.save("crop.png" ,quality=100)
    print('image address:',im1) 
    captcha = pytesseract.image_to_string(im1) 
    captcha = captcha.replace(" ", "").strip()

    with open('abc.txt',mode ='w') as file:      
        file.write(captcha) 
        print('result',captcha)
        print('write result',captcha[18:22])
        
    #sget element for captcha enter
    element5 = driver.find_element(By.XPATH, "//*[@id='nlpAnswer']")
    print('find')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = element5)
    # send keys
    action.send_keys(captcha[18:22])
    action.perform()
    print('captcha enter')

    time.sleep(1)
    # get element of ok 
    signup = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button')
    signup.click()
    print('signup')
    time.sleep(5)

    #passenger box
    name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
    name.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = name)
    # send keys
    action.send_keys(p1.get())
    action.perform()
    time.sleep(2)

    #age box
    age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
    age.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = age)
    # send keys
    action.send_keys(a1.get())
    action.perform()
    time.sleep(2)

    #gender box
    gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
    gender.click()
    time.sleep(2)

    gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
    gender_select.click()

    # #food box
    # food = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select')
    # food.click()
    # time.sleep(1)
    # #veg choose
    # food_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select/option[2]')
    # food_select.click()
    # time.sleep(1)
    #pay option
    pay = driver.find_element(By.XPATH, '//*[@id="2"]/div/div[2]/span')
    pay.click()
    time.sleep(2)

    #continue button
    submit = driver.find_element(By.XPATH, '//*[@id="psgn-form"]/form/div/div[1]/div[14]/div/button[2]')
    submit.click()
    time.sleep(5)

    img=driver.find_element(By.ID, "nlpImgContainer")
    img.screenshot("logo2.png")
    im = PIL.Image.open('logo2.png')
    left = 0
    top = 250
    right = 300
    bottom = 270

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im1.save("crop2.png" ,quality=100)
    print('image address:',im1) 
    captcha = pytesseract.image_to_string(im1) 
    captcha = captcha.replace(" ", "").strip()
    

    with open('payment.txt',mode ='w') as file:      
        file.write(captcha) 
        print('result',captcha)
        print('write result',captcha[18:22])
        
    #sget element for captcha enter
    element5 = driver.find_element(By.XPATH, "//*[@id='nlpAnswer']")
    print('find')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = element5)
    # send keys
    action.send_keys(captcha[18:22])
    action.perform()
    print('captcha enter')
    time.sleep(1)

    #continue buttton
    continue_button = driver.find_element(By.XPATH, '//*[@id="review"]/div[1]/form/div[3]/div/button[2]')
    continue_button.click()
    print('continue_button')
    time.sleep(3)

    #multiple payment buttton
    upi_choose = driver.find_element(By.XPATH, '//*[@id="pay-type"]/span/div[1]/span')
    upi_choose.click()
    print('multiple choose')
    time.sleep(2)

    
    #roserpay buttton
    roserpay = driver.find_element(By.XPATH, '//*[@id="bank-type"]/div/table/tr/span[3]/td/div/div/span')
    roserpay.click()
    print('upi choose roserpay')
    time.sleep(2)

    #pay & book button
    pay = driver.find_element(By.XPATH,'//*[@id="psgn-form"]/div[1]/div[1]/app-payment/div[2]/button[2]')
    pay.click()
    print('upi payment')
    time.sleep(2)

    #upi or QR
    roserpay = driver.find_element(By.XPATH, '//*[@id="form-common"]/div[1]/div/div/div/div/div/button[1]')
    roserpay.click()
    print('upi choose roserpay')
    time.sleep(2)

   
    #clicl and add upi
    conti_confirm = driver.find_element(By.XPATH,'//*[@id="vpa-upi"]')
    conti_confirm.click()
    print('add payment number')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = conti_confirm)
    # send keys
    action.send_keys('sarbjitdeol@ybl')
    action.perform()
    time.sleep(2)

    #proceed button to paytm
    paytm_submit = driver.find_element(By.XPATH,'//*[@id="footer-cta"]')
    paytm_submit.click()
    print(' pay button')
    time.sleep(2)

    #proceed button to paytm
    contine_pay = driver.find_element(By.XPATH,'//*[@id="overlay"]/div/div/div[2]')
    contine_pay.click()
    print(' continue button')
    time.sleep(2)

    while True:
        pass

def login_screen():
    global e1,e2
    page1=Frame(root,bg='sky blue', width=1200, height=550)
    page1.place(x=0,y=0)
    font1=tkfont.Font(family='Times', size=15, weight="bold")

    #frames
    f1=Frame(page1 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=1)
    f1.place(x=10,y=20,width=880,height=200)
    #labels
    label1=Label(page1,text='Login Details',bg='sky blue',font=font1)
    label1.place(x=17, y=10)
    label2=Label(f1,text='Irctc ID :',bg='sky blue',font=("Times",12,"bold"))
    label2.place(x=100, y=10)
    label3=Label(f1,text='Password :',bg='sky blue',font=("Times",12,"bold"))
    label3.place(x=400, y=10)

    username = StringVar()
    password = StringVar()

    e1=Entry(f1,font=("Times",12,"bold"),textvariable=username)
    e1.place(x=180, y=10,width=200,height=30)
    
    e2=Entry(f1,font=("Times",12,"bold"),textvariable=password)
    e2.place(x=490, y=10,width=200,height=30)
    #validateLogin = partial(validateLogin, username, password)
    #save button
    save = Button(f1, text = 'Add',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : Add())
    save.place(x=330, y=70,width=200,height=30)

    
  
    f2=Frame(page1,bg='sky blue')
    f2.place(x=150,y=220,width=880,height=340)
    #frame 2 button
    delb = Button(f2, text = 'Delete',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : delete())
    delb.place(x=530, y=80,width=150,height=30)
    upd = Button(f2, text = 'Update',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : update())
    upd.place(x=530, y=140,width=150,height=30)
    login = Button(f2, text = 'LOGIN',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : start())
    login.place(x=530, y=200,width=150,height=30)


    def GetValue(event):
        
        e1.delete(0,END)
        e2.delete(0,END)
        row_id=listbox.selection()[0]
        select=listbox.set(row_id)
        e1.insert(0,select['username'])
        e2.insert(0,select['password'])
    
    
    def Add():
        username = e1.get()
        password = e2.get()
    
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            sql = "INSERT INTO  login (username,password) VALUES (%s, %s)"
            val = (username,password,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Employee inserted successfully...")
            e1.delete(0, END)
            e2.delete(0, END)
            e1.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    
    
    def update():
        username = e1.get()
        password = e2.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            sql = "Update login set username= %s,password= %s "

            val = (username,password)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record Updateddddd successfully...")
        
            e1.delete(0, END)
            e2.delete(0, END)
            
            e1.focus_set()
    
        except Exception as e:
    
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    
    def delete():
        username = e1.get()
    
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            sql = "delete from login where username = %s"
            val = (username,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record Deleteeeee successfully...")
        
            e1.delete(0, END)
            e2.delete(0, END)
        

            e1.focus_set()
    
        except Exception as e:
    
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    
    def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT username,password FROM login")
        records = mycursor.fetchall()
        print(records)

        for i, (username,password) in enumerate(records, start=1):
            listbox.insert("", "end", values=(username,password))
            connection.close()
    
    cols=("username","password")
    listbox=ttk.Treeview(f2,columns=cols,show='headings')

    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=0,column=0,columnspan=2)
        listbox.place(width=500,height=370)

    show()
    listbox.bind("<Double-Button-1>",GetValue)

def passanger_screen():
    global p1,a1,g1,from_entry,to_entry,date_entry,passanger_value
    
    page2=Frame(root,bg='sky blue', width=1200, height=550)
    page2.place(x=0,y=0)
    font1=tkfont.Font(family='Helvetica', size=10, weight="bold")
    #frames
    pf1=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
    pf1.place(x=0,y=0,width=350,height=500)

    l1=Label(pf1,text='Train Details',bg='light gray',foreground='white',font=font1)
    l1.place(x=0,y=0,width=336,height=40)

    p_from = StringVar()
    p_to = StringVar()
    p_date = StringVar()
    p_name = StringVar()
    p_age = StringVar()
    p_gender = StringVar()

    p_from.set(passanger_value["ifrom"])
    p_to.set(passanger_value["ito"])
    p_date.set(passanger_value["date"])
    p_name.set(passanger_value["name"])
    p_age.set(passanger_value["age"])
    p_gender.set(passanger_value["gender"])
    

    #from label & entry
    from_label=Label(pf1,text='From :',bg='sky blue',font=font1)
    from_label.place(x=10,y=60,width=50,height=25)
    from_entry=Entry(pf1,textvariable=p_from)
    from_entry.place(x=120,y=60,width=200,height=25)
    
    #To label & entry
    to_label=Label(pf1,text='To :',bg='sky blue',font=font1)
    to_label.place(x=10,y=100,width=30,height=25)
    to_entry=Entry(pf1,textvariable=p_to)
    to_entry.place(x=120,y=100,width=200,height=25)

    #journey date label & entry
    date_label=Label(pf1,text='Journey Date :',bg='sky blue',font=font1)
    date_label.place(x=10,y=140,width=100,height=25)
    date_entry=DateEntry(pf1,selectmode='day',date_pattern='dd/MM/yyyy',textvariable=p_date)
    date_entry.place(x=222,y=140,width=100,height=25)
    
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
    
    search_b = Button(pf1, text = 'save',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda :pass_add())
    search_b.place(x=120, y=340,width=150,height=30)

    #frame2 passanger detail
    pf2=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=3)
    pf2.place(x=350,y=0,width=850,height=500)

    l2=Label(pf2,text='Enter Passenger Details',bg='light gray',foreground='white',font=font1)
    l2.place(x=0,y=0,width=835,height=40)


    #Column labels 
    label1=Label(pf2,text='Passenger Name',bg='sky blue',font=font1)
    label1.place(x=20,y=60,width=120,height=25)
    p1=Entry(pf2,textvariable=p_name)
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
    a1=Entry(pf2,textvariable=p_age)
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
    g1 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p_gender) #readonly
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
    

    
    def pass_add():
        
        name = p1.get()
        age = a1.get()
        gender = g1.get()
        ifrom = from_entry.get()
        ito = to_entry.get()
        date = date_entry.get()

        passanger_value["name"] = name
        passanger_value["age"] = age
        passanger_value["gender"] = gender
        passanger_value["ifrom"] = ifrom
        passanger_value["ito"] = ito
        passanger_value["date"] = date
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            my_conn.execute('''create table if not exists passanger_data(name text ,age text ,gender text ,ifrom text ,ito text ,date text)''')
            sql = "INSERT INTO  passanger_data (NAME,AGE,GENDER,IFROM,ITO,DATE) VALUES (%s, %s, %s, %s, %s,%s)"
            val = (name,age,gender,ifrom,ito,date)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "passanger data inserted successfully...")
            p1.delete(0, END)
            a1.delete(0, END)
            g1.delete(0, END)
            from_entry.delete(0, END)
            to_entry.delete(0, END)
            date_entry.delete(0, END)
            p1.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

def third_screen():
    page3=Frame(root,bg='yellow', width=1200, height=550)
    page3.place(x=0,y=0)
    test = Label(page3,text="PAYMENT")
    test.place(x = 50, y = 50)

def fourth_screen():
    page4=Frame(root,bg='green', width=1200, height=550)
    page4.place(x=0,y=0)
    test = Label(page4,text="HOME")
    test.place(x = 50, y = 50)

Button1=Button(root,text='LOGIN',command=lambda:login_screen())
Button1.place(x=10,y=570)
Button2=Button(root,text='PASSSENGER',command=lambda:passanger_screen())
Button2.place(x=65,y=570)
Button3=Button(root,text='PAYMENT',command=lambda:third_screen())
Button3.place(x=155,y=570)
Button3=Button(root,text='HOME',command=lambda:fourth_screen())
Button3.place(x=230,y=570)


root.mainloop()