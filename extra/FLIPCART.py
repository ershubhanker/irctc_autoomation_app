from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import os
try:    
    os.chdir('C:\\Program Files\\Google\\Chrome\\Application')
    os.system('start cmd /k "chrome.exe --remote-debugging-port=9222 --user-data-dir=E:\chromedriver_win32\chromedata"')
except:
    print('re check path')
opt = Options()
opt.add_experimental_option("debuggerAddress",'localhost:9222')
driver=webdriver.Chrome(executable_path=r"E:\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)


driver.maximize_window()
driver.get("https://checkout.razorpay.com/orders/order_KbFikMZG6JiALT?x_ranid=KbFijl3RTloKTB")

#upi or QR
try:
    roserpay = driver.find_element(By.XPATH, '//*[@id="form-common"]/div[1]/div/div/div/div/div/button[1]/div/div[1]')
    roserpay.click()
    print('upi choose roserpay')
    time.sleep(2)
except:
    print('take in your hands')


#click and add upi
conti_confirm = driver.find_element(By.XPATH,'//*[@id="vpa-upi"]')
conti_confirm.click()
print('add payment number')
# create action chain object
action = ActionChains(driver)
# click the item
action.click(on_element = conti_confirm)
# send keys
action.send_keys('sarbdeol@ybl')
action.perform()
time.sleep(2)