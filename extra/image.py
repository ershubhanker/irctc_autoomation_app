#--------program to crop the image & save------------

# Importing Image class from PIL module
# from PIL import Image
# import pytesseract
# import os
# pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# # Opens a image in RGB mode
# im = Image.open(r"E:\DJANGO\irctc_autoomation_app\recapcha bypass\logo.png")

# # Setting the points for cropped image
# left = 0
# top = 110
# right = 300
# bottom = 170
# # left = 0
# # top = 250
# # right = 300
# # bottom = 270

# # Cropped image of above dimension
# # (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
# image_file1=im1.save("hit.png")
# captcha = pytesseract.image_to_string(im) 
# captcha = captcha.replace(" ", "").strip()
# # save in abc.txt file
# with open(r'E:\DJANGO\recapcha bypass\captcha.txt',mode ='w') as file:      
#     file.write(captcha) 
#     print('result',captcha)
# # Shows the image in image viewer
# im.show()
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
file = 'logo.png'

img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
img = cv2.medianBlur(img, 9)
th, img = cv2.threshold(img, 185, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,8))
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("sample2.png", img)


file = 'sample2.png'
captcha = pytesseract.image_to_string(file)
with open("abc.txt",mode ='w') as file:     
        file.write(captcha) 
        print('result',captcha)
        print('write result',captcha)