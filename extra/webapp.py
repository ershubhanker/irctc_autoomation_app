# import required library
import webbrowser
from tkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
import time
# creating root
# root = Tk()

# # setting GUI title
# root.title("WebBrowsers")

# # setting GUI geometry
# root.geometry("660x660")

# # call webbrowser.open() function.
# driver=webbrowser.open("www.instagram.com")

# Import tkinter and webview libraries
from tkinter import *
import webview

# define an instance of tkinter
tk = Tk()

# size of the window where we show our website
tk.geometry("800x450")

# Open website
webview.create_window('Geeks for Geeks', 'https://geeksforgeeks.org')
webview.start()
# click ok 
