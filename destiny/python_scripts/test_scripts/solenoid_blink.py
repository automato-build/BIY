import RPi.GPIO as GPIO   
from time import sleep     

GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BCM)

solenoid_pin = 19
GPIO.setup(solenoid_pin, GPIO.OUT, initial=GPIO.LOW)  

try:
	while True: 
		GPIO.output(solenoid_pin, 1) 
		sleep(0.1)
		GPIO.output(solenoid_pin, 0)
		sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()