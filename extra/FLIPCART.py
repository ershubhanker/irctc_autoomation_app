from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
opt = Options()
opt.add_experimental_option("debuggerAddress",'localhost:9222')
driver=webdriver.Chrome(executable_path=r"E:\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
driver.get('https://www.irctc.co.in/nget/train-search')