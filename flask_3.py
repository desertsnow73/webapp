from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__) #make instance

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

def l_on():
	GPIO.output(8, GPIO.HIGH)

def l_off():
	GPIO.output(8, GPIO.LOW)

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

@app.route('/profile/<username>')
def profile(username):
	return 'Hey there %s' % username

@app.route('/post/<int:post_id>')
def tuna(post_id):
	return '<h2>Post ID is %d</h2>' % post_id

@app.route('/LED/<int:stat>')
def led_stat(stat):
	if(stat == 1):
		l_on()
		return 'LED ON'
	elif(stat == 0):
		l_off()
		return 'LED OFF'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888)

