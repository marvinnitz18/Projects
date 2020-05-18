import sys
import time
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from Instabot import auth

options = wd.FirefoxOptions()
#options.add_argument('--headless')
driver = wd.Firefox(options=options, executable_path='geckodriver.exe')
driver.set_window_size(600,800)


#pass args [username,password,path to users file]
args = sys.argv
#if args[0] == "":
#    print("supply args")
#    exit();

lines = open('users.txt','r', encoding='utf8').readlines()
print('loaded ',str(len(lines)),' users')
user_count = 1
username = auth.username
password = auth.password
instaurl = 'https://www.instagram.com'

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


