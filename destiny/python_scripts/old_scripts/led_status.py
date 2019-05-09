import RPi.GPIO as GPIO

PPin_listening = 16 #YELLOW
PPin_recognizing = 20 #BLUE
PPin_name_found = 21 #GREEN
PPin_no_names = 24 #RED

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PPin_listening, GPIO.OUT)
GPIO.setup(PPin_recognizing, GPIO.OUT)
GPIO.setup(PPin_name_found, GPIO.OUT)
GPIO.setup(PPin_no_names, GPIO.OUT)

def listening():
	GPIO.output(PPin_listening, 1)
	GPIO.output(PPin_recognizing, 0)
	GPIO.output(PPin_name_found, 0)
	GPIO.output(PPin_no_names, 0)

def recognizing():
	GPIO.output(PPin_listening, 0)
	GPIO.output(PPin_recognizing, 1)
	GPIO.output(PPin_name_found, 0)
	GPIO.output(PPin_no_names, 0)

def found_names():
	GPIO.output(PPin_listening, 0)
	GPIO.output(PPin_recognizing, 0)
	GPIO.output(PPin_name_found, 1)
	GPIO.output(PPin_no_names, 0)

def no_names():
	GPIO.output(PPin_listening, 0)
	GPIO.output(PPin_recognizing, 0)
	GPIO.output(PPin_name_found, 0)
	GPIO.output(PPin_no_names, 1)

def deactivate():
	GPIO.output(PPin_listening, 0)
	GPIO.output(PPin_recognizing, 0)
	GPIO.output(PPin_name_found, 0)
	GPIO.output(PPin_no_names, 0)