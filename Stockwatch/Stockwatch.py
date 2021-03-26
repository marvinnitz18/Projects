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
    
    print(stocks[count]+' opening '+'\033[31m'+str(opening_price)+'\033[0m')
    print(stocks[count]+' last '+str(last_price))
    
    
    count = count +1
    print("\n")


