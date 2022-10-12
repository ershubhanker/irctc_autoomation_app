# Necessary webdrivers ned to be imported
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# This is for Firefox. Similarly if
# chrome is needed , then it has to be specified
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# first tab. Open google.com in the first tab
driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()
# second tab
# execute_script->Executes JavaScript snippet.
# Here the snippet is window.open that means, it
# opens in a new browser tab
driver.execute_script("window.open('about:blank','secondtab');")

# It is switching to second tab now
driver.switch_to.window("secondtab")

# In the second tab, it opens geeksforgeeks
driver.get('https://www.irctc.co.in/nget/train-search')

#driver.maximize_window()



# get element of ok 
element = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button")
element.click()
time.sleep(1)
print('clicked ok')
while True:
    pass
# #tap on date 
# date = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input")
# date.click()
# time.sleep(1)
# # create action chain object
# action = ActionChains(driver)
# # click the item
# action.click(on_element = date)
# action.double_click(on_element = date)
# # send keys

# action.send_keys("12/10/2022")
# action.perform()
# time.sleep(2)
# #tap on from route
# loc = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
# loc.click()
# time.sleep(2)
# # create action chain object
# action = ActionChains(driver)
# # click the item
# action.click(on_element = loc)
# # send keys

# action.send_keys('12345')
# action.perform()
# time.sleep(2)
# #from location
# loc1 = driver.find_element(By.XPATH, '//*[@id="pr_id_1_list"]/li/span')
# loc1.click()
# time.sleep(2)