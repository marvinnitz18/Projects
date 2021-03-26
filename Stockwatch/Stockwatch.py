import requests
import json

api_key = open("api.key","r")
access_key = api_key.read()
access_key = access_key[:-1]

api_url = "http://api.marketstack.com/v1/intraday/latest"

stocks = open("stocks.txt","r")
stocks = stocks.read()
print("Stocks to watch: "+stocks)


#Initiaziled

print("API REQUEST: "+api_url +"?access_key="+access_key+"&symbols="+stocks)

#API Request
r = requests.get(api_url +"?access_key="+access_key+"&symbols="+stocks)
if (r.status_code != 200):
    print("API Request failed !")
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
    
    print("\033[1;32;40m"+stocks[count]+'\033[0m'+' opening '+'\033[33m'+str(opening_price)+'\033[0m')
    print("\033[1;32;40m"+stocks[count]+'\033[0m'+' last '+'\033[33m'+str(last_price)+'\033[0m')
    
    #calculate percentage
    try:
        percentage = last_price / opening_price
    except:
        print("No latest data")
   #stock + 
    if (percentage > 1 and last_price != "None"):
        percentage = str(percentage)
        percentage = percentage[3:]
        percentage = percentage[:2]
        percentage = percentage[:1]+','+percentage[1:]
        print("\033[32m"+"+"+percentage+"\033[0m"+" today")
    
    #stock -
    if (percentage < 1 and last_price != "None"):
        percentage = str(percentage)
        percentage = percentage[3:]
        percentage = percentage[:2]
        percentage = percentage[:1]+','+percentage[1:]
        print("\033[31m"+"-"+percentage+"\033[0m"+" today")

    if('percentage' not in locals()):
        print("percentage could not be calculated")
        exit()
    
    count = count +1
    print("\n")


