# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
import PIL.Image
from PIL import Image,ImageFilter
from tkinter import *
from functools import partial
from tkinter import font  as tkfont
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#configure webdriver manager
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
    action.send_keys("sarbdeoll")

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
    action.send_keys("Deol9646@")

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


    # get element of ok 
    signup = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button")
    signup.click()
    print('signup')
    time.sleep(6)
    #tap on date 
    date = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input")
    date.click()
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = date)
    action.double_click(on_element = date)
    # send keys
    action.send_keys("29/09/2022")
    action.perform()
    time.sleep(2)
    #tap on from route
    loc = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete')
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
    loc1 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/div/ul/li[1]')
    loc1.click()
    time.sleep(2)
    #tap on from route
    loc3 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/input')
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
    loc4 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/div/ul/li[1]/span")
    loc4.click()
    time.sleep(2)
    #SEARCH
    search = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button")
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
def data():
    global v1,v2
    
    v1=StringVar()
    v2=StringVar()
    
    v1=username.get()

    v2=password.get()
    
    # print(e1)
    # print(e2)
    
    # e1=input('enter the usernam')
    # e2=input('password')
    print(v1)
    print(v2)
    #database connection
    import mysql.connector
    connection=mysql.connector.connect(host='localhost',username='root',password='deol9646',database="train_login")
    cursor=connection.cursor()
    print('successfully connected')

    
    try:  
    #creating a new table  
        cursor.execute('''create table if not exists login(username text ,password text)''')

        cursor.execute('''INSERT INTO LOGIN(USERNAME, PASSWORD) 
        VALUES (%s ,%s)''',(v1, v2)) 
        connection.commit()
        
    except:  
        connection.rollback()
        print('rollback') 
    for x in cursor:  
        print(x)
    



#tkinter window

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
#window
tkWindow = Tk()  
tkWindow.geometry('400x280')  
tkWindow.configure(bg='white')
tkWindow.title('irctc.co.in')

# create a Form label 
Label(text="Login Here",font=("impact",30,"bold"),fg='sky blue',bg='white').pack() 
Label(text="", bg='white').pack() 
 


#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name",bg='white').pack() 
Label(text="",bg='white').pack() 
 
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username,bg='lightgray').pack()
Label(text="",bg='white').pack() 
 

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",bg='white').pack() 
Label(text="",bg='white').pack() 
   
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*' ,bg='lightgray').pack() 
Label(text="",bg='white').pack() 
 

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=lambda:[data(),start()]).pack() 

 



tkWindow.mainloop()



#print(element)




