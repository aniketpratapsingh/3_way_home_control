import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
while True:
    GPIO.output(23,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(23,GPIO.LOW)
    time.sleep(0.9)
