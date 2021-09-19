from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import WebDriverException

import time
import random
import string
import sys



registration = int(input("Enter number of users to create: "))
count=0

while registration>0:

    count+=1
    driver= webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    with webdriver.Chrome() as driver:
        
        wait = WebDriverWait(driver, 10)
        URL = 'enter website registration page url here' 
        try:
            driver.get(URL)
        except WebDriverException:
            sys.exit("Page not available..exiting..")
        
        time.sleep(3)

        fname = driver.find_element_by_name('first_name')
        lname = driver.find_element_by_name('last_name')
        email = driver.find_element_by_name('email')
        phone = driver.find_element_by_name('phone')
        unireg = driver.find_element_by_name('unireg')
        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        confirmpwd = driver.find_element_by_name('confirmpassword')
        collegeid = driver.find_element_by_name('collegeid')
      
        time.sleep(3)
        
        #generate random inputs
        string_inp = ''.join(random.choices(string.ascii_lowercase, k=5))
        string_inp_str = str(string_inp+'@'+string_inp+'.com')
        pwd = random.randint(0,10000)
        gender_select =random.randint(0,2)
        
        
        
        print("Entering fname")
        time.sleep(2)
        fname.send_keys(str(string_inp))
        
        
        print("Entering lname")
        time.sleep(2)
        lname.send_keys(str(string_inp))
        
        
        print("Entering gender")
        time.sleep(2)
        if gender_select==0:
            driver.find_element_by_css_selector("input[type='radio'][value='Male']").click()
        elif gender_select==1:    
            driver.find_element_by_css_selector("input[type='radio'][value='Female']").click()
        else: 
            driver.find_element_by_css_selector("input[type='radio'][value='Other']").click()
            
        
        print("Entering email")
        time.sleep(2)
        email.send_keys(string_inp_str)
        
        print("Entering phone number")
        time.sleep(2)
        phone.send_keys(random.randint(10000000,99999999))
        
        print("Entering uni. reg. number")
        time.sleep(2)
        unireg.send_keys(random.randint(0,10000))
        
        print("Entering uni. reg. number")
        time.sleep(2)
        unireg.send_keys(random.randint(0,10000))
        
        print("Entering college id")
        time.sleep(2)
        collegeid.send_keys(random.randint(0,10000))
        
    
        print("Entering username")
        time.sleep(2)
        username.send_keys(string_inp)
        
       
        print("Entering password")
        time.sleep(2)
        password.send_keys(pwd)
        
        print("Entering confirm password")
        time.sleep(2)
        confirmpwd.send_keys(pwd)
        
        print("Submitting form")
        time.sleep(5)
        submit_button = driver.find_element_by_id('reguserbtn')
        submit_button.click()
        
        print(f"User {count} creation completed")
        print(f"Username {string_inp} Password {pwd}")
        time.sleep(5)
    
    registration = registration-1

print("All users successfully added")
