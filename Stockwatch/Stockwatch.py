import requests
import json

api_key = open("api.key","r")
access_key = api_key.read()
access_key = access_key[:-2]

api_url = "http://api.marketstack.com/v1/intraday/latest"

stocks = open("stocks.txt","r")
stocks = stocks.read()
print(stocks)

#Terminal Input
#stock = input ("Enter your Stock symbol: ")


print("API REQUEST: "+api_url +"?access_key="+access_key+"&symbols="+stocks)

r = requests.get(api_url +"?access_key="+access_key+"&symbols="+stocks)
data = r.json()
data = data['data']

print(data)

