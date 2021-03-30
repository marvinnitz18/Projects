import RPi.GPIO as GPIO
import subprocess
import json
import time

process = subprocess.Popen(["sensors","-j"], stdout=subprocess.PIPE)
output, error = process.communicate()

temp = json.loads(output)

temp = temp["cpu_thermal-virtual-0"]["temp1"]["temp1_input"]

print("current temp: ",temp)

GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)
#off
GPIO.output(6, GPIO.LOW)

time.sleep(20)

GPIO.cleanup(6)

print(GPIO.getmode())
