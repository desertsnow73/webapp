import RPi.GPIO as GPIO
import os
from time import sleep
from flask import abort, redirect, url_for

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

sound = 24
led = 8

GPIO.setup(sound, GPIO.IN)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

@app.route('/<int:stat>')
def sound_led(stat):
	if stat == 1:
		try:	
			while 1:
       			
				#soundlvl = GPIO.input(sound)
       			#print "soundlvl", soundlvl
				
       			#if soundlvl > 0:
				os.system("curl http://192.168.0.114:8888/LED/ON")
				return 'LED ON'

		except KeyboardInterrupt:
    		pass

	elif stat == 0:
		try:	
   			while 1:
				
       			#soundlvl = GPIO.input(sound)
       			#print "soundlvl", soundlvl
				
       			#if soundlvl < 1:
				os.system("curl http://192.168.0.114:8888/LED/OFF")
        	    return 'LED OFF'

		except KeyboardInterrupt:
    		pass

GPIO.cleanup()

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8889)
