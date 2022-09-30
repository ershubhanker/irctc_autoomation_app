# import the following libraries 
# will convert the image to text string 

import pytesseract       
 
# adds image processing capabilities 

from PIL import Image     
 # opening an image from the source path 

img = Image.open('crop.png')      
# describes image format in the output 
print('text:',img)                           
# path where the tesseract module is installed 
pytesseract.pytesseract.tesseract_cmd ="C:\Program Files\Tesseract-OCR\\tesseract.exe" 
# converts the image to result and saves it into result variable 

result = pytesseract.image_to_string(img)  
result = result.replace(" ", "").strip()


# write text in a text file and save it to source path    

with open('abc.txt',mode ='w') as file:      

    file.write(result) 
    print(result)
    print('result',result[16:20]) 

                   

#p = Translator()                       
# translates the text into german language 

#k = p.translate(result,dest='german')       

#print(k) 

##engine = pyttsx3.init() 

  
# an audio will be played which speaks the test if pyttsx3 recognizes it 
#engine.say(k)                              
#engine.runAndWait() 

# img=driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img")
# image_file=img.screenshot("logo.png")
# im = Image.open('logo.png')
# print('text:',im) 
# captcha = pytesseract.image_to_string(im) 
# captcha = captcha.replace(" ", "").strip()
# with open('abc.txt',mode ='w') as file:      
#     file.write(captcha) 
#     print('result',captcha)