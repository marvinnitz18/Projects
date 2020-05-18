![Instabot](https://image.flaticon.com/icons/svg/87/87390.svg)


# INSTABOT


> *easy to use in windows and a command line environment.* 


* required: python,selenium
* driver is located in the scripts directory

# Installation

* pip install selenium

* add a auth.py file in the script directory with this content:

username='yourusername'

password='yourpassword'


* add a users.txt file in the script directory with instagram usernames:

exampleuser  
exampleuser  
.  
.  


Linux | Windows
------------ | -------------
headless | GUI
multiple threads (soon) | single threaded



# TODO:

* solve linux execution error
* solve *AttributeError: module 'selenium.webdriver' has no attribute 'FirefoxOptions'*
* add unfollow.py


