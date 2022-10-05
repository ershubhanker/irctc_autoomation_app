from ast import Delete
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from turtle import heading, width 
from PIL import Image, ImageTk
from tkinter.messagebox import askyesno
from tkinter import font  as tkfont
from functools import partial
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# import Action chains 
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

print('successfully connected')
# ####### end of connection ####
my_conn = connection.cursor()

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



def start():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.irctc.co.in/nget/train-search")

    
    # get element of ok 
    element = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button")
    element.click()
    time.sleep(1)
    #get element for login button
    element2 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]')
    element2.click()
    time.sleep(3)
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
    signup = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button")
    signup.click()
    print('signup')
    time.sleep(5)
    #tap on date 
    date = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input")
    date.click()
    time.sleep(1)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = date)
    action.double_click(on_element = date)
    # send keys
    action.send_keys("06/10/2022")
    action.perform()
    time.sleep(2)
    #tap on from route
    loc = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input')
    loc.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = loc)
    # send keys
    action.send_keys("CDG")
    action.perform()
    time.sleep(2)
    #CHANDIGARH
    loc1 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/div/ul/li[1]/span')
    loc1.click()
    time.sleep(2)
    #tap on from route
    loc3 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/input')
    loc3.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = loc3)
    # send keys
    action.send_keys("ASR")

    action.perform()
    time.sleep(2)
    #asr
    loc4 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/div/ul/li[1]/span")
    loc4.click()
    time.sleep(2)
    #SEARCH
    search = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div/button")
    search.click()
    time.sleep(2)
    #refresh
    choose = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-train-list/div[4]/div[1]/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]")
    choose.click()
    time.sleep(2)
    #choose train
    choose = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-train-list/div[4]/div[1]/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[7]/div[1]/div[3]/table/tr/td[2]/div/div[2]/strong")
    choose.click()
    time.sleep(2)

    #book
    book = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-train-list/div[4]/div[1]/div[5]/div/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button")
    book.click()
    time.sleep(2)
    #agree
    agree = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-train-list/p-confirmdialog[1]/div/div/div[3]/button[1]/span[2]")
    agree.click()
    time.sleep(4)
    #passenger box
    name = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span")
    name.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = name)
    # send keys
    action.send_keys("sarbjit")
    action.perform()
    time.sleep(2)

    #age box
    age = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input")
    age.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = age)
    # send keys
    action.send_keys("21")
    action.perform()
    time.sleep(2)

    #gender box
    gender = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select")
    gender.click()
    time.sleep(2)

    gender_select = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]")
    gender_select.click()
    #pay option
    pay = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[12]/p-panel/div/div[2]/div/table/tr[2]/label/p-radiobutton/div/div[2]/span")
    pay.click()
    time.sleep(2)

    #continue button
    submit = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[14]/div/button[2]")
    submit.click()
    time.sleep(5)
    while True:
        pass

def fetchdata(student):
    print('1',student)
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
    #---Page---
    font1=tkfont.Font(family='Times', size=15, weight="bold")

    #frames
    f1=Frame(page2 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=1)
    f1.place(x=10,y=20,width=880,height=200)
    #labels
    label1=Label(page2,text='IRCTC ID',bg='sky blue',font=font1)
    label1.place(x=17, y=10)
    label2=Label(f1,text='Irstc ID :',bg='sky blue',font=("Times",12,"bold"))
    label2.place(x=100, y=10)
    label3=Label(f1,text='Password :',bg='sky blue',font=("Times",12,"bold"))
    label3.place(x=400, y=10)

    # f1 entry
    global e1,e2
    username = StringVar()
    e1=Entry(f1,font=("Times",12,"bold"),textvariable=username)
    e1.place(x=180, y=10,width=200,height=30)
    password = StringVar()
    e2=Entry(f1,font=("Times",12,"bold"),textvariable=password)
    e2.place(x=490, y=10,width=200,height=30)
    #validateLogin = partial(validateLogin, username, password)
    #save button
    save = Button(f1, text = 'Add',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : Add())
    save.place(x=330, y=70,width=200,height=30)

    
    # v1=StringVar()
    # v2=StringVar()
    # v1=username.get()
    # v2=password.get()
    
    # print(v1)
    # print(v2)
    
    f2=Frame(page2,bg='sky blue')
    f2.place(x=150,y=220,width=880,height=340)
    #frame 2 button
    delb = Button(f2, text = 'Delete',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : delete())
    delb.place(x=530, y=80,width=150,height=30)
    upd = Button(f2, text = 'Update',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : update())
    upd.place(x=530, y=140,width=150,height=30)
    login = Button(f2, text = 'Login',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : start())
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