#--------program to crop the image & save------------

# Importing Image class from PIL module
from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# Opens a image in RGB mode
im = Image.open(r"E:\DJANGO\recapcha bypass\logo.png")

# Setting the points for cropped image
left = 0
top = 110
right = 300
bottom = 170
# left = 0
# top = 250
# right = 300
# bottom = 270

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
image_file1=im1.save("hit.png")
captcha = pytesseract.image_to_string(im) 
captcha = captcha.replace(" ", "").strip()
# save in abc.txt file
with open(r'E:\DJANGO\recapcha bypass\captcha.txt',mode ='w') as file:      
    file.write(captcha) 
    print('result',captcha)
# Shows the image in image viewer
im.show()
