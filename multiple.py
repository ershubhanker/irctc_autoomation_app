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
import threading,multiprocessing
var=os.getcwd()
# This is for Firefox. Similarly if
# chrome is needed , then it has to be specified

def one():
    
        try:    
            os.chdir('C:\\Program Files\\Google\\Chrome\\Application')
            os.system('start cmd /k "chrome.exe --remote-debugging-port=9221 --user-data-dir=E:\chromedriver_win32\chromedata"')
        except:
            print('re check path')
        opt = Options()
        opt.add_experimental_option("debuggerAddress",'localhost:9221')
        driver=webdriver.Chrome(executable_path=r"E:\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
        
        
        driver.maximize_window()
        driver.get("https://en.wikipedia.org/wiki/Main_Page")

    
#     

def two():
    try:    
        os.chdir('C:\\Program Files\\Google\\Chrome\\Application')
        os.system('start cmd /k "chrome.exe --remote-debugging-port=9222 --user-data-dir=E:\chromedriver_win32\chromedata2"')
    except:
        print('re check path')
    opt = Options()
    opt.add_experimental_option("debuggerAddress",'localhost:9222')
    driver=webdriver.Chrome(executable_path=r"E:\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
    
    
    driver.maximize_window()
    driver.get("https://www.irctc.co.in/nget/train-search")





root = Tk()
root.configure(bg='sky blue')
root.title("IRCTC")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("1200x600+200+50")
icon=PhotoImage(file='icon.png')
root.iconphoto(False,icon)
thread1=multiprocessing.Process(target=one)
thread2=multiprocessing.Process(target=two)

if __name__ == "__main__":
    def click():
        global e1
        e1=entry.get()
        print(e1)
        # thread1.start()
        # # time.sleep(0.5)
        # thread2.start()

        # thread1.join()
        # thread2.join()
        def action():
            if e1=="1":
                thread1.start()
                thread1.join()
            elif e1=="2":
                thread1.start()
                # time.sleep(0.5)
                thread2.start()

                thread1.join()
                thread2.join()
        action()
    entry=Entry(root)
    entry.pack()
    button=Button(root,text='click',command=lambda:click()).pack()
    root.mainloop()