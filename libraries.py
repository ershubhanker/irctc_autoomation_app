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
#passanger value dictionary
passanger_value={'name':"",'age':"",'gender':"",'name2':"",'age2':"",'gender2':"",'name3':"",'age3':"",'gender3':"",'name4':"",
'age4':"",'gender4':"",'name5':"",'age5':"",'gender5':"",'name6':"",'age6':"",'gender6':"",'ifrom':"",'ito':"",'date':"",'total':"",'qouta':""}
upi_value={'upi':""}
debit_value={'bank name':"",'card type':"",'card number':"",'expiry month':"",'expiry year':'','owner':"",'cvv':"",'3D pass':""}
method_pay={'method_p':""}
counter_value={'tatkal_counter':""}
var=os.getcwd()
#print(var)