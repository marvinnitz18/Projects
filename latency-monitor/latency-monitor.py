#!/usr/bin/python3

from pythonping import ping
import matplotlib.pyplot as plt

x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()


def get_latency(host):
   try:
      result = str(ping(host,count=1))
      result = result.split(" ")
      result = result[6]
      result = result[:-9]
      return result
   except:
      print("Ping failed")



print(get_latency("1.1.1.1"))