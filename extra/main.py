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
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import PIL.Image
from PIL import Image,ImageFilter
from functools import partial
import pytesseract
import os
from tkcalendar import DateEntry
import multiprocessing
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import mysql.connector
import cv2
import sys
import requests
import base64

import time ,os
from selenium.webdriver.common.action_chains import ActionChains
from fp.fp import FreeProxy
from fake_useragent import UserAgent
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
var=os.getcwd()



# class Spoofer(object):

#     def __init__(self, country_id=['US'], rand=True, anonym=True):
#         self.country_id = country_id
#         self.rand = rand
#         self.anonym = anonym
#         self.userAgent, self.ip = self.get()

#     def get(self):
#         ua = UserAgent()
#         proxy = FreeProxy(country_id=self.country_id, rand=self.rand, anonym=self.anonym).get()
#         ip = proxy.split("://")[1]
#         return ua.random, ip


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument("disable-infobars")
options.add_argument('--remote-debugging-port=9223 ')
options.add_argument(f'--user-data-dir={var}\chrome\chromedata3')
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"


# options.binary_location = brave_path
# helperSpoofer = Spoofer()
# print("""
#         IP:{}
#         UserAgent: {}
#         """.format(helperSpoofer.ip, helperSpoofer.userAgent))

# PROXY = helperSpoofer.ip
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "noProxy":None,
#     "proxyType":"MANUAL",
#     "autodetect":False
# }
# webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True



driver = webdriver.Chrome(executable_path=f"E:\\PYTHON\\irctc_v3\\chrome\\chromedriver.exe", chrome_options=options)
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source":
#         "const newProto = navigator.__proto__;"
#         "delete newProto.webdriver;"
#         "navigator.__proto__ = newProto;"
# })

# options.add_argument('user-agent={}'.format(helperSpoofer.userAgent))
# options.add_argument('--proxy-server=%s' % helperSpoofer.ip)

driver.set_window_size(50, 600)
driver.get("https://www.irctc.co.in/nget/train-search")
wait=WebDriverWait(driver, 10)
try:
    #get element for login button  
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/div/a[2]'))).click()
    print('login click')
    
    #ads click
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/img'))).click()
        # element2 = driver.find_element(By.XPATH, '/html/body/div[4]/img')
        # element2.click()
    print('ad click')
        
    time.sleep(1)
    
except:
    print('page 1 not reload, Unable to locate element login button  ')
    # log_obj.exception("Unable to locate element login button") 
    driver.quit()
# log_obj.info("username click")
time.sleep(1)
try:
    #get element for usernme
    element3=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/input')))
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = element3)
    # send keys
    action.send_keys('sarbdeoll') #e1.get()
    # perform the operation
    action.perform()
    print('username 1 entered')
    # log_obj.info("username entered")
    
except Exception as e:
    # log_obj.exception("error in username enter")
    print(e)
try:
    
    # log_obj.info("password element find")
    # get element for password
    element4=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/input')))
    # create action chain object
    action2 = ActionChains(driver)
    # click the item
    action2.click(on_element = element4)
    # send keys
    action2.send_keys('Deol9646@')
    # perform the operation
    action2.perform()
    
    print('password 1 entered')
    # log_obj.info("password entered")
  
except Exception as e:
    # log_obj.exception("error in username enter")
    print(e)

