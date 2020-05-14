Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import RPi.GPIO as GPIO             
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
for x in range(0,3):
    GPIO.output(4,True)
    time.sleep(3)
    GPIO.output(4,False)
    time.sleep(1)
GPIO.cleanup()