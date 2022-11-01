# from ast import Delete
from cProfile import label
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
from selenium.webdriver.chrome.options import Options 
import time
import PIL.Image
from PIL import Image,ImageFilter
from functools import partial
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import mysql.connector
connection=mysql.connector.connect(host='localhost',username='root',password='deol9646',database="train_login")
from tkcalendar import DateEntry

#database connect
my_conn = connection.cursor()
# create login table
my_conn.execute('''create table if not exists login(username text ,password text ,name text)''')

#----root window----
root = Tk()
root.configure(bg='sky blue')
root.title("IRCTC")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("1200x600+200+50")
icon=PhotoImage(file='icon.png')
root.iconphoto(False,icon)
#passanger value dictionary
passanger_value={'name':"",'age':"",'gender':"",'name2':"",'age2':"",'gender2':"",'name3':"",'age3':"",'gender3':"",'name4':"",'age4':"",'gender4':"",'name5':"",'age5':"",'gender5':"",'name6':"",'age6':"",'gender6':"",'ifrom':"",'ito':"",'date':"",'total':"",}

payment_value={'upi':"",'temp_name':""}
#irctc website fuction
def start():
    try:    
        os.chdir('C:\\Program Files\\Google\\Chrome\\Application')
        os.system('start cmd /k "chrome.exe --remote-debugging-port=9222 --user-data-dir=E:\chromedriver_win32\chromedata"')
    except:
        print('re check path')
    opt = Options()
    opt.add_experimental_option("debuggerAddress",'localhost:9222')
    driver=webdriver.Chrome(executable_path=r"E:\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
    
    
    driver.maximize_window()
    driver.get("https://www.irctc.co.in/nget/train-search")

    
    # click ok 
    element = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button")
    element.click()
    time.sleep(1)

    #get element for login button
    element2 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]')
    element2.click()
    time.sleep(3)

    #get element for usernme
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
    #image function for captcha
    img=driver.find_element(By.ID, "nlpImgContainer") #By.ID, "nlpImgContainer"
    img.screenshot(r'E:\DJANGO\recapcha bypass\logo.png')
    im = Image.open(r'E:\DJANGO\recapcha bypass\logo.png') #use PIL.Image.open if not work
    left = 0
    top = 250
    right = 300
    bottom = 270

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im1.save(r'E:\DJANGO\recapcha bypass\crop.png' ,quality=100)
    print('image address:',im1) 
    captcha = pytesseract.image_to_string(im1) 
    captcha = captcha.replace(" ", "").strip()
    # save in abc.txt file
    with open(r'E:\DJANGO\recapcha bypass\abc.txt',mode ='w') as file:      
        file.write(captcha) 
        print('result',captcha)
        print('write result',captcha[18:22]) #5:14 paints  18:22default  5:12match
        
    #get element for captcha enter
    element5 = driver.find_element(By.XPATH, "//*[@id='nlpAnswer']")
    print('find')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = element5)
    # enter captcha
    action.send_keys(captcha[18:22]) #[18:22]
    action.perform()
    print('captcha enter')
    time.sleep(5)

    # click signup button 
    signup = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button')
    signup.click()
    print('signup')
    time.sleep(6)
    #tap on date 
    date_e = driver.find_element(By.XPATH, "//*[@id='jDate']/span/input")
    date_e.click()
    time.sleep(1)
    # create action chain object
    action = ActionChains(driver)
    # click the date
    action.click(on_element = date_e)
    action.double_click(on_element = date_e)
    # write date
    action.send_keys(date)
    action.perform()
    time.sleep(2)
    #tap on from route
    loc = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
    loc.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the from route
    action.click(on_element = loc)
    # enter from location
    action.send_keys(from_entry.get())
    action.perform()
    time.sleep(2)

    #to location click
    loc1 = driver.find_element(By.XPATH, '//*[@id="pr_id_1_list"]/li/span')
    loc1.click()
    time.sleep(2)
    #tap on to route
    loc3 = driver.find_element(By.XPATH, '//*[@id="destination"]/span/input')
    loc3.click()
    time.sleep(2)
    # create action chain object
    action = ActionChains(driver)
    # click the to location
    action.click(on_element = loc3)
    # enter destination 
    action.send_keys(to_entry.get())
    action.perform()
    time.sleep(2)
    # click destination location
    loc4 = driver.find_element(By.XPATH, '//*[@id="pr_id_2_list"]/li[1]')
    loc4.click()
    time.sleep(2)

    #SEARCH buttton click
    search = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div/button')
    search.click()
    time.sleep(3)

    #refresh button
    choose = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]/span')
    choose.click()
    time.sleep(2)

    #choose train
    choose = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[7]/div[1]/div[3]/table/tr/td[2]/div/div[2]/strong')
    choose.click()
    time.sleep(2)

    #book
    book = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button')
    book.click()
    time.sleep(2)
    # #agree
    # agree = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/p-confirmdialog[1]/div/div/div[3]/button[1]/span[2]')
    # agree.click()
    # time.sleep(4)

    
    
    # ---function of passangers 1 2 3 4 5 6------
    def pass1():
        #enter passanger name
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
    def pass2():
        pass1()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[1]/a/span[1]')
        add_pas.click()

        #enter passanger name
        name2 = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name2.click()
        time.sleep(2)                               #//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name2)
        # send keys
        action.send_keys(p2.get())
        action.perform()
        time.sleep(2)

        #age box
        age2 = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age2.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age2)
        # send keys
        action.send_keys(a2.get())
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        #male
        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()

        #female
        # gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-24-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[3]')
        # gender_select.click()
    def pass3():
        pass2()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[1]/a/span[2]')
        add_pas.click()

        #enter passanger name
        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(p3.get())
        action.perform()
        time.sleep(2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(a3.get())
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()

    def pass4():
        pass3()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[1]/a/span[2]')
        add_pas.click()

        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(p4.get())
        action.perform()
        time.sleep(2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(a4.get())
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()
    def pass5():
        pass4()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[1]/a/span[1]')
        add_pas.click()

        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(p5.get())
        action.perform()
        time.sleep(2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(a5.get())
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()
    def pass6():
        pass5()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[1]/a/span[1]')
        add_pas.click()

        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(p6.get())
        action.perform()
        time.sleep(2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(a6.get())
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()

    # ------condition of passanger count-----------
    if count=='1':
        pass1()
    elif count == '2':
        pass2()
    elif count == '3':
        pass3()
    elif count == '4':
        pass4()
    elif count == '5':
        pass5()
    elif count == '6':
        pass6()
    
        

    #food box
    # food = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select')
    # food.click()
    # time.sleep(1)
    # #veg choose
    # food_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select/option[2]')
    # food_select.click()
    # time.sleep(1)

    
    #choose pay option from debit or upi

    #default set for debit pay

    #upi select
    pay = driver.find_element(By.XPATH, '//*[@id="2"]/div/div[2]/span') # for upi
    pay.click()
    time.sleep(2)

    #continue button
    submit = driver.find_element(By.XPATH, '//*[@id="psgn-form"]/form/div/div[1]/div[14]/div/button[2]')
    submit.click()
    time.sleep(5)

    #payment captcha 
    img=driver.find_element(By.ID, "nlpImgContainer")
    img.screenshot(r"E:\DJANGO\recapcha bypass\logo2.png")
    im = Image.open(r"E:\DJANGO\recapcha bypass\logo2.png")
    left = 0
    top = 250
    right = 300
    bottom = 270
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im1.save(r"E:\DJANGO\recapcha bypass\crop2.png" ,quality=100)
    print('image address:',im1) 
    captcha = pytesseract.image_to_string(im1) 
    captcha = captcha.replace(" ", "").strip()

    #save in payment.txt
    with open('payment.txt',mode ='w') as file:      
        file.write(captcha) 
        print('result',captcha)
        print('write result',captcha[18:22])
        
    #get element for captcha enter
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


    #choose method to pay

    
    #choose multiple payment method //*[@id="pay-type"]/span/div[1]/span
    upi_choose = driver.find_element(By.XPATH, '//*[@id="pay-type"]/span/div[1]/span')
    upi_choose.click()
    print('multiple choose')
    time.sleep(2)

    
    #roserpay select 
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
    roserpay = driver.find_element(By.XPATH, '//*[@id="form-common"]/div[1]/div/div/div/div/div/button[1]/div/div[1]/div[1]/div[1]')
    roserpay.click()
    print('upi choose roserpay')
    time.sleep(2)

   
    #click and add upi
    conti_confirm = driver.find_element(By.XPATH,'//*[@id="vpa-upi"]')
    conti_confirm.click()
    print('add payment number')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = conti_confirm)
    # send keys
    action.send_keys(upi_entry.get())
    action.perform()
    time.sleep(2)

    #select debit
    def debit_function():
        #click on card number
        card_number = driver.find_element(By.XPATH,'//*[@id="card_number"]')
        card_number.click()
        action = ActionChains(driver)
                # click the item
        action.click(on_element = card_number)
                # send keys
        action.send_keys('card number')
        action.perform()
        time.sleep(2)

        #click on Expiry
        card_expiry = driver.find_element(By.XPATH,'//*[@id="card_expiry"]')
        card_expiry.click()
        action = ActionChains(driver)
                # click the item
        action.click(on_element = card_expiry)
                # send keys
        action.send_keys('0123')
        action.perform()
        time.sleep(2)

        #click on holder's name
        card_holder = driver.find_element(By.XPATH,'//*[@id="card_name"]')
        card_holder.click()
        action = ActionChains(driver)
                # click the item
        action.click(on_element = card_holder)
                # send keys
        action.send_keys('holder name')
        action.perform()
        time.sleep(2)

        #click on CVV
        card_CVV = driver.find_element(By.XPATH,'//*[@id="card_cvv"]')
        card_CVV.click()
        action = ActionChains(driver)
                # click the item
        action.click(on_element = card_CVV)
                # send keys
        action.send_keys('102')
        action.perform()
        time.sleep(2)



    #proceed button to upi pay
    paytm_submit = driver.find_element(By.XPATH,'//*[@id="footer-cta"]')
    paytm_submit.click()
    print(' pay button')
    time.sleep(2)

    #continue for mobile pay send
    contine_pay = driver.find_element(By.XPATH,'//*[@id="overlay"]/div/div/div[2]')
    contine_pay.click()
    print(' continue button')
    time.sleep(2)

    while True:
        pass

#irctc login screen
def login_screen():
    global e1,e2
    page1=Frame(root,bg='sky blue', width=1200, height=550)
    page1.place(x=0,y=0)
    font1=tkfont.Font(family='Times', size=15, weight="bold")

    #frame 1 for username and password detail
    f1=Frame(page1 ,bg='sky blue',bd=5,highlightbackground="white", highlightthickness=1)
    f1.place(x=140,y=20,width=880,height=200)
    #labels
    label1=Label(page1,text='Login Details',bg='sky blue',font=font1)
    label1.place(x=170, y=10)
    label2=Label(f1,text='Irctc ID :',bg='sky blue',font=("Times",12,"bold"))
    label2.place(x=100, y=10)
    label3=Label(f1,text='Password :',bg='sky blue',font=("Times",12,"bold"))
    label3.place(x=400, y=10)
    temp = StringVar()
    temp_lbl=Label(f1,text='Give a name to store',fg='white',bg='sky blue',font=("Times",11,'bold'))
    temp_lbl.place(x=365, y=50)
    temp_entry=Entry(f1,font=("Times",11,"bold"),textvariable=temp)
    temp_entry.place(x=350,y=70)

    
    username = StringVar()
    password = StringVar()
    #username entry
    e1=Entry(f1,font=("Times",12,"bold"),textvariable=username)
    e1.place(x=180, y=10,width=200,height=30)
    #password entry
    e2=Entry(f1,font=("Times",12,"bold"),textvariable=password)
    e2.place(x=490, y=10,width=200,height=30)
    #save button
    save = Button(f1, text = 'Add',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : Add())
    save.place(x=330, y=120,width=200,height=30)

    
    # frame 2 for list view for login data
    f2=Frame(page1,bg='sky blue')
    f2.place(x=250,y=220,width=740,height=330)

    #frame 2 button delete update login 
    delb = Button(f2, text = 'Delete',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : delete())
    delb.place(x=530, y=80,width=150,height=30)
    upd = Button(f2, text = 'Update',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : update())
    upd.place(x=530, y=140,width=150,height=30)
    login = Button(f2, text = 'LOGIN',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda : start())
    login.place(x=530, y=200,width=150,height=30)

    #function for get username and password from entry
    def GetValue(event):
        
        e1.delete(0,END)
        e2.delete(0,END)
        temp_entry.delete(0,END)
        row_id=listbox.selection()[0]
        select=listbox.set(row_id)
        e1.insert(0,select['username'])
        e2.insert(0,select['password'])
        temp_entry.insert(0,select['name'])
    
    # add user and pass in database
    def Add():
        username = e1.get()
        password = e2.get()
        name=temp_entry.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            sql = "INSERT INTO  login (username,password,name) VALUES (%s, %s,%s)"
            val = (username,password,name)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Employee inserted successfully...launch app again to watch")
            e1.delete(0, END)
            e2.delete(0, END)
            temp_entry.delete(0,END)
            e1.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    
    # update user and pass in database
    def update():
        username = e1.get()
        password = e2.get()
        name=temp_entry.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            sql = "Update login set username= %s , password= %s where name =%s"

            val = (username,password,name)
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

    # # delete user and pass from database
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

    # show user and pass in list
    def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT username,password,name FROM login")
        records = mycursor.fetchall()
        print(records)
        for i, (username,password,name) in enumerate(records, start=1):
            listbox.insert("", "end", values=(username,password,name))
            connection.close()
    cols=("username","password","name")
    listbox=ttk.Treeview(f2,columns=cols,show='headings')
    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=0,column=0,columnspan=2)
        listbox.place(width=500,height=330)
    show()
    listbox.bind("<Double-Button-1>",GetValue)

#passanger data screen
def passanger_screen():
    global p1,a1,g1,p2,a2,g2,p3,a3,g3,p4,a4,g4,p5,a5,g5,p6,a6,g6,from_entry,to_entry,date_entry,passanger_value,c1,count
    
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



    p_from.set(passanger_value["ifrom"])
    p_to.set(passanger_value["ito"])
    p_date.set(passanger_value["date"])

    p_name.set(passanger_value["name"])
    p2_name.set(passanger_value["name2"])
    p3_name.set(passanger_value["name3"])
    p4_name.set(passanger_value["name4"])
    p5_name.set(passanger_value["name5"])
    p6_name.set(passanger_value["name6"])

    p_age.set(passanger_value["age"])
    p2_age.set(passanger_value["age2"])
    p3_age.set(passanger_value["age3"])
    p4_age.set(passanger_value["age4"])
    p5_age.set(passanger_value["age5"])
    p6_age.set(passanger_value["age6"])
   
    p_gender.set(passanger_value["gender"])
    p2_gender.set(passanger_value["gender2"])
    p3_gender.set(passanger_value["gender3"])
    p4_gender.set(passanger_value["gender4"])
    p5_gender.set(passanger_value["gender5"])
    p6_gender.set(passanger_value["gender6"])

    p_count.set(passanger_value["total"])

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
    def go():
        messagebox.showinfo("information", "passanger data inserted successfully...")
        passanger_screen()
    search_b = Button(pf1, text = 'save',bg='#FFA500',activebackground='black',font=("Times",10,"bold"), command = lambda :[pass_add(),go()])
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

    p2=Entry(pf2,textvariable=p2_name)
    p2.place(x=10,y=120,width=140,height=25)

    p3=Entry(pf2,textvariable=p3_name)
    p3.place(x=10,y=150,width=140,height=25)

    p4=Entry(pf2,textvariable=p4_name)
    p4.place(x=10,y=180,width=140,height=25)

    p5=Entry(pf2,textvariable=p5_name)
    p5.place(x=10,y=210,width=140,height=25)

    p6=Entry(pf2,textvariable=p6_name)
    p6.place(x=10,y=240,width=140,height=25)

    #age
    label2=Label(pf2,text='Age',bg='sky blue',font=font1)
    label2.place(x=160,y=60,width=40,height=25)
    a1=Entry(pf2,textvariable=p_age)
    a1.place(x=165,y=90,width=30,height=25)

    a2=Entry(pf2,textvariable=p2_age)
    a2.place(x=165,y=120,width=30,height=25)

    a3=Entry(pf2,textvariable=p3_age)
    a3.place(x=165,y=150,width=30,height=25)

    a4=Entry(pf2,textvariable=p4_age)
    a4.place(x=165,y=180,width=30,height=25)

    a5=Entry(pf2,textvariable=p5_age)
    a5.place(x=165,y=210,width=30,height=25)

    a6=Entry(pf2,textvariable=p6_age)
    a6.place(x=165,y=240,width=30,height=25)
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

    g2 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p2_gender) #readonly
    g2.place(x=220,y=120,width=40,height=25)
    g2.current(0)

    g3 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p3_gender) #readonly
    g3.place(x=220,y=150,width=40,height=25)
    g3.current(0)

    g4 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p4_gender) #readonly
    g4.place(x=220,y=180,width=40,height=25)
    g4.current(0)

    g5 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p5_gender) #readonly
    g5.place(x=220,y=210,width=40,height=25)
    g5.current(0)

    g6 = ttk.Combobox(pf2,state="readonly",values=gender,textvariable=p6_gender) #readonly
    g6.place(x=220,y=240,width=40,height=25)
    g6.current(0)


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
    l2.place(x=0,y=320,width=835,height=40)
    
    #label for num of passangers
    p_count=Label(pf2,text='Total passanger',bg='sky blue',font=font1)
    p_count.place(x=10,y=270,width=120,height=25)
    num_of_passanger = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6"
    ] 
        # Create Dropdown menu
    c1 = ttk.Combobox(pf2,state="readonly",values=num_of_passanger,textvariable=p_count) #readonly
    c1.place(x=10,y=290,width=40,height=25)
    c1.current(0)
    print(passanger_value)
    def pass_add():
        global date,count
        name = p1.get()
        name2 = p2.get()
        name3 = p3.get()
        name4 = p4.get()
        name5 = p5.get()
        name6 = p6.get()
       

        age = a1.get()
        age2 = a2.get()
        age3 = a3.get()
        age4 = a4.get()
        age5 = a5.get()
        age6 = a6.get()

        gender = g1.get()
        gender2 = g2.get()
        gender3 = g3.get()
        gender4 = g4.get()
        gender5 = g5.get()
        gender6 = g6.get()
  
        ifrom = from_entry.get()
        ito = to_entry.get()
        date = date_entry.get()
        count=c1.get()

        passanger_value["name"] = name
        passanger_value["name2"] = name2
        passanger_value["name3"] = name3
        passanger_value["name4"] = name4
        passanger_value["name5"] = name5
        passanger_value["name6"] = name6

        passanger_value["age"] = age
        passanger_value["age2"] = age2
        passanger_value["age3"] = age3
        passanger_value["age4"] = age4
        passanger_value["age5"] = age5
        passanger_value["age6"] = age6

        passanger_value["gender"] = gender
        passanger_value["gender2"] = gender2
        passanger_value["gender3"] = gender3
        passanger_value["gender4"] = gender4
        passanger_value["gender5"] = gender5
        passanger_value["gender6"] = gender6

        passanger_value["ifrom"] = ifrom
        passanger_value["ito"] = ito
        passanger_value["date"] = date
        passanger_value["total"]=count
        print("total number of passangers", c1.get())
        print(passanger_value)
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
        mycursor=mysqldb.cursor()
    
        try:
            my_conn.execute('''create table if not exists passanger_data(name text ,age text ,gender text ,
            name2 text ,age2 text ,gender2 text,
            name3 text ,age3 text ,gender3 text,
            name4 text ,age4 text ,gender4 text,
            name5 text ,age5 text ,gender5 text,
            name6 text ,age6 text ,gender6 text,
            ifrom text ,ito text ,date text)''')

            sql = '''INSERT INTO  passanger_data (NAME,AGE,GENDER,
            NAME2,AGE2,GENDER2,
            NAME3,AGE3,GENDER3,
            NAME4,AGE4,GENDER4,
            NAME5,AGE5,GENDER5,
            NAME6,AGE6,GENDER6,IFROM,ITO,DATE) VALUES (%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s)'''
            
            val = (name,age,gender,name2,age2,gender2,name3,age3,gender3,name4,age4,gender4,name5,age5,gender5,name6,age6,gender6,ifrom,ito,date)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            # def go():
            #     messagebox.showinfo("information", "passanger data inserted successfully...")
            #     passanger_screen()
            print(date)
            p1.delete(0, END)
            a1.delete(0, END)
            g1.delete(0, END)

            p2.delete(0, END)
            a2.delete(0, END)
            g2.delete(0, END)

            p3.delete(0, END)
            a3.delete(0, END)
            g3.delete(0, END)

            p4.delete(0, END)
            a4.delete(0, END)
            g4.delete(0, END)

            p5.delete(0, END)
            a5.delete(0, END)
            g5.delete(0, END)

            p6.delete(0, END)
            a6.delete(0, END)
            g6.delete(0, END)

            from_entry.delete(0, END)
            to_entry.delete(0, END)
            date_entry.delete(0, END)
            p1.focus_set()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

