'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
# Create a dictionary called pins to store the pin number, name, and pin state:
f = open('/home/pi/webserver/pin_status.csv','r')
pins = eval(f.read())
f.close()

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, pins[pin]['state'])

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   #for pin in pins:
   #   pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   f = open('/home/pi/webserver/pin_status.csv','r')
   pins = eval(f.read())
   f.close()
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
      pins[changePin]['state'] = GPIO.HIGH

   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."
      pins[changePin]['state'] = GPIO.LOW

   f = open('/home/pi/webserver/pin_status.csv','w')
   f.write(str(pins))
   f.close()
   # For each pin, read the pin state and store it in the pins dictionary:
   '''for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)'''

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
