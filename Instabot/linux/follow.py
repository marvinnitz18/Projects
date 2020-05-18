#!/bin/python
import auth
import sys
import time
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

driver = wd.Firefox(executable_path='geckodriver')
options = wd.FirefoxOptions()
options.add_argument('--headless')

#pass args
#args = sys.argv[]

lines = open('users','r', encoding='utf8').readlines()
user_count = 1
username = auth.username
password = auth.password
instaurl = 'https://www.instagram.de'

driver.get(instaurl)
time.sleep(3)
try:
#enter password
    usernameinput = driver.find_element_by_name('username')
    usernameinput.click()
    usernameinput.send_keys(username)
    print('entered username')
#enter username
    passwordinput = driver.find_element_by_name('password')
    passwordinput.click()
    passwordinput.send_keys(password)
    print('entered password')
    passwordinput.send_keys(Keys.ENTER)
    print('login successfull')
    time.sleep(2)
except:
    print('login failed')

for x in range(5,len(lines)):
    try:
        print("Username #", str(user_count), ": ", str(lines[x]))
        driver.get(instaurl+"/"+lines[x])
        print("found profile")
        time.sleep(2)
        driver.find_elements_by_css_selector('button')[0].click()
        print('followed',lines[x])
        time.sleep(50)
        user_count = user_count +1
    except:
        print("Didnt find profile")

    user_count = user_count +1