#----- function for captcha------
def  logincaptcha():
    img=driver.find_element(By.ID, "nlpImgContainer") #By.ID, "nlpImgContainer" '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img'
    img.screenshot(f"{var}\logo.png")
    im = Image.open(f"{var}\logo.png") #use PIL.Image.open if not work
    left = 0
    top = 250
    right = 300
    bottom = 270
    # left = 0
    # top = 50
    # right = 300
    # bottom = 270

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im1.save(f"{var}\crop2.png" ,quality=100)
    print('image address:',im1) 
    captcha = pytesseract.image_to_string(im1) 
    captcha = captcha.replace(" ", "").strip()
    # save in abc.txt file
    with open(f"{var}\\abc2.txt",mode ='w') as file:     
        file.write(captcha) 
        print('result',captcha)
        print('write result',captcha[18:22]) #5:14 paints  [18:22] default  5:12match

    #get element for captcha enter
    element5 = driver.find_element(By.XPATH, "//*[@id='nlpAnswer']")
    print('find')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = element5)
    # enter captcha
    action.send_keys(captcha[18:22]) #[18:22]]
    action.perform()
    print('captcha enter 1')
    time.sleep(1)
    # click signup button 
    signup = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button')
    signup.click()
    print('signup 2')
    time.sleep(5)
# log_obj.info("getting login captcha")
def logincaptcha2():
    print('logincaptcha 2')
    img=driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img')
    img.screenshot(f"{var}\logo.png")
    
    
    with open(f"{var}\logo.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('ascii')
        
        url = 'https://api.apitruecaptcha.org/one/gettext'

        data = { 
            'userid':'sarbjitdeol72@gmail.com', 
            'apikey':'hAWX2MbYjpViHGSVhYPX',  
            'data':encoded_string,
            'mode':'human'
        }
        response = requests.post(url = url, json = data)
        data = response.json()
        captcha=data['result']
        print('login captcha 2',captcha)


    #get element for captcha enter
    element5 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/input")
    print('find')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = element5)
    # enter captcha
    action.send_keys(captcha) #[18:22]]
    action.perform()
    print('captcha enter')
    # log_obj.info("captcha entered")
    # time.sleep(2)
    # click signup button 
    signup = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button')
    signup.click()
    print('signup 1')
    
    time.sleep(5)
    # try:
    #     if driver.find_element(By.XPATH, "//*[@id='jDate']/span/input").is_displayed==False:
    #         time.sleep(5)
    # except:
    #     pass
def check_captcha():
    
    
    try:
        if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
            print("blue image captcha show")
            # log_obj.info("blue image captcha show")
            logincaptcha2()
    
    except Exception as e:
        print('error in captcha 2 load')
            # log_obj.exception("error in captcha 2 load")
    
check_captcha()

def error_check():
    for i in range(0,3):
        try:
            if driver.find_element(By.XPATH,'//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[1]').is_displayed()==True:
                print('again enter')
                time.sleep(0.5)

                logincaptcha2()
        
                
            elif driver.find_element(By.XPATH,'//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[1]').is_displayed()==False:
                print('captcha is correct')
        except:
            print('captcha is corrects')
error_check()
# log_obj.info("login done")

try:
    # log_obj.info("getting FROM route element")
    #tap on from route
    loc = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="origin"]/span/input')))
    
    # time.sleep(.5)
    # create action chain object
    action = ActionChains(driver)
    # click the from route
    action.click(on_element = loc)
    # enter from location
    action.send_keys('hwh')
    action.perform()
    time.sleep(.5)
    loc2 = driver.find_element(By.XPATH, '//*[@id="pr_id_1_list"]/li/span')
    loc2.click()
   
except:
    # log_obj.exception("error in <FROM> route")
    # driver.quit()
    print('loc 1 error')
try:
    # log_obj.info("getting TO route element")
    #tap on to route
    loc3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="destination"]/span/input')))
    # loc3.click()
    # time.sleep(.5)
    # create action chain object
    action = ActionChains(driver)
    # click the to location
    action.click(on_element = loc3)
    # enter destination 
    action.send_keys('ypr')
    action.perform()
    time.sleep(.5)
    # click destination location
    loc4 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pr_id_2_list"]/li[1]')))
    loc4.click()
    # time.sleep(.5)
except:
    # log_obj.exception("error in <TO> route select")
    # driver.quit()
    print('error in loc 2')

try:
    # log_obj.info("getting date element")
    #tap on date 
    date_e = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='jDate']/span/input")))
    date_e.click()
    time.sleep(0.3)
    # create action chain object
    action = ActionChains(driver)
    # # click the date
    action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
    # write date
    action.send_keys('08/01/2023')
    action.perform()
    time.sleep(.7)
