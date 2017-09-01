from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__) #make instance

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route('/LED/ON')
def led_on():
	GPIO.output(8, GPIO.HIGH)
	return 'LED ON'

@app.route('/LED/OFF')
def led_off():
	GPIO.output(8, GPIO.LOW)
	return 'LED OFF'

@app.route('/')
def index():
	return 'This is the Homepage'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888)

