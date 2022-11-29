from libraries import  *
from _main import *
from passanger import *


def start1(user1,user1_pass,passanger_value,upi_value,method_pay,debit_value):
    
    name_1=passanger_value["name"]  
    name_2=passanger_value["name2"]  
    name_3=passanger_value["name3"]  
    name_4=passanger_value["name4"]  
    name_5=passanger_value["name5"]  
    name_6=passanger_value["name6"]  

    age_1=passanger_value["age"]  
    age_2=passanger_value["age2"]  
    age_3=passanger_value["age3"]  
    age_4=passanger_value["age4"]  
    age_5=passanger_value["age5"]  
    age_6=passanger_value["age6"]  

    gender=passanger_value["gender"]  
    gender2=passanger_value["gender2"]  
    gender3=passanger_value["gender3"]  
    gender4=passanger_value["gender4"]  
    gender5=passanger_value["gender5"]  
    gender6=passanger_value["gender6"]  

    ifrom=passanger_value["ifrom"]  
    ito=passanger_value["ito"]  
    date=passanger_value["date"]  
    count=passanger_value["total"]
    qouta=passanger_value["qouta"]


    upi=upi_value["upi"]
    e1=debit_value["bank name"] 
    e2=debit_value["card type"] 
    e3=debit_value["card number"]
    month=debit_value["expiry month"]
    year=debit_value["expiry year"] 
    e5=debit_value["owner"]
    e6=debit_value["cvv"] 
    e7=debit_value["3D pass"]
   
    try:    
        os.chdir('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application')
        os.system(f'start cmd /k "brave.exe --remote-debugging-port=9221 --user-data-dir={var}\chrome\chromedata"')
     
    except:
        print('re check path')
    opt = Options()
    opt.add_experimental_option("debuggerAddress",'localhost:9221')
    driver=webdriver.Chrome(executable_path=f"{var}\\chrome\\chromedriver.exe",chrome_options=opt)
    
    
    #driver.minimize_window()
    driver.set_window_size(50, 550)
    driver.get("https://www.irctc.co.in/nget/train-search")
    
    
    #get element for login button  
    element2 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/div/a[2]')
    element2.click()
    print('login click')
    time.sleep(3)
    if driver.find_element(By.XPATH, '/html/body/div[4]/img').is_displayed()==True:
        element2 = driver.find_element(By.XPATH, '/html/body/div[4]/img')
        element2.click()
        print('ad click')
        time.sleep(2)
    else:
        print('ad not show')
        time.sleep(2)
        element2 = driver.find_element(By.XPATH, '/html/body/div[4]/img')
        element2.click()
        print('ad click')
        time.sleep(2)
    #get element for usernme
    element3 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/input')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = element3)
    # send keys
    
    

    action.send_keys(user1) #e1.get()
    # perform the operation
    action.perform()
    print('username 1 entered')
    time.sleep(.5)
    

    # get element for password
    element4 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/input')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element = element4)
    # send keys
    action.send_keys(user1_pass)
    # perform the operation
    action.perform()
    
    print('password 1 entered')
    time.sleep(1)

    #----- function for captcha------
    def  logincaptcha():
        img=driver.find_element(By.ID, "nlpImgContainer") #By.ID, "nlpImgContainer" '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img'
        img.screenshot(f"{var}\logo.png")
        im = Image.open(f"{var}\logo.png") #use PIL.Image.open if not work
        left = 0
        top = 250
        right = 300
        bottom = 270
        # left = 0
        # top = 50
        # right = 300
        # bottom = 270

        # Cropped image of above dimension
        # (It will not change original image)
        im1 = im.crop((left, top, right, bottom))
        im1.save(f"{var}\crop.png" ,quality=100)
        print('image address:',im1) 
        captcha = pytesseract.image_to_string(im1) 
        captcha = captcha.replace(" ", "").strip()
        # save in abc.txt file
        with open(f"{var}\\abc.txt",mode ='w') as file:     
            file.write(captcha) 
            print('result',captcha)
            print('write result',captcha[18:22]) #5:14 paints  [18:22] default  5:12match
    
        #get element for captcha enter
        element5 = driver.find_element(By.XPATH, "//*[@id='nlpAnswer']")
        print('find')
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = element5)
        # enter captcha
        action.send_keys(captcha[18:22]) #[18:22]]
        action.perform()
        print('captcha enter 1')
        time.sleep(1)
        # click signup button 
        signup = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button')
        signup.click()
        print('signup 1')
        time.sleep(5)
    
    def logincaptcha2():
        print('logincaptcha 2')
        img=driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img')
        img.screenshot(f"{var}\logo.png")
        im = Image.open(f"{var}\logo.png") #use PIL.Image.open if not work
        
        captcha = pytesseract.image_to_string(im) 
        captcha = captcha.replace(" ", "").strip()
        # save in abc.txt file
        with open(f"{var}\\abc.txt",mode ='w') as file:     
            file.write(captcha) 
            print('result',captcha)
            print('write result',captcha) #5:14 paints  [18:22] default  5:12match

        #get element for captcha enter
        element5 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/input")
        print('find')
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = element5)
        # enter captcha
        action.send_keys(captcha) #[18:22]]
        action.perform()
        print('captcha enter')
        time.sleep(2)
        # click signup button 
        signup = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button')
        signup.click()
        print('signup 1')
        time.sleep(5)
        if driver.find_element(By.XPATH, "//*[@id='jDate']/span/input").is_displayed==False:
            time.sleep(5)
        else:
            pass
    def check_captcha():
        for i in range(0,5):
            try:
                if driver.find_element(By.ID, "nlpImgContainer").is_displayed()==True: 
                    print("first captcha show")
                    logincaptcha()
            except Exception as e:
                print('error in captcha 1 load')
            
            try:
                if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                    print("blue image captcha show")
                    logincaptcha2()
            
            except Exception as e:
                print('error in captcha 2 load')
         
    check_captcha()

    def error_check():
        try:
            for i in range(3):
                if driver.find_element(By.XPATH,'//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[1]').is_displayed()==True:
                    print('again enter')
                    time.sleep(1)

                    try:
                        if driver.find_element(By.ID, "nlpImgContainer").is_displayed()==True: 
                            print("error fill in first captcha ")
                            logincaptcha()
                    except Exception as e:
                        print('error in captcha 1 load')

                    try:
                        if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                            print("error fill in second captcha")
                            logincaptcha2()
                    except Exception as e:
                        print('error in captcha 2 load')
                    
                elif driver.find_element(By.XPATH,'//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[1]').is_displayed()==False:
                    print('captcha is correct')
        except:
            print('captcha is corrects')
    error_check()
   
    time.sleep(2)
    
    #tap on from route
    loc = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
    loc.click()
    time.sleep(.5)
    # create action chain object
    action = ActionChains(driver)
    # click the from route
    action.click(on_element = loc)
    # enter from location
    action.send_keys(ifrom)
    action.perform()
    time.sleep(.5)

    #to location click
    loc1 = driver.find_element(By.XPATH, '//*[@id="pr_id_1_list"]/li/span')
    loc1.click()
    time.sleep(.5)
    #tap on to route
    loc3 = driver.find_element(By.XPATH, '//*[@id="destination"]/span/input')
    loc3.click()
    time.sleep(.5)
    # create action chain object
    action = ActionChains(driver)
    # click the to location
    action.click(on_element = loc3)
    # enter destination 
    action.send_keys(ito)
    action.perform()
    time.sleep(.5)
    # click destination location
    loc4 = driver.find_element(By.XPATH, '//*[@id="pr_id_2_list"]/li[1]')
    loc4.click()
    time.sleep(.5)

    #tap on date 
    date_e = driver.find_element(By.XPATH, "//*[@id='jDate']/span/input")
    date_e.click()
    time.sleep(1)
    # create action chain object
    action = ActionChains(driver)
    # click the date
    action.click(on_element = date_e)
    action.double_click(on_element = date_e)
    # write date
    action.send_keys(date)
    action.perform()
    time.sleep(.7)
    loc = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
    loc.click()
    # journey qauta
    def general():
        pass
    
    def tatkal():
        #tatkal box
        tatkal = driver.find_element(By.XPATH, '//*[@id="journeyQuota"]/div')
        tatkal.click()
        time.sleep(.5)

        tatkal = driver.find_element(By.XPATH, '//*[@id="journeyQuota"]/div/div[4]/div/ul/p-dropdownitem[5]/li')
        tatkal.click()

    if qouta=="GENERAL":
        general()
    elif qouta=="TATKAL":
        # general()
        tatkal()
    #SEARCH buttton click
    search = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div/button')
    search.click()
    time.sleep(4)
    if driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]/span').is_displayed==False:
        time.sleep(4)
    else:
        pass

    #refresh button
    choose = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]/span')
    choose.click()
    time.sleep(2)

    #choose train
    choose = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[7]/div[1]/div[3]/table/tr/td[2]/div/div[2]/strong')
    choose.click()
    time.sleep(1.5)

    #book
    book = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button')
    book.click()
    time.sleep(3)
    try:
        book = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/p-confirmdialog[2]/div/div/div[3]/button[1]/span[2]')
        book.click()
        time.sleep(3)
    except:
        if driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/p-confirmdialog[2]/div/div/div[3]/button[1]/span[2]'):
            time.sleep(3)
        else:
            pass
    
    # ---function of passangers 1 2 3 4 5 6------
    def pass1():
        #enter passanger name
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(.5)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(name_1)
        action.perform()
        time.sleep(.2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(.3)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(age_1)
        action.perform()
        time.sleep(.5)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(.5)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()
    def pass2():
        pass1()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[1]/a/span[1]')
        add_pas.click()

        #enter passanger name
        name2 = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name2.click()
        time.sleep(2)                               #//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name2)
        # send keys
        action.send_keys(name_2)
        action.perform()
        time.sleep(2)

        #age box
        age2 = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age2.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age2)
        # send keys
        action.send_keys(age_2)
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        #male
        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()

        #female
        # gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-24-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[3]')
        # gender_select.click()
    def pass3():
        pass2()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[1]/a/span[2]')
        add_pas.click()

        #enter passanger name
        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(name_3)
        action.perform()
        time.sleep(2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(age_3)
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[3]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()

    def pass4():
        pass3()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[1]/a/span[2]')
        add_pas.click()

        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(name_4)
        action.perform()
        time.sleep(2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(age_4)
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[4]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()
    def pass5():
        pass4()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[1]/a/span[1]')
        add_pas.click()

        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(name_5)
        action.perform()
        time.sleep(2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(age_5)
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[5]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()
    def pass6():
        pass5()
        add_pas = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[1]/a/span[1]')
        add_pas.click()

        name = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
        name.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = name)
        # send keys
        action.send_keys(name_6)
        action.perform()
        time.sleep(2)

        #age box
        age = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
        age.click()
        time.sleep(2)
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = age)
        # send keys
        action.send_keys(age_6)
        action.perform()
        time.sleep(2)

        #gender box
        gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
        gender.click()
        time.sleep(2)

        gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[6]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
        gender_select.click()

    # ------condition of passanger count-----------
    if count=='1':
        pass1()
    elif count == '2':
        pass2()
    elif count == '3':
        pass3()
    elif count == '4':
        pass4()
    elif count == '5':
        pass5()
    elif count == '6':
        pass6()
           
    #food box
    # food = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select')
    # food.click()
    # time.sleep(1)
    # #veg choose
    # food_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select/option[2]')
    # food_select.click()
    # time.sleep(1)

    
    
    #upi select
    def upi_function():
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        pay = driver.find_element(By.XPATH, '//*[@id="2"]/div/div[2]/span') # for upi
        pay.click()
        time.sleep(1)

        #continue button same for both
        submit = driver.find_element(By.XPATH, '//*[@id="psgn-form"]/form/div/div[1]/p-sidebar/div/div/div[2]/button')
        submit.click()
        time.sleep(4)
        print('payment captcha page')
        
        #payment captcha 
        def paycaptcha():
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            img=driver.find_element(By.ID, "nlpImgContainer")
            img.screenshot(f"{var}\logo.png")
            im = Image.open(f"{var}\logo.png")
            left = 0
            top = 250
            right = 300
            bottom = 280
            # Cropped image of above dimension
            # (It will not change original image)
            im1 = im.crop((left, top, right, bottom))
            im1.save(f"{var}\crop.png" ,quality=100)
            print('image address:',im1) 
            captcha = pytesseract.image_to_string(im1) 
            captcha = captcha.replace(" ", "").strip()

            #save in payment.txt
            with open(f"{var}\payment.txt",mode ='w') as file:      
                file.write(captcha) 
                print('result',captcha)
                print('write result',captcha[18:22])
            #get element for captcha enter
            element5 = driver.find_element(By.XPATH, "//*[@id='nlpAnswer']")
            print('find')
            # create action chain object
            action = ActionChains(driver)
            # click the item
            action.click(on_element = element5)
            time.sleep(1)
            # send keys
            action.send_keys(captcha[18:22])
            action.perform()
            print('payement captcha enter')
            time.sleep(3)

            #continue buttton
            continue_button = driver.find_element(By.XPATH, '//*[@id="review"]/div[1]/p-sidebar/div/div/div[2]/button')
            continue_button.click()
            print('continue_button')
            time.sleep(3)
           
        def paycaptcha2():
            print('paycaptcha 2')
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            img=driver.find_element(By.XPATH,'//*[@id="review"]/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img')
            img.screenshot(f"{var}\logo.png")
            im = Image.open(f"{var}\logo.png") #use PIL.Image.open if not work

            captcha = pytesseract.image_to_string(im) 
            captcha = captcha.replace(" ", "").strip()
            # save in abc.txt file
            with open(f"{var}\\payment.txt",mode ='w') as file:     
                file.write(captcha) 
                print('result',captcha)
                print('write result',captcha) #5:14 paints  [18:22] default  5:12match

            #get element for captcha enter
            element5 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/input")
            print('find')
            # create action chain object
            action = ActionChains(driver)
            # click the item
            action.click(on_element = element5)
            # enter captcha
            action.send_keys(captcha) #[18:22]]
            action.perform()
            print('captcha enter')
            time.sleep(.5)
            
            #continue buttton
            continue_button = driver.find_element(By.XPATH, '//*[@id="review"]/div[1]/p-sidebar/div/div/div[2]/button')
            continue_button.click()
            print('continue_button')
            time.sleep(3)
            if driver.find_element(By.XPATH, '//*[@id="pay-type"]/span/div[1]/span').is_displayed==False:
                paycaptcha2()
            else:
                pass
        def check_pay_captcha():
            try:
                if driver.find_element(By.ID, "nlpImgContainer").is_displayed()==True: 
                    print("first pay captcha show")
                    paycaptcha()
            except Exception as e:
                print('error in captcha 1 load')
            
            try:
                if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                    print("blue image pay captcha show")
                    paycaptcha2()
            
            except Exception as e:
                print('error in captcha 2 load')
        check_pay_captcha()
         
        time.sleep(3)
        def error_check():
            try:
                for i in range(3):
                    
                    try:
                        if driver.find_element(By.ID, "nlpImgContainer").is_displayed()==True: 
                            print("enter agian ")
                            paycaptcha()
                    except Exception as e:
                        print('error in captcha 1 load')

                    try:
                        if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                            print("agin enter second captcha")
                            # error = driver.find_element(By.XPATH, '//*[@id="psgn-form"]/form/div/div[1]/p-sidebar/div/div/div[2]/button')
                            # error.click()
                            paycaptcha2()
                    except Exception as e:
                        print('error in captcha 2 load')
                           
            except:
                print('captcha is corrects')
        error_check()
        #choose method to pay

        
        #choose multiple payment method //*[@id="pay-type"]/span/div[1]/span
        upi_choose = driver.find_element(By.XPATH, '//*[@id="pay-type"]/span/div[1]/span')
        upi_choose.click()
        print('multiple choose')
        time.sleep(1)
        
        cont = driver.find_element(By.XPATH,'//*[@id="psgn-form"]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[2]/div/div/div[2]/button')
        cont.click()
        print('continue')
        time.sleep(3)
        # #//*[@id="google_esf"]
        # #enter iframe
        # iframe = driver.find_element(By.XPATH,'/html/body/iframe')
        # driver.switch_to.frame(iframe)
        #roserpay select 
        roserpay = driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-payment-options/div[4]/div[2]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[1]/div/div/div[1]/div[2]/app-bank/div/div/table/tr/span[3]/td/div/div/span')
        roserpay.click()
        print('upi choose roserpay')
        time.sleep(.5)

        
        #pay & book button
        pay = driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-payment-options/div[4]/div[2]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[1]/div/div/div[2]/div[2]/button')
        pay.click()
        print('upi payment')
        time.sleep(4)
        #enter iframe
        if driver.find_element(By.XPATH,"//iframe[@class='razorpay-checkout-frame']").is_displayed==True:
            iframe = driver.find_element(By.XPATH,"//iframe[@class='razorpay-checkout-frame']")
            driver.switch_to.frame(iframe)
        else:
            time.sleep(4)
            iframe = driver.find_element(By.XPATH,"//iframe[@class='razorpay-checkout-frame']")
            driver.switch_to.frame(iframe)
        #upi or QR
        try:
            roserpay = driver.find_element(By.XPATH, '//*[@id="form-common"]/div[1]/div[1]/div/div/div/div/button[1]/div/div[1]/div[1]/div[1]')
            roserpay.click()
            print('upi or QR')
            time.sleep(1)
        except:
            print('take in your hands')

    
        #click and add upi
        conti_confirm = driver.find_element(By.XPATH,'//*[@id="vpa-upi"]')
        conti_confirm.click()
        print('add payment number')
        # create action chain object
        action = ActionChains(driver)
        # click the item
        action.click(on_element = conti_confirm)
        # send keys
        action.send_keys(upi_value["upi"])
        action.perform()
        time.sleep(1)

        #proceed button to upi pay  
        try:
            paytm_submit = driver.find_element(By.XPATH,'//*[@id="footer-cta"]')
            paytm_submit.click()
            print(' pay button')
            time.sleep(1)
        except:
            paytm_submit = driver.find_element(By.XPATH,'//*[@id="redesign-v15-cta"]')
            paytm_submit.click()
            print(' pay button')
            time.sleep(1)

        #continue for mobile pay send 
        try:
            contine_pay = driver.find_element(By.XPATH,'//*[@id="overlay"]/div/div/div[2]')
            contine_pay.click()
            print(' continue button')
            time.sleep(1)
        except:
            contine_pay = driver.find_element(By.XPATH,'//*[@id="overlay"]/div[2]/div/div[2]')
            contine_pay.click()
            print(' continue button')
            time.sleep(1)
    #upi_function()

    #select debit
    def debit_function():
        #continue button same for both
        submit = driver.find_element(By.XPATH, '//*[@id="psgn-form"]/form/div/div[1]/div[14]/div/button[2]')
        submit.click()
        time.sleep(8)
        print('payment captcha page')
        #payment captcha 
        def paycaptcha():
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            img=driver.find_element(By.ID, "nlpImgContainer")
            img.screenshot(f"{var}\logo.png")
            im = Image.open(f"{var}\logo.png")
            left = 0
            top = 250
            right = 300
            bottom = 280
            # Cropped image of above dimension
            # (It will not change original image)
            im1 = im.crop((left, top, right, bottom))
            im1.save(f"{var}\crop.png" ,quality=100)
            print('image address:',im1) 
            captcha = pytesseract.image_to_string(im1) 
            captcha = captcha.replace(" ", "").strip()

            #save in payment.txt
            with open(f"{var}\payment.txt",mode ='w') as file:      
                file.write(captcha) 
                print('result',captcha)
                print('write result',captcha[18:22])
            #get element for captcha enter
            element5 = driver.find_element(By.XPATH, "//*[@id='nlpAnswer']")
            print('find')
            # create action chain object
            action = ActionChains(driver)
            # click the item
            action.click(on_element = element5)
            time.sleep(1)
            # send keys
            action.send_keys(captcha[18:22])
            action.perform()
            print('payement captcha enter')
            time.sleep(3)

            #continue buttton
            continue_button = driver.find_element(By.XPATH, '//*[@id="review"]/div[1]/p-sidebar/div/div/div[2]/button')
            continue_button.click()
            print('continue_button')
            time.sleep(3)
           
        def paycaptcha2():
            print('paycaptcha 2')
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            img=driver.find_element(By.XPATH,'//*[@id="review"]/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img')
            img.screenshot(f"{var}\logo.png")
            im = Image.open(f"{var}\logo.png") #use PIL.Image.open if not work

            captcha = pytesseract.image_to_string(im) 
            captcha = captcha.replace(" ", "").strip()
            # save in abc.txt file
            with open(f"{var}\\payment.txt",mode ='w') as file:     
                file.write(captcha) 
                print('result',captcha)
                print('write result',captcha) #5:14 paints  [18:22] default  5:12match

            #get element for captcha enter
            element5 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/input")
            print('find')
            # create action chain object
            action = ActionChains(driver)
            # click the item
            action.click(on_element = element5)
            # enter captcha
            action.send_keys(captcha) #[18:22]]
            action.perform()
            print('captcha enter')
            time.sleep(.5)
            
            #continue buttton
            continue_button = driver.find_element(By.XPATH, '//*[@id="review"]/div[1]/p-sidebar/div/div/div[2]/button')
            continue_button.click()
            print('continue_button')
            time.sleep(3)
            if driver.find_element(By.XPATH, '//*[@id="pay-type"]/span/div[1]/span').is_displayed==False:
                paycaptcha2()
            else:
                pass
        def check_pay_captcha():
            try:
                if driver.find_element(By.ID, "nlpImgContainer").is_displayed()==True: 
                    print("first pay captcha show")
                    paycaptcha()
            except Exception as e:
                print('error in captcha 1 load')
            
            try:
                if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                    print("blue image pay captcha show")
                    paycaptcha2()
            
            except Exception as e:
                print('error in captcha 2 load')
        check_pay_captcha()
         
        time.sleep(3)
        def error_check():
            try:
                for i in range(3):
                    
                    try:
                        if driver.find_element(By.ID, "nlpImgContainer").is_displayed()==True: 
                            print("enter agian ")
                            paycaptcha()
                    except Exception as e:
                        print('error in captcha 1 load')

                    try:
                        if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                            print("agin enter second captcha")
                            paycaptcha2()
                    except Exception as e:
                        print('error in captcha 2 load')
                           
            except:
                print('captcha is corrects')
        error_check()
        #choose method to pay

        
        #choose multiple payment method //*[@id="pay-type"]/span/div[1]/span
        debit_choose = driver.find_element(By.XPATH, '//*[@id="pay-type"]/span/div[2]')
        debit_choose.click()
        print('multiple choose')
        time.sleep(2)

        
        #roserpay select 
        roserpay = driver.find_element(By.XPATH, '//*[@id="bank-type"]/div/table/tr/span[3]/td/div/div')
        roserpay.click()
        print('debit choose roserpay')
        time.sleep(2)

        #pay & book button
        pay = driver.find_element(By.XPATH,'//*[@id="psgn-form"]/div[1]/div[1]/app-payment/div[2]/button[2]')
        pay.click()
        print('debit payment')
        time.sleep(6)
        #enter iframe
        iframe = driver.find_element(By.XPATH,"//iframe[@class='razorpay-checkout-frame']")
        driver.switch_to.frame(iframe)

        roserpay = driver.find_element(By.XPATH, '//*[@id="form-common"]/div[1]/div/div/div/div/div/button[1]/div/div[1]/div[1]/div[1]')
        roserpay.click()
        print('Debit/credit card')
        time.sleep(2)

        #click on card number
        card_number = driver.find_element(By.XPATH,'//*[@id="card_number"]')
        card_number.click()
        action = ActionChains(driver)
                # click the item
        action.click(on_element = card_number)
                # send keys
        action.send_keys(e3)
        action.perform()
        print('card number enter')
        time.sleep(2)

        #click on Expiry
        card_expiry = driver.find_element(By.XPATH,'//*[@id="card_expiry"]')
        card_expiry.click()
        action = ActionChains(driver)
                # click the item
        action.click(on_element = card_expiry)
                # send keys
        action.send_keys(month) 
            
        action.send_keys(year)
        action.perform()
        print('date enter')
        time.sleep(2)

        #click on holder's name
        card_holder = driver.find_element(By.XPATH,'//*[@id="card_name"]')
        card_holder.click()
        action = ActionChains(driver)
                # click the item
        action.click(on_element = card_holder)
                # send keys
        action.send_keys(e5)
        action.perform()
        print('holder name enter')
        time.sleep(2)

        #click on CVV
        card_CVV = driver.find_element(By.XPATH,'//*[@id="card_cvv"]')
        card_CVV.click()
        action = ActionChains(driver)
                # click the item
        action.click(on_element = card_CVV)
                # send keys
        action.send_keys(e6)
        action.perform()
        print('cvv enter')
        time.sleep(2)
        #proceed button to upi pay
        pay_debit = driver.find_element(By.XPATH,'//*[@id="footer-cta"]')
        pay_debit.click()
        print(' debit pay button')
        time.sleep(2)

        #continue for mobile pay send
        contine_pay = driver.find_element(By.XPATH,'//*[@id="overlay"]/div/div/div[2]')
        contine_pay.click()
        print(' continue button')
        time.sleep(2)
    #debit_function()

    if method_pay["method_p"]=="UPI":
        upi_function()
    elif method_pay["method_p"]=="DEBIT":
        debit_function()


    while True:
        pass