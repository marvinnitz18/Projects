#!/usr/bin/python3

from pythonping import ping
import matplotlib.pyplot as plt

x = []
y = []
i = 0
  
def get_latency(host):
   result = str(ping(host,count=1))
   result = result.split(" ")
   result = result[6]
   result = result[:-9]
   x.append(str(result))
   return result



for x in range(5):
   get_latency("1.1.1.1")
   y.append(str(i))
   i = i + 1

plt.plot(x, y)
  

plt.xlabel('x - axis')
plt.ylabel('y - axis')
  
plt.title('My first graph!')
plt.show()