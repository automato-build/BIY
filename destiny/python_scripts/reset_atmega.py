'''
close serial port
'''

import os
import time

# kill the other python process where serial port is associated already
print(" => killing \"main.py\" to disable it's serial connectivity to ATMEGA")
time.sleep(1)
try:
	os.system('pkill -f main.py >/dev/null 2>&1')
except Exception as e:
	print("Couldn't kill \"main_destiny_logger.py\". It might not be running")

# attch to serial port
print(" => Initializing Serial module here")
time.sleep(1)

try:
	import serial_module
	serial_module.initialize()
	# write reset command which the ATMEGA would be listening for.
	# the data structure ["string,number:"] is same from the main script to write data to ATMEGA
	print(" => Sending reset command!")
	time.sleep(1)
	serial_module.write_data("rst,0:".encode('utf-8'))
	# close serial port
	print(" => Closing this Serial connectivity here!")
	time.sleep(1)
	serial_module.close()
	time.sleep(1)
	print(" => Please start \"main_destiny_logger.py\" again.\n")

	exit()
except Exception as e:
	print("Coouldn't establish Serial with ATMEGA. Check if something else is connected to that port.")






