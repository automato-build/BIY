import RPi.GPIO as GPIO
import time

PPin_listening = 16 #YELLOW

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PPin_listening, GPIO.OUT)


def defaultOn():
	GPIO.output(PPin_listening, 1)


def listening():
	GPIO.output(PPin_listening, 1)
	time.sleep(0.25)
	GPIO.output(PPin_listening, 0)
	time.sleep(0.25)
	GPIO.output(PPin_listening, 1)
	time.sleep(0.25)
	GPIO.output(PPin_listening, 0)
	time.sleep(0.25)
	GPIO.output(PPin_listening, 1)

def recognizing():
	GPIO.output(PPin_listening, 0)
	time.sleep(0.5)
	GPIO.output(PPin_listening, 1)
	time.sleep(0.5)
	GPIO.output(PPin_listening, 0)
	time.sleep(0.5)
	GPIO.output(PPin_listening, 1)

def found_names():
	GPIO.output(PPin_listening, 0)
	time.sleep(1)
	GPIO.output(PPin_listening, 1)
	time.sleep(1)
	GPIO.output(PPin_listening, 0)
	time.sleep(1)
	GPIO.output(PPin_listening, 1)

def no_names():
	GPIO.output(PPin_listening, 1)
	time.sleep(2)
	GPIO.output(PPin_listening, 0)

def deactivate():
	GPIO.output(PPin_listening, 0)

def cleanupGPIO():
	GPIO.cleanup()


# recognizing()