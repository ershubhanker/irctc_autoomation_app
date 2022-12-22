#--------program to crop the image & save------------

# Importing Image class from PIL module
from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# Opens a image in RGB mode
im = Image.open(r"circuit_board_otsu.png")

# Setting the points for cropped image
# left = 0
# top = 110
# right = 300
# bottom = 170
# left = 0
# top = 250
# right = 300
# bottom = 270

# Cropped image of above dimension
# (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
# image_file1=im1.save("hit.png")
captcha = pytesseract.image_to_string(im) 
captcha = captcha.replace(" ", "").strip()
# save in abc.txt file
with open(r'E:\DJANGO\recapcha bypass\captcha.txt',mode ='w') as file:      
    file.write(captcha) 
    print('result',captcha)
# # Shows the image in image viewer
# im.show()
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import cv2
# pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# file = 'sample2.png'

# img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
# img = cv2.medianBlur(img, 9)
# th, img = cv2.threshold(img, 185, 255, cv2.THRESH_BINARY)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,8))
# img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# cv2.imwrite("sample3.png", img)


# file = 'sample3.png'
# captcha = pytesseract.image_to_string(file)
# with open("abc.txt",mode ='w') as file:     
#         file.write(captcha) 
#         print('result',captcha)
#         print('write result',captcha)

# import keras_ocr 

# pipeline = keras_ocr.pipeline.Pipeline()

# images = [
# keras_ocr.tools.read('logo3.png')]

# #print(images[0])


# prediction_groups = pipeline.recognize(images)

# predicted_image_1 = prediction_groups[0]
# for text, box in predicted_image_1:
#     print(text)

# import matplotlib.pyplot as plt
# import keras_ocr
# pipeline = keras_ocr.pipeline.Pipeline()
# images = [
#     keras_ocr.tools.read(img) for img in ['circuit_board_mask.png',
#                                           'logo2.png'
#     ]
# ]
# prediction_groups = pipeline.recognize(images)
# fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
# for ax, image, predictions in zip(axs, images, prediction_groups):
#     keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
# print(predictions)

# import cv2
# import numpy as np
# import pytesseract
# from PIL import Image,ImageFilter
# import os
# pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# # read image
# img = cv2.imread('logo.png')

# # blur
# blur = cv2.GaussianBlur(img, (3,3), 0)

# # convert to hsv and get saturation channel
# sat = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)[:,:,1]

# # threshold saturation channel
# thresh = cv2.threshold(sat, 50, 255, cv2.THRESH_BINARY)[1]

# # apply morphology close and open to make mask
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
# morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
# mask = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel, iterations=1)

# # do OTSU threshold to get circuit image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# # write black to otsu image where mask is black
# otsu_result = otsu.copy()
# otsu_result[mask==0] = 0

# # write black to input image where mask is black
# img_result = img.copy()
# img_result[mask==0] = 0

# # write result to disk
# # cv2.imwrite("circuit_board_mask.png", sat)
# cv2.imwrite("circuit_board_otsu.png", otsu)
# # cv2.imwrite("circuit_board_otsu_result.png", otsu_result)
# # cv2.imwrite("circuit_board_img_result.png", img_result)


# # display it
# # cv2.imshow("IMAGE", img)
# # cv2.imshow("SAT", sat)
# # cv2.imshow("MASK", mask)
# cv2.imshow("OTSU", otsu)
# # cv2.imshow("OTSU_RESULT", otsu_result)
# # cv2.imshow("IMAGE_RESULT", img_result)
# var=os.getcwd()
# cv2.waitKey(0)
