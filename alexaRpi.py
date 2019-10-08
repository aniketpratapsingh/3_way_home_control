#Import all the libraries
import RPi.GPIO as GPIO
import time
from pubnub import Pubnub

# Initialize the Pubnub Keys
pub_key = "<your publish key>"
sub_key = "<your subscribe key>"
PINS = [18,19,20,21,22,23,24]
LIGHT = 18           #define pin of RPi on which you want to take output
FAN = 23
NIGHT_LIGHT = 19
BALCONY_LIGHT = 22

#this is to write in a file
f = open('/home/pi/webserver/pin_status.csv','r')
pins = eval(f.read())
f.close()

def init():          #initalize the pubnub keys and start subscribing
    print("INIT")
    global pubnub    #Pubnub Initialization
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LIGHT,GPIO.OUT)
    #GPIO.output(LIGHT, False)
    GPIO.setup(FAN, GPIO.OUT)
    #GPIO.output(FAN, False)
    GPIO.setup(NIGHT_LIGHT, GPIO.OUT)
    #GPIO.output(NIGHT_LIGHT, False)
    GPIO.setup(BALCONY_LIGHT, GPIO.OUT)
    #GPIO.output(BALCONY_LIGHT, False)
    pubnub = Pubnub(publish_key=pub_key,subscribe_key=sub_key)
    pubnub.subscribe(channels='alexaTrigger', callback=callback, error=callback, reconnect=reconnect, disconnect=disconnect)


def control_alexa(controlCommand):          #this function control Aalexa, commands received and action performed
    if(controlCommand.has_key("trigger")):
        if controlCommand["trigger"] == "light":
            if controlCommand["status"] == 1:
                GPIO.output(LIGHT, True)
                print "light is on"
                pins[LIGHT]['state'] = GPIO.HIGH
            else:
                GPIO.output(LIGHT, False)
                print "light is off"
                pins[LIGHT]['state'] = GPIO.LOW
        if controlCommand["trigger"] == "fan":
            if controlCommand["status"] == 1:
                GPIO.output(FAN, True)
                print "fan is on"
                pins[FAN]['state'] = GPIO.HIGH
            else:
                GPIO.output(FAN, False)
                print "fan is off"
                pins[FAN]['state'] = GPIO.LOW
        if controlCommand["trigger"] == "balcony_light":
            if controlCommand["status"] == 1:
                GPIO.output(BALCONY_LIGHT, True)
                print "balcony light is on"
                pins[BALCONY_LIGHT]['state'] = GPIO.HIGH
            else:
                GPIO.output(BALCONY_LIGHT, False)
                print "balcony light is off"
                pins[BALCONY_LIGHT]['state'] = GPIO.LOW
        if controlCommand["trigger"] == "night_light":
            if controlCommand["status"] == 1:
                GPIO.output(NIGHT_LIGHT, True)
                print "night light is on"
                pins[NIGHT_LIGHT]['state'] = GPIO.HIGH
            else:
                GPIO.output(NIGHT_LIGHT, False)
                print "night light is off"
                pins[NIGHT_LIGHT]['state'] = GPIO.LOW
    else:
        pass
    f = open('/home/pi/webserver/pin_status.csv','w')
    f.write(str(pins))
    f.close()



def callback(message, channel):        #this function waits for the message from the aleatrigger channel
    if(message.has_key("requester")):
        control_alexa(message)
    else:
        pass


def error(message):                    #if there is error in the channel,print the  error
    print("ERROR : " + str(message))


def reconnect(message):                #responds if server connects with pubnub
    print("RECONNECTED")


def disconnect(message):               #responds if server disconnects with pubnub
    print("DISCONNECTED")


if __name__ == '__main__':
    init()                    #Initialize the Script
