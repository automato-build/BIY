import serial
import time
import threading

# import RPi.GPIO as GPIO

send_to_arduino = True

ser = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

print("Serial opened")
time.sleep(2)  # this is needed as arduino RESETs after opening serial port


def write_data():
    global ser
    global send_to_arduino

    # while True:
    #     # print(send_to_arduino)
    #     if send_to_arduino == True:
    #         ser.write(
    #             b"Helen|8|You are influenced by Saturn. You want to be a leader in work. You want security in finance and authority. You want to be a big brother.|9|You have an emphasis by Saturn. You are able to draw your picture as successful administrators or business man. You have a great attractive personality.;"
    #         )
    #         ser.flush()
    #         send_to_arduino = False
    #     time.sleep(0.2)


def read_data():
    global ser
    global send_to_arduino

    while True:
    	msg = str(ser.readline().decode('utf-8').rstrip())
    	if(len(msg) > 0):
    		print(msg)
	    	# time.serialep(0.1)
	        # msg = str(raw_msg[2 : len(raw_msg) - 5])
	        # print(msg)
	        # if msg == "next":
	        #     send_to_arduino = True
	        # else:
	        #     send_to_arduino = False


if __name__ == "__main__":

    # thread1 = threading.Thread(target=read_data)
    # thread2 = threading.Thread(target=write_data)
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    
    try:
    	thread1 = threading.Thread(target=read_data)
    	thread1.start()
    	thread1.join()
    	# write_data()
    except KeyboardInterrupt:
    	print("done")
    	ser.close()