def payment_screen():
    global payment_value,upibutton,Debitbutton
    font1=tkfont.Font(family='Times', size=15, weight="bold")
    page3=Frame(root,bg='#80aaff', width=1200, height=550)
    page3.place(x=0,y=0)

    upibutton=Button(page3,text="UPI PAY",font=font1,bg='white',activebackground='black'
    ,activeforeground='white',width=30,command=lambda:upi())
    upibutton.place(x=70,y=10)

    Debitbutton=Button(page3,text="Debit PAY",font=font1,bg='white',activebackground='black'
    ,activeforeground='white',width=30,command=lambda:debit())
    Debitbutton.place(x=460,y=10)
   
    def upi():
        global upi_entry
        print(payment_value)


        
        upiframe=Frame(page3,bg='white',width=550, height=400,bd=5,highlightbackground="black", highlightthickness=1)
        upiframe.place(x=10,y=60)
        upi_label = Label(upiframe,text="Upi payment",font=font1,fg='#80aaff',bg='white')
        upi_label.place(x = 185, y = 55)

        upi_name=StringVar()
        temp_name=StringVar()
        upi_name.set(payment_value["upi"])
        temp_name.set(payment_value["temp_name"])

        upi_entry=Entry(upiframe,width=30,bd=2,font=font1,textvariable=upi_name)
        upi_entry.place(x=100,y=100)

        upi_temp = Label(upiframe,text="Give a name to save",font=font1,fg='#80aaff',bg='white')
        upi_temp.place(x = 105, y = 145)
        temp_entry=Entry(upiframe,width=30,bd=2,font=font1,textvariable=temp_name)
        temp_entry.place(x=100,y=180)

        upi_btn=Button(upiframe,text='Save',width=15,font=font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:Add())
        upi_btn.place(x=220,y=250)

        upi_del=Button(page3,text="Delete",width=10,font=font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:upi_delete())
        upi_del.place(x=600,y=450)

        upi_upd=Button(page3,text="update",width=10,font=font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:upi_update())
        upi_upd.place(x=800,y=450)

        select_upi=Button(page3,text="USE UPI",width=10,font=font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:method())
        select_upi.place(x=50,y=490)
        # upilist=Frame(page3,bg='white',width=550, height=450)
        # upilist.place(x=570,y=60)
        # add user and pass in database
        def method():
            upi = upi_entry.get()
            name=temp_entry.get()
            payment_value["upi"] = upi
            payment_value["temp_name"] = name
            print(payment_value)
        def GetValue(event):
            upi = upi_entry.get()
            name=temp_entry.get()
            payment_value["upi"] = upi
            payment_value["temp_name"] = name
            upi_entry.delete(0, END)
            temp_entry.delete(0, END)

            row_id=listbox.selection()[0]
            select=listbox.set(row_id)
           
            upi_entry.insert(0,select['upi'])
            temp_entry.insert(0,select['name'])
        def Add():
            
            upi = upi_entry.get()
            name=temp_entry.get()
            payment_value["upi"] = upi
            payment_value["temp_name"] = name
            print(payment_value)
            
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()
        
            try:
                mycursor.execute('''create table if not exists upi_data(id int(15) auto_increment ,upi text,name text,primary key(id))''')
                sql = "INSERT INTO upi_data (ID,UPI,NAME) VALUES  (%s,%s,%s)"
                val = (0,upi,name)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "upi inserted successfully...")
                upi_entry.delete(0, END)
                temp_entry.delete(0, END)
                upi_entry.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        # update user and pass in database
        def upi_update():
            upi = upi_entry.get()
            name=temp_entry.get()
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()
        
            try:
                sql = "Update upi_data set upi= %s where name=%s"

                val = (upi,name)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "upi Updated successfully...")
                upi_entry.delete(0, END)
                temp_entry.delete(0, END)
                upi_entry.focus_set()
        
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        # # delete user and pass from database
        def upi_delete():
            upi = upi_entry.get()
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()
            try:
                sql = "delete from upi_data where upi = %s"
                val = (upi,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "upi Deleteeeee successfully...")
                upi_entry.delete(0, END)
                temp_entry.delete(0, END)
                upi_entry.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        # show user and pass in list
        def show():
            
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
            mycursor = mysqldb.cursor()
            try:
                mycursor.execute("SELECT id,upi,name FROM upi_data")
            except Exception as e:
                print(e)
            records = mycursor.fetchall()
            print(records)
            for i, (id,upi,name) in enumerate(records, start=1):
                listbox.insert("", "end", values=(id,upi,name))
                mysqldb.close()
        cols=("id","upi","name")
        listbox=ttk.Treeview(page3,columns=cols,show='headings')
        listbox.column('id', anchor=CENTER, width=3)
        listbox.column('upi', anchor=CENTER, width=120)
        listbox.column('name', anchor=CENTER, width=90)
        for col in cols:
            listbox.heading(col, text=col)
            listbox.place(x=570,y=60)
            listbox.place(width=600,height=330)
        show()
        listbox.bind("<Double-Button-1>",GetValue)


    def debit():
        global debit_e1,debit_e2,debit_e3,debit_M,debit_Y,debit_e5,cvv,pass3d
        font2=tkfont.Font(family='Times New Roman', size=15, weight="bold")
        Debitframe=Frame(page3,bg='white',width=550, height=400,bd=5,highlightbackground="black", highlightthickness=1)
        Debitframe.place(x=10,y=60)

        # bank_name = StringVar()
        # card_type = StringVar()
        # card_no = StringVar()
        # valid_M = StringVar()
        # valid_y = StringVar()
        # name_on_card = StringVar()
        # cvv = StringVar()
        # pass3d = StringVar()
        # name = StringVar()

        bank_name = Label(Debitframe,text="Bank Name :",font=font2,bg='white')
        bank_name.place(x = 25, y = 10)
        debit_e1=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
        debit_e1.place(x=270,y=10)

        card_type = Label(Debitframe,text="Card Type :",font=font2,bg='white')
        card_type.place(x = 25, y = 50)
        debit_e2=Entry(Debitframe,width=15,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
        debit_e2.place(x=270,y=50)

        card_no = Label(Debitframe,text="Card Number :",font=font2,bg='white')
        card_no.place(x = 25, y = 90)
        debit_e3=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
        debit_e3.place(x=270,y=90)

        valid = Label(Debitframe,text="Expiry mm/yy :",font=font2,bg='white')
        valid.place(x = 25, y = 130)
        debit_M=Entry(Debitframe,width=6,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
        debit_M.place(x=270,y=130)

        debit_Y=Entry(Debitframe,width=6,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
        debit_Y.place(x=390,y=130)

        name_on_card = Label(Debitframe,text="Name On Card :",font=font2,bg='white')
        name_on_card.place(x = 25, y = 170)
        debit_e5=Entry(Debitframe,width=25,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
        debit_e5.place(x=270,y=170)

        cvv = Label(Debitframe,text="CVV :",font=font2,bg='white')
        cvv.place(x = 25, y = 210)
        debit_e6=Entry(Debitframe,width=7,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
        debit_e6.place(x=270,y=210)

        pass3d = Label(Debitframe,text="3D Password :",font=font2,bg='white')
        pass3d.place(x = 25, y = 250)
        debit_e7=Entry(Debitframe,width=10,font=font2,bd=1,highlightbackground="grey", highlightthickness=1)
        debit_e7.place(x=270,y=250)

        

        debit_btn=Button(Debitframe,text='Save',width=15,font=font1,fg='white',bg='black',activebackground='white'
        ,activeforeground='black',command=lambda:add_debit())
        debit_btn.place(x=270,y=340)

        select_upi=Button(page3,text="USE DEBIT",width=10,font=font1,bg='white',activebackground='black'
        ,activeforeground='white',command=lambda:method())
        select_upi.place(x=50,y=490)

        def method():
            pass
        #function for get username and password from entry
        def GetValue(event):
            
            debit_e1.delete(0, END)
            debit_e2.delete(0, END)
            debit_e3.delete(0, END)
            debit_M.delete(0, END)
            debit_Y.delete(0, END)
            debit_e5.delete(0, END)
            debit_e6.delete(0, END)
            debit_e7.delete(0, END)

            row_id=listbox.selection()[0]
            select=listbox.set(row_id)
            #Bank","Card_type","Card_num","month","year","owner","cvv","pass3d","Name
            debit_e1.insert(0,select['Bank'])
            debit_e2.insert(0,select['Card_type'])
            debit_e3.insert(0,select['Card_num'])
            debit_M.insert(0,select['month'])
            debit_Y.insert(0,select['year'])
            debit_e5.insert(0,select['Holder'])
            debit_e6.insert(0,select['cvv'])
            debit_e7.insert(0,select['pass3d'])
        
        def add_debit():
            
            bank_name = debit_e1.get()
            card_type = debit_e2.get()
            card_number = debit_e3.get()
            validity_m = debit_M.get()
            validity_y = debit_Y.get()
            holder = debit_e5.get()
            cvv = debit_e6.get()
            pass3d = debit_e7.get()
            
            
    
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="deol9646",database="train_login")
            mycursor=mysqldb.cursor()
        
            try:
                mycursor.execute('''create table if not exists debit_data(bank_name text,card_type text,card_number text,
                validity_m text,validity_y text,holder text,cvv text,pass3d text)''')
                sql = "INSERT INTO debit_data ( BANK_NAME,CARD_TYPE,CARD_NUMBER,VALIDITY_M,VALIDITY_Y,HOLDER,CVV,PASS3D ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (bank_name,card_type,card_number,validity_m,validity_y,holder,cvv,pass3d)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "DEBIT CARD inserted successfully...launch app again to watch")
                debit_e1.delete(0, END)
                debit_e2.delete(0, END)
                debit_e3.delete(0, END)
                debit_M.delete(0, END)
                debit_Y.delete(0, END)
                debit_e5.delete(0, END)
                debit_e6.delete(0, END)
                debit_e7.delete(0, END)
                debit_e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def debitshow():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="deol9646", database="train_login")
            mycursor = mysqldb.cursor()
            try:
                mycursor.execute("SELECT bank_name,card_type,card_number,validity_m,validity_y,holder,cvv,pass3d FROM debit_data")
            except Exception as e:
                print(e)
            records = mycursor.fetchall()
            print(records)
            for i, (bank_name,card_type,card_number,validity_m,validity_y,holder,cvv,pass3d) in enumerate(records, start=1):
                listbox.insert("", "end", values=(bank_name,card_type,card_number,validity_m,validity_y,holder,cvv,pass3d))
                mysqldb.close()
        cols=("Bank","Card_type","Card_num","month","year","Holder","cvv","pass3d")
        
        listbox=ttk.Treeview(page3,columns=cols,show='headings')
        listbox.column('Bank', anchor=CENTER, width=60)
        listbox.column('Card_type', anchor=CENTER, width=50)
        listbox.column('Card_num', anchor=CENTER, width=80)
        listbox.column('month', anchor=CENTER, width=30)
        listbox.column('year', anchor=CENTER, width=30)
        listbox.column('Holder', anchor=CENTER, width=80)
        listbox.column('cvv', anchor=CENTER, width=40)
        listbox.column('pass3d', anchor=CENTER, width=50)

        for col in cols:
            listbox.heading(col, text=col)
            listbox.place(x=570,y=60)
            listbox.place(width=600,height=330)
        debitshow()
        listbox.bind("<Double-Button-1>",GetValue)

def fourth_screen():
    page4=Frame(root,bg='green', width=1200, height=550)
    page4.place(x=0,y=0)
    test = Label(page4,text="HOME")
    test.place(x = 50, y = 50)

Button1=Button(root,text='LOGIN',command=lambda:login_screen())
Button1.place(x=10,y=570)
Button2=Button(root,text='PASSSENGER',command=lambda:passanger_screen())
Button2.place(x=65,y=570)
Button3=Button(root,text='PAYMENT',command=lambda:payment_screen())
Button3.place(x=155,y=570)
Button3=Button(root,text='HOME',command=lambda:fourth_screen())
Button3.place(x=230,y=570)


root.mainloop()