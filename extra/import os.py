import os 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
try:    
    os.chdir('C:\\Program Files\\Google\\Chrome\\Application')
    os.system('start cmd /k "chrome.exe --remote-debugging-port=9222 --user-data-dir=E:\chromedriver_win32\chromedata"')
except:
    print('done')

opt = Options()
opt.add_experimental_option("debuggerAddress",'localhost:9222')
driver=webdriver.Chrome(executable_path=r"E:\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)


driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")
