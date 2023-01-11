from libraries import  *
from _main import *
from passanger import *
from logging_module import logging_module
log_obj = logging_module.setup_logger("frame11")
user1='sarbdeoll'
user1_pass='Deol9646@'

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

    e1=debit_value["bank name"] 
    e2=debit_value["card type"] 
    e3=debit_value["card number"]
    month=debit_value["expiry month"]
    year=debit_value["expiry year"] 
    e5=debit_value["owner"]
    e6=debit_value["cvv"] 
    e7=debit_value["3D pass"]
    


    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-infobars")
    options.add_argument('--remote-debugging-port=9221')
    options.add_argument(f'--user-data-dir={var}\chrome\chromedata')
    options.add_argument('--disable-notifications')
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    options.binary_location = brave_path
    
    log_obj.info("opening browser")
    driver = webdriver.Chrome(executable_path=f"E:\\PYTHON\\train_ticket_v2\\chrome\\chromedriver.exe", options=options)
    
    try:
        driver.set_window_size(50, 550)
        driver.get("https://www.irctc.co.in/nget/train-search")
    except WebDriverException:
        print('Page Down')
        log_obj.exception("Page Down")
    log_obj.info("getting element for login button") 
    wait=WebDriverWait(driver, 10)
    try:
        #get element for login button
        element2=wait.until(EC.element_to_be_clickable(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/div/a[2]'))
          
        # element2 = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/div/a[2]')
        element2.click()
        print('login click')
       
        
        element2 = wait.until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[4]/img')).click()
      
        print('ad click')
 
        
    except:
        print('page 1 not reload, Unable to locate element login button  ')
        log_obj.exception("Unable to locate element login button") 
        # driver.quit()
    log_obj.info("username click")
    try:
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
        log_obj.info("username entered")
        time.sleep(.5)
    except:
        log_obj.exception("error in username enter")
        # driver.quit()
    try:
        
        log_obj.info("password element find")
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
        log_obj.info("password entered")
        time.sleep(1)
    except:
        log_obj.exception("error in password enter")
        # driver.quit()
    try:
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
            im1.save(f"{var}\crop2.png" ,quality=100)
            print('image address:',im1) 
            captcha = pytesseract.image_to_string(im1) 
            captcha = captcha.replace(" ", "").strip()
            # save in abc.txt file
            with open(f"{var}\\abc2.txt",mode ='w') as file:     
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
            print('signup 2')
            time.sleep(5)
        log_obj.info("getting login captcha")
        def logincaptcha2():
            print('logincaptcha 2')
            img=driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img')
            img.screenshot(f"{var}\logo.png")
            
            
            with open(f"{var}\logo.png", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('ascii')
                
                url = 'https://api.apitruecaptcha.org/one/gettext'

                data = { 
                    'userid':'sarbjitdeol72@gmail.com', 
                    'apikey':'hAWX2MbYjpViHGSVhYPX',  
                    'data':encoded_string,
                    'mode':'human'
                }
                response = requests.post(url = url, json = data)
                data = response.json()
                captcha=data['result']
                print('login captcha 2',captcha)


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
            log_obj.info("captcha entered")
            time.sleep(2)
            # click signup button 
            signup = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button')
            signup.click()
            print('signup 1')
            
            time.sleep(5)
            try:
                if driver.find_element(By.XPATH, "//*[@id='jDate']/span/input").is_displayed==False:
                    time.sleep(5)
            except:
                pass
        def check_captcha():
            for i in range(0,3):
                try:
                    if driver.find_element(By.ID, "nlpImgContainer").is_displayed()==True: 
                        print("first captcha show")
                        logincaptcha()
                except Exception as e:
                    print('error in captcha 1 load')
                
                try:
                    if driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div/span[1]/img').is_displayed()==True: 
                        print("blue image captcha show")
                        log_obj.info("blue image captcha show")
                        logincaptcha2()
                
                except Exception as e:
                    print('error in captcha 2 load')
                    # log_obj.exception("error in captcha 2 load")
            
        check_captcha()

        def error_check():
            try:
                for i in range(3):
                    if driver.find_element(By.XPATH,'//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[1]').is_displayed()==True:
                        print('again enter')
                        time.sleep(0.5)

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
        log_obj.info("login done")
        time.sleep(2)
        try:
            log_obj.info("getting FROM route element")
            #tap on from route
            loc = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
            loc.click()
            # time.sleep(.5)
            # create action chain object
            action = ActionChains(driver)
            # click the from route
            action.click(on_element = loc)
            # enter from location
            action.send_keys(ifrom)
            action.perform()
            time.sleep(.5)
            loc2 = driver.find_element(By.XPATH, '//*[@id="pr_id_1_list"]/li/span')
            loc2.click()
            time.sleep(1)
        except:
            log_obj.exception("error in <FROM> route")
            # driver.quit()
        try:
            log_obj.info("getting TO route element")
            #tap on to route
            loc3 = driver.find_element(By.XPATH, '//*[@id="destination"]/span/input')
            loc3.click()
            # time.sleep(.5)
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
        except:
            log_obj.exception("error in <TO> route select")
            # driver.quit()

        try:
            log_obj.info("getting date element")
            #tap on date 
            date_e = driver.find_element(By.XPATH, "//*[@id='jDate']/span/input")
            date_e.click()
            time.sleep(1)
            # create action chain object
            action = ActionChains(driver)
            # # click the date
            action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
            # write date
            action.send_keys(date)
            action.perform()
            time.sleep(.7)
        except:
            log_obj.exception("error in date enter")
            # driver.quit()

        try:
            loc = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
            loc.click()
            # journey qauta
            def general():
                pass
            
            def tatkal():
                #tatkal box
                log_obj.info("tatkal click")
                tatkal = driver.find_element(By.XPATH, '//*[@id="journeyQuota"]/div')
                tatkal.click()
                time.sleep(.5)

                tatkal = driver.find_element(By.XPATH, '//*[@id="journeyQuota"]/div/div[4]/div/ul/p-dropdownitem[5]/li')
                tatkal.click()
        except:
            log_obj.exception("error in qouta select")
            # driver.quit()

        if qouta=="GENERAL":
            general()
        elif qouta=="TATKAL":
            tatkal()

        try:
            log_obj.info("train search start")
            #SEARCH buttton click
            search = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div/button')
            search.click()
            time.sleep(4)
        except:
            log_obj.exception("Error in train search button")
            # driver.quit()

        # check refresh button show or not
        if driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]/span').is_displayed==False:
            time.sleep(4)
            print('wait')
        else:
            pass
        
        try:
            log_obj.info("refresh train button")
            #refresh button
            choose = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div[1]/table/tr/td[1]/div/div[2]/span')
            choose.click()
            time.sleep(2)
        except:
            log_obj.exception(" error in refresh train button")
            # driver.quit()
        # loading icon show
        try:
            if driver.find_element(By.XPATH, '//*[@id="preloaderP"]').is_displayed()==True:
                print('loading 2')
                log_obj.info("loading 2")
                time.sleep(4)
        except:
            time.sleep(2)
        try:
            log_obj.info("choose train button")
            #choose train
            choose = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[7]/div[1]/div[3]/table/tr/td[2]/div/div[2]/strong')
            choose.click()
            time.sleep(0.5)
        except:
            log_obj.exception("error in choose train")
            # driver.quit()

        try:
            log_obj.info("book button")
            #book
            book = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button')
            book.click()
            time.sleep(3)
        except:
            log_obj.exception("error in book button click")
            # driver.quit()

        try:
            if driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button').is_enabled()==True:
                print('book button is disabled')
                log_obj.exception("book button is disabled")
                # driver.quit()
                
            else:
                print('booking....')
        except:
            # messagebox.showinfo('','login again')
            print('book')
        try:
            if driver.find_element(By.XPATH, '//*[@id="preloaderP"]').is_displayed()==True:
                print('loading 2')
                time.sleep(5)
        except:
            time.sleep(2)
        # ---function of passangers 1 2 3 4 5 6------
        def pass1():
            log_obj.info("passanger 1 detail filling")
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            try:
                #enter passanger name
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
                log_obj.info("name enter")
            except:
                log_obj.exception("error in first passanger name")
                # driver.quit()
            
            try:
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
                log_obj.info("age enter")
            except:
                log_obj.exception("error in first passanger age")
                # driver.quit()
            try:
                #gender box
                gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
                gender.click()
                time.sleep(.5)

                gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
                gender_select.click()
                log_obj.info("gender select")
            except:
                log_obj.exception("error in first passanger gender")
                # driver.quit()

            try:
                if driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select').is_displayed()==True:
                    try:
                        #food box
                        food = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select')
                        food.click()
                        time.sleep(1)
                        #veg choose
                        food_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[2]/select/option[2]')
                        food_select.click()
                        time.sleep(1)
                        log_obj.info("food choose")
                    except:
                        log_obj.exception("error in first passanger food choose")
                        # driver.quit()
            except:
                print('food is not serve in selected train')
                
        def pass2():
            pass1()
            log_obj.info("passanger 2 details filling")
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
            log_obj.info("name enter")
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
            log_obj.info("age enter")
            #gender box
            gender = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
            gender.click()
            time.sleep(2)

            #male
            gender_select = driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[2]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select/option[2]')
            gender_select.click()
            log_obj.info("gender select")
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
        
        #upi select
        def upi_function():
            try:
                log_obj.info("upi payment start")
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                pay = driver.find_element(By.XPATH, '//*[@id="2"]/div/div[2]/span') # for upi
                pay.click()
                time.sleep(0.5)
            except:
                log_obj.exception("error in selecting upi payment")
                # driver.quit()

            try:
                #continue button same for both
                submit = driver.find_element(By.XPATH, '//*[@id="psgn-form"]/form/div/div[1]/p-sidebar/div/div/div[2]/button')
                submit.click()
                time.sleep(4)
                try:
                    if driver.find_element(By.XPATH, '//*[@id="preloaderP"]').is_displayed()==True:
                        print('loading 2')
                        time.sleep(10)
                        try:
                            if driver.find_element(By.XPATH, '//*[@id="preloaderP"]').is_displayed()==True:
                                print('loading 2')
                                time.sleep(5)
                        except:
                            pass
                except:
                    pass
            except:
                log_obj.exception("error in upi continue button")
                # driver.quit()

            #payment captcha page
            try:
                print('payment captcha page')
                log_obj.info("upi payment captcha page")
                #payment captcha 
                def paycaptcha():
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    img=driver.find_element(By.ID, "nlpImgContainer")
                    img.screenshot(f"{var}\logo2.png")
                    im = Image.open(f"{var}\logo2.png")
                    left = 0
                    top = 250
                    right = 300
                    bottom = 280
                    # Cropped image of above dimension
                    # (It will not change original image)
                    im1 = im.crop((left, top, right, bottom))
                    im1.save(f"{var}\crop2.png" ,quality=100)
                    print('image address:',im1) 
                    captcha = pytesseract.image_to_string(im1) 
                    captcha = captcha.replace(" ", "").strip()

                    #save in payment.txt
                    with open(f"{var}\payment2.txt",mode ='w') as file:      
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
                    img.screenshot(f"{var}\logo2.png")
                    
                    with open(f"{var}\logo2.png", "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read()).decode('ascii')
                        
                        url = 'https://api.apitruecaptcha.org/one/gettext'

                        data = { 
                            'userid':'sarbjitdeol72@gmail.com', 
                            'apikey':'hAWX2MbYjpViHGSVhYPX',  
                            'data':encoded_string,
                            'mode':'human'
                        }
                        response = requests.post(url = url, json = data)
                        data = response.json()
                        captcha=data['result']
                        print('payment 2',captcha)

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
                    log_obj.info("upi payment captcha enter")
                    time.sleep(.5)
                    
                    #continue buttton
                    continue_button = driver.find_element(By.XPATH, '//*[@id="review"]/div[1]/p-sidebar/div/div/div[2]/button')
                    continue_button.click()
                    print('continue_button')
                    log_obj.info("upi continue_button")
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
                        log_obj.exception("error in captcha 2 load")
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
                                # log_obj.exception("error in captcha 2 load")
                                
                    except:
                        print('captcha is corrects')
                error_check()
            except:
                log_obj.exception("error in payment captcha page")
                # driver.quit()

            try:
                #choose method to pay
                log_obj.info("Multiple Payment Service")
                #choose multiple payment method //*[@id="pay-type"]/span/div[1]/span
                upi_choose = driver.find_element(By.XPATH, '//*[@id="pay-type"]/span/div[1]/span')
                upi_choose.click()
                print('Multiple Payment Service')
                time.sleep(1)
            except:
                log_obj.exception("error in Multiple Payment Service")
                # driver.quit()
            try:
                cont = driver.find_element(By.XPATH,'//*[@id="psgn-form"]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[2]/div/div/div[2]/button')
                cont.click()
                print('continue')
                time.sleep(3)
            except:
                log_obj.exception("error in Multiple Payment Service contine")
                # driver.quit()
            #roserpay select 
            try:
                
                log_obj.info("roserpay method")
                roserpay = driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-payment-options/div[4]/div[2]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[1]/div/div/div[1]/div[2]/app-bank/div/div/table/tr/span[3]/td/div/div/span')
                roserpay.click()
                print('choose roserpay method')
                time.sleep(.5)
            except:
                log_obj.exception("error in roserpay select")
                # driver.quit()

            #pay & book button
            try:
                log_obj.info("getting pay & book button")
                pay = driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[3]/div/app-payment-options/div[4]/div[2]/div[1]/div[1]/app-payment/div[1]/div/form/p-sidebar[1]/div/div/div[2]/div[2]/button')
                pay.click()
                print('pay & book button')
                time.sleep(7)
            except:
                log_obj.exception("error in pay & book button")
                # driver.quit()

            try:
                log_obj.info("getting payment page")
                if driver.find_element(By.XPATH,"//iframe[@class='razorpay-checkout-frame']").is_displayed==True:
                    print('enter payment iframe')
                    iframe = driver.find_element(By.XPATH,"//iframe[@class='razorpay-checkout-frame']")
                    driver.switch_to.frame(iframe)
                else:
                    time.sleep(4)
                    iframe = driver.find_element(By.XPATH,"//iframe[@class='razorpay-checkout-frame']")
                    driver.switch_to.frame(iframe)
            except:
                log_obj.exception("error in getting payment page")
                # driver.quit()

            #upi or QR
            
            try:
                log_obj.info("click upi or QR")
                roserpay = driver.find_element(By.XPATH, '//*[@id="form-common"]/div[1]/div[1]/div/div/div/div/button[1]/div/div[1]/div[1]/div[1]')
                roserpay.click()
                print('upi or QR')
                time.sleep(1)
            except:
                log_obj.exception("error click on upi or QR")
                print('error click on upi or QR')
                # driver.quit()
            
            #click and add upi
            try:
                log_obj.info("click upi add button")
                conti_confirm = driver.find_element(By.XPATH,'//*[@id="vpa-upi"]')
                conti_confirm.click()
                print('click upi add button')
                # create action chain object
                action = ActionChains(driver)
                # click the item
                action.click(on_element = conti_confirm)
                # send keys
                action.send_keys(upi_value["upi"])
                action.perform()
                time.sleep(1)
                log_obj.info("upi added ")
            except:
                log_obj.exception("error in upi id enter ")
                # driver.quit()

            #proceed button to upi pay  
            try:
                pay_now = driver.find_element(By.XPATH,'//*[@id="footer-cta"]')
                pay_now.click()
                print(' pay now button')
                log_obj.info("pay now button click")
                time.sleep(1)
            except:
                try:
                    pay_now = driver.find_element(By.XPATH,'//*[@id="redesign-v15-cta"]')
                    pay_now.click()
                    print(' pay button')
                    log_obj.info("pay button click")
                    time.sleep(2)
                except:
                    log_obj.exception("error in pay button click ")
                    # driver.quit()
            #continue for mobile pay send 
            try:
                contine_pay = driver.find_element(By.XPATH,'//*[@id="overlay"]/div/div/div[2]')
                contine_pay.click()
                print(' continue button')
                log_obj.info("mobile link sending")
                time.sleep(1)
            except:
                try:
                    contine_pay = driver.find_element(By.XPATH,'//*[@id="overlay"]/div[2]/div/div[2]')
                    contine_pay.click()
                    print(' continue button')
                    log_obj.info("mobile link sending")
                    time.sleep(1)
                except:
                    log_obj.exception("error in continue and pay button click ")
                    # driver.quit()

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
                img.screenshot(f"{var}\logo2.png")
                im = Image.open(f"{var}\logo2.png")
                left = 0
                top = 250
                right = 300
                bottom = 280
                # Cropped image of above dimension
                # (It will not change original image)
                im1 = im.crop((left, top, right, bottom))
                im1.save(f"{var}\crop2.png" ,quality=100)
                print('image address:',im1) 
                captcha = pytesseract.image_to_string(im1) 
                captcha = captcha.replace(" ", "").strip()

                #save in payment.txt
                with open(f"{var}\payment2.txt",mode ='w') as file:      
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
                img.screenshot(f"{var}\logo2.png")
                with open(f"{var}\logo2.png", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('ascii')
                    
                    url = 'https://api.apitruecaptcha.org/one/gettext'

                    data = { 
                        'userid':'sarbjitdeol72@gmail.com', 
                        'apikey':'hAWX2MbYjpViHGSVhYPX',  
                        'data':encoded_string,
                        'mode':'human'
                    }
                    response = requests.post(url = url, json = data)
                    data = response.json()
                    captcha=data['result']
                    print('debit 2 captcha',captcha)
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


        
    except WebDriverException as e:
        print('1 something went wrong login again')
        # log_obj.exception("something went wrong login again")
        # driver.quit()

    while True:
        pass