except:
    # log_obj.exception("error in date enter")
    driver.quit()

try:
    loc = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
    loc.click()
    # journey qauta
    def general():
        pass
    
    def tatkal():
        #tatkal box
        # log_obj.info("tatkal click")
        tatkal = driver.find_element(By.XPATH, '//*[@id="journeyQuota"]/div')
        tatkal.click()

        tatkal_ = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="journeyQuota"]/div/div[4]/div/ul/p-dropdownitem[5]/li')))
        tatkal_.click()
    tatkal()
except:
    # log_obj.exception("error in qouta select")
    driver.quit()

# if qouta=="GENERAL":
#     general()
# elif qouta=="TATKAL":
#     tatkal()

try:
    # log_obj.info("train search start")
    #SEARCH buttton click
    search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div/button')))
    search.click()
    # time.sleep(4)
except:
    # log_obj.exception("Error in train search button")
    driver.quit()

# # check refresh button show or not
# if driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]/span').is_displayed==False:
#     time.sleep(4)
#     print('wait')
# else:
#     pass

try:
    # log_obj.info("refresh train button")
    #refresh button
    refresh = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]/span')))
    refresh.click()
    # time.sleep(2)
except:
    # log_obj.exception(" error in refresh train button")
    driver.quit()
# loading icon show
# try:
#     if wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="preloaderP"]'))).is_displayed()==True:
#         print('loading 2')
#         # log_obj.info("loading 2")
#         time.sleep(4)
# except:
#     time.sleep(2)
try:
    # log_obj.info("choose train button")
    #choose train
    choose = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[7]/div[1]/div[3]/table/tr/td[2]/div/div[2]/strong')))
    choose.click()
    # time.sleep(0.5)
except:
    # log_obj.exception("error in choose train")
    driver.quit()

try:
    # log_obj.info("book button")
    #book
    book = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button')))
    book.click()
    time.sleep(3)
except:
    # log_obj.exception("error in book button click")
    driver.quit()

try:
    if driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button').is_enabled()==True:
        print('book button is disabled')
        # log_obj.exception("book button is disabled")
        driver.quit()
        
    else:
        print('booking....')
except:
    # messagebox.showinfo('','login again')
    print('book')
try:
    if driver.find_element(By.XPATH, '//*[@id="preloaderP"]').is_displayed()==True:
        print('loading 2')
        time.sleep(5)
except:
    time.sleep(2)
# ---function of passangers 1 2 3 4 5 6------
def pass1():
    # log_obj.info("passanger 1 detail filling")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try:
        #enter passanger name
        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(.5)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys('name')
        action.perform()
        time.sleep(.2)
        # log_obj.info("name enter")
    except:
        # log_obj.exception("error in first passanger name")
        driver.quit()
    
    try:
        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(.3)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys('12')
        action.perform()
        time.sleep(.5)
        # log_obj.info("age enter")
    except:
        # log_obj.exception("error in first passanger age")
        driver.quit()
    try:
        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(.5)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()
        # log_obj.info("gender select")
    except:
        # log_obj.exception("error in first passanger gender")
        driver.quit()
    try:
        if driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select').is_displayed()==True:
            try:
                #food box
                food = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select')
                food.click()
                time.sleep(1)
                #veg choose
                food_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select/option[2]')
                food_select.click()
                time.sleep(1)
                # log_obj.info("food choose")
            except:
                # log_obj.exception("error in first passanger food choose")
                # driver.quit()
                print('error in food')
    except:
        print('food is not serve in selected train')
    try:
        if driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select').is_displayed()==True:
            try:
                #food box
                food = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select')
                food.click()
                time.sleep(1)
                #veg choose
                food_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select/option[2]')
                food_select.click()
                time.sleep(1)
                # log_obj.info("food choose")
            except:
                # log_obj.exception("error in first passanger food choose")
                driver.quit()
    except:
        print('food is not serve in selected train')
        


