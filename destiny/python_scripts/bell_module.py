import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

channel = 19

GPIO.setup(channel, GPIO.OUT)

def move_solenaoid(_delay_val):
	global channel

	GPIO.output(channel, 1)
	time.sleep(_delay_val)
	GPIO.output(channel, 0)
	time.sleep(_delay_val)


def ring(_times, __delay_val):
	for counter in range(0, _times):
		move_solenaoid(__delay_val)

def cleanupGPIO():
	GPIO.cleanup()


# ring(2, 0.25)
# GPIO.cleanup()