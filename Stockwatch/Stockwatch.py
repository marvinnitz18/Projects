import requests
import json

api_key = open("api.key","r")
access_key = api_key.read()
access_key = access_key[:-1]

api_url = "http://api.marketstack.com/v1/intraday/latest"

stocks = open("stocks.txt","r")
stocks = stocks.read()
print(stocks)


#Initiaziled

print("API REQUEST: "+api_url +"?access_key="+access_key+"&symbols="+stocks)

#API Request
r = requests.get(api_url +"?access_key="+access_key+"&symbols="+stocks)

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
    print(stocks[count]+" "+str(opening_price))
    count = count +1


