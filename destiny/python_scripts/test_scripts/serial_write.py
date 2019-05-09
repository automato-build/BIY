import serial
import time
# import RPi.GPIO as GPIO

#/dev/ttyAMA0'
try:
	ser = serial.Serial(
		port='/dev/ttyAMA0',
		baudrate=9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=10
	)
	print ("Serial opened")
	time.sleep(2)
	# ser.write(b'Hello from python;')
	ser.write(b'Helen|8|You are influenced by Saturn. You want to be a leader in work. You want security in finance and authority. You want to be a big brother.|9|You have an emphasis by Saturn. You are able to draw your picture as successful administrators or business man. You have a great attractive personality.;')
	ser.flush()
	time.sleep(2)
	print(">>data sent")
except e:
	print(e)
	pass
finally:
	# ser.close()
	pass

print("Serial closed")

