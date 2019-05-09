import time
import serial

portOpen = False

ser = serial.Serial(
    port="/dev/ttyAMA0",  # for pi
    # port = "/dev/tty.usbserial-AI05HDSG", # for my mac
    baudrate=57600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    # ser.timeout = None,         # block read
    timeout=1            	 	 # non-block read
    # ser.xonxoff = False,     	 # disable software flow control
    # ser.rtscts = False,        # disable hardware (RTS/CTS) flow control
    # ser.dsrdtr = False,        # disable hardware (DSR/DTR) flow control
    # ser.writeTimeout = 1    	 # timeout for write
)


def initialize():
    # CLEAN UP AFTER OPEN
    if ser.isOpen():
        portOpen = True
        ser.flushInput()  # flush input buffer,
        ser.flushOutput()  # flush output buffer,
    else:
        portOpen = False

    return portOpen


def read_data():
    try:
        msg = str(ser.readline().decode('utf-8').rstrip())
        if(len(msg) > 0):
            # print(msg)
            return msg
    except Exception as e:
        print(e)
        ser.close()
        exit()


def flushSerial():
	ser.flushInput()
	ser.flushOutput()


def write_data(message):
    try:
        ser.write(message)
    except Exception as e:
        print(e)
        ser.close()
        exit()


def close():
    ser.close()



# print("writing dummy data")
# data = "Lorenzo,9:".encode('utf-8')
# initialize()
# write_data(data)