# ------condition of passanger count-----------

pass1()

#upi select
def upi_function():
    try:
        # log_obj.info("upi payment start")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        pay = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="2"]/div/div[2]/span'))) # for upi
        pay.click()
       
    except:
        # log_obj.exception("error in selecting upi payment")
        driver.quit()

    try:
        #continue button same for both
        submit = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="psgn-form"]/form/div/div[1]/p-sidebar/div/div/div[2]/button')))
        submit.click()
        time.sleep(4)
        # try:
        #     if driver.find_element(By.XPATH, '//*[@id="preloaderP"]').is_displayed()==True:
        #         print('loading 2')
        #         time.sleep(10)
        #         try:
        #             if driver.find_element(By.XPATH, '//*[@id="preloaderP"]').is_displayed()==True:
        #                 print('loading 2')
        #                 time.sleep(5)
        #         except:
        #             pass
        # except:
        #     pass
    except:
        # log_obj.exception("error in upi continue button")
        driver.quit()

    #payment captcha page
    try:
        print('payment captcha page')
        # log_obj.info("upi payment captcha page")
        #payment captcha 
        def paycaptcha():
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            img=driver.find_element(By.ID, "nlpImgContainer")
            img.screenshot(f"{var}\logo2.png")
            im = Image.open(f"{var}\logo2.png")
            left = 0
            top = 250
            right = 300
            bottom = 280
            # Cropped image of above dimension
            # (It will not change original image)
            im1 = im.crop((left, top, right, bottom))
            im1.save(f"{var}\crop2.png" ,quality=100)
            print('image address:',im1) 
            captcha = pytesseract.image_to_string(im1) 
            captcha = captcha.replace(" ", "").strip()

            #save in payment.txt
            with open(f"{var}\payment2.txt",mode ='w') as file:      
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
            time.sleep(1)
            # send keys
            action.send_keys(captcha[18:22])
            action.perform()
            print('payement captcha enter')
            time.sleep(3)

            #continue buttton
            continue_button = driver.find_element(By.XPATH, '//*[@id="review"]/div[1]/p-sidebar/div/div/div[2]/button')
            continue_button.click()
            print('continue_button')
            time.sleep(3)
        
        def paycaptcha2():
            print('paycaptcha 2')
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            img=driver.find_element(By.XPATH,'//*[@id="review"]/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img')
            img.screenshot(f"{var}\logo2.png")
            
            with open(f"{var}\logo2.png", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('ascii')
                
                url = 'https://api.apitruecaptcha.org/one/gettext'

                data = { 
                    'userid':'sarbjitdeol72@gmail.com', 
                    'apikey':'hAWX2MbYjpViHGSVhYPX',  
                    'data':encoded_string,
                    'mode':'human'
                }
                response = requests.post(url = url, json = data)
                data = response.json()
                captcha=data['result']
                print('payment 2',captcha)

            #get element for captcha enter
            element5 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/input")
            print('find')
            # create action chain object
            action = ActionChains(driver)
            # click the item
            action.click(on_element = element5)
            # enter captcha
            action.send_keys(captcha) #[18:22]]
            action.perform()
            print('captcha enter')
            # log_obj.info("upi payment captcha enter")
            # time.sleep(.5)
            
            #continue buttton
            continue_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="review"]/div[1]/p-sidebar/div/div/div[2]/button')))
            continue_button.click()
            print('continue_button')
            # log_obj.info("upi continue_button")
            time.sleep(3)
            if driver.find_element(By.XPATH, '//*[@id="pay-type"]/span/div[1]/span').is_displayed==False:
                paycaptcha2()
            else:
                pass
        def check_pay_captcha():
 
            try:
                if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                    print("blue image pay captcha show")
                    paycaptcha2()
            
            except Exception as e:
                print('error in captcha 2 load')
                # log_obj.exception("error in captcha 2 load")
        check_pay_captcha()
        
   
        def error_check():
            try:
                for i in range(3):
            
                    try:
                        if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                            print("agin enter second captcha")
                            paycaptcha2()
                    except Exception as e:
                        print('error in captcha 2 load')
                        # log_obj.exception("error in captcha 2 load")
                        
            except:
                print('captcha is corrects')
        error_check()
    except:
        # log_obj.exception("error in payment captcha page")
        driver.quit()

    try:
        #choose method to pay
        # log_obj.info("Multiple Payment Service")
        #choose multiple payment method //*[@id="pay-type"]/span/div[1]/span
        upi_choose =wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pay-type"]/span/div[1]/span')))
        upi_choose.click()
        print('Multiple Payment Service')
        # time.sleep(1)
    except:
        # log_obj.exception("error in Multiple Payment Service")
        driver.quit()
    try:
        cont =wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="psgn-form"]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[2]/div/div/div[2]/button')))
        cont.click()
        print('continue')
        # time.sleep(3)
    except:
        # log_obj.exception("error in Multiple Payment Service contine")
        driver.quit()
    #roserpay select 
    try:
        
        # log_obj.info("roserpay method")
        roserpay = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-payment-options/div[4]/div[2]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[1]/div/div/div[1]/div[2]/app-bank/div/div/table/tr/span[3]/td/div/div/span')))
        roserpay.click()
        print('choose roserpay method')
        
    except:
        # log_obj.exception("error in roserpay select")
        driver.quit()

    #pay & book button
    try:
        # log_obj.info("getting pay & book button")
        pay = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-payment-options/div[4]/div[2]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[1]/div/div/div[2]/div[2]/button')))
        pay.click()
        print('pay & book button')
       
    except:
        # log_obj.exception("error in pay & book button")
        driver.quit()

    try:
        
        print('enter payment iframe')
        iframe = wait.until(EC.presence_of_element_located((By.XPATH,"//iframe[@class='razorpay-checkout-frame']")))
        driver.switch_to.frame(iframe)
  
    except:
        # log_obj.exception("error in getting payment page")
        driver.quit()

    #upi or QR
    
    try:
        # log_obj.info("click upi or QR")
        qr = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-common"]/div[1]/div[1]/div/div/div/div/button[1]/div/div[1]/div[1]/div[1]')))
        qr.click()
        print('upi or QR')
      
    except:
        # log_obj.exception("error click on upi or QR")
        print('error click on upi or QR')
        driver.quit()
    
    #click and add upi
    try:
        # log_obj.info("click upi add button")
        conti_confirm = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="vpa-upi"]')))
        conti_confirm.click()
        print('click upi add button')
        # create action chain object
        action = ActionChains(driver)
        # click the item
        # action.click(on_element = conti_confirm)
        # send keys
        # action.send_keys(upi_value["upi"])
        action.send_keys('sarbjitdeol@ybl')
        action.perform()
  
        # log_obj.info("upi added ")
    except:
        # log_obj.exception("error in upi id enter ")
        driver.quit()

    #proceed button to upi pay  
    try:
        pay_now = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="footer-cta"]')))
        pay_now.click()
        print(' pay now button')
        # log_obj.info("pay now button click")
   
    except:
        try:
            pay_now = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="redesign-v15-cta"]')))
            pay_now.click()
            print(' pay button')
            # log_obj.info("pay button click")
        
        except:
            # log_obj.exception("error in pay button click ")
            driver.quit()
    #continue for mobile pay send 
    try:
        contine_pay = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="overlay"]/div/div/div[2]')))
        contine_pay.click()
        print(' continue button')
        # log_obj.info("mobile link sending")

    except:
        try:
            contine_pay = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="overlay"]/div[2]/div/div[2]')))
            contine_pay.click()
            print(' continue button')
            # log_obj.info("mobile link sending")
        
        except:
            # log_obj.exception("error in continue and pay button click ")
            driver.quit()
upi_function()