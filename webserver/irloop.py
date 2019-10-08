'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

'''
import pylirc
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# Create a dictionary called pins to store the pin number, name, and pin state:
f = open('/home/pi/webserver/pin_status.csv','r')
pins = eval(f.read())
f.close()
pylirc.init( 'pylirc', '/home/pi/pylirc.conf', 0 )

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, pins[pin]['state'])


while ( True ) :
   s = pylirc.nextcode( 1 )
   command = None
   if ( s ) :
      for ( code ) in s :
         f = open('/home/pi/webserver/pin_status.csv','r')
         pins = eval(f.read())
         f.close()
         print( code["config"] )
         if code["config"] == 'MUTE':
            if pins[23]['state'] == GPIO.HIGH:
               GPIO.output(23, GPIO.LOW)
               pins[23]['state'] = GPIO.LOW
            else:
               GPIO.output(23, GPIO.HIGH)
               pins[23]['state'] = GPIO.HIGH
         elif code["config"] == 'POWER_ON':
            if pins[18]['state'] == GPIO.HIGH:
               GPIO.output(18, GPIO.LOW)
               pins[18]['state'] = GPIO.LOW
            else:
               GPIO.output(18, GPIO.HIGH)
               pins[18]['state'] = GPIO.HIGH
         elif code["config"] == 'VOL_DOWN':
            if pins[22]['state'] == GPIO.HIGH:
               GPIO.output(22, GPIO.LOW)
               pins[22]['state'] = GPIO.LOW
            else:
               GPIO.output(22, GPIO.HIGH)
               pins[22]['state'] = GPIO.HIGH
         elif code["config"] == 'VOL_UP':
            if pins[19]['state'] == GPIO.HIGH:
               GPIO.output(19, GPIO.LOW)
               pins[19]['state'] = GPIO.LOW
            else:
               GPIO.output(19, GPIO.HIGH)
               pins[19]['state'] = GPIO.HIGH
         f = open('/home/pi/webserver/pin_status.csv','w')
         f.write(str(pins))
         f.close()

