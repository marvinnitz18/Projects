import requests
import json
import time
import os
from colorama import init
from colorama import Fore, Back, Style
init()


api_key = open("api.key","r")
access_key = api_key.read()
#access_key = access_key[:-1]

api_url = "http://api.marketstack.com/v1/intraday/latest"

stocks = open("stocks.txt","r")
stocks = stocks.read()
print("\n")
print("Stocks to watch: "+stocks+Style.RESET_ALL)


#Initiaziled

print(Fore.GREEN+Back.BLACK+"API REQUEST: "+api_url +"?access_key="+access_key+"&symbols="+stocks+Style.RESET_ALL)

#API Request
r = requests.get(api_url +"?access_key="+access_key+"&symbols="+stocks)
if (r.status_code != 200):
    print(Fore.RED+Style.RED+"API Request failed !"+Style.RESET_ALL)
    exit()

#Stocks into list
stocks = stocks[:-2]
stocks = stocks.split(",")
#get num of stocks to watch
length = len(stocks)


data = json.loads(r.text)
data = data['data']

count = 0
for i in range(length):
    opening_price = data[count]['open']
    last_price = data[count]['last']
    
    print(Fore.BLACK+Back.WHITE+Style.BRIGHT+stocks[count]+Style.RESET_ALL+' opened at '+Style.BRIGHT+str(opening_price)+Style.RESET_ALL)
    print(stocks[count]+' last '+str(last_price)+Style.RESET_ALL)
    
    #calculate percentage
    try:
        percentage = last_price / opening_price
    except:
        print("No latest data available"+Style.RESET_ALL)
        percentage = None
   #stock + 
    if (percentage and percentage > 1):
        percentage = str(percentage)
        percentage = percentage[3:]
        percentage = percentage[:2]
        percentage = percentage[:1]+','+percentage[1:]
        print(+Back.GREEN+"+"+percentage+" today"+Style.RESET_ALL)

    #stock -
    if (percentage and percentage < 1):
        percentage = str(percentage)
        percentage = percentage[3:]
        percentage = percentage[:2]
        percentage = percentage[:1]+','+percentage[1:]
        print(+Back.RED+"-"+percentage+" today"+Style.RESET_ALL)

    else:
        pass


    count = count +1
    print("\n")

time.sleep(5)


