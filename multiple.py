# Necessary webdrivers ned to be imported
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options 
import os
# This is for Firefox. Similarly if
# chrome is needed , then it has to be specified
try:    
    os.chdir('C:\\Program Files\\Google\\Chrome\\Application')
    os.system('start cmd /k "chrome.exe --remote-debugging-port=9222 --user-data-dir=E:\chromedriver_win32\chromedata"')
except:
    print('re check path')
opt = Options()
opt.add_experimental_option("debuggerAddress",'localhost:9222')
driver=webdriver.Chrome(executable_path=r"E:\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
# first tab. Open google.com in the first tab
driver.get('https://checkout.razorpay.com/orders/order_KcGuQSlhKnWR3H?x_ranid=KcGuQ5bIOFct8t')
driver.maximize_window()
# second tab
# execute_script->Executes JavaScript snippet.
# Here the snippet is window.open that means, it
# opens in a new browser tab
# driver.execute_script("window.open('about:blank','secondtab');")

# # It is switching to second tab now
# driver.switch_to.window("secondtab")
# print('second tab open')
# In the second tab, it opens geeksforgeeks
# driver.get('https://checkout.razorpay.com/orders/order_KcGuQSlhKnWR3H?x_ranid=KcGuQ5bIOFct8t')
time.sleep(5)
 #upi or QR
iframe = driver.find_element(By.XPATH,"//iframe[@class='razorpay-checkout-frame']")
driver.switch_to.frame(iframe)
roserpay = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div[3]/form/div[2]/div[1]/div[1]/div/div/div/div/div/button[1]')
roserpay.click()
print('upi or QR')
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
action.send_keys('sarbjitdeol@ybl')
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