import auth
import sys
import time
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys


#options.add_argument('--headless')

driver = wd.Chrome(executable_path='geckodriver')
