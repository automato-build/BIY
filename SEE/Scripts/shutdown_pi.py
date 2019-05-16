#!/bin/python
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.

SHUT_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SHUT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def Shutdown():
    os.system("sudo shutdown -h now")

def Reboot():
    os.system("sudo reboot")

# Our function on what to do when the button is pressed
def shutdown_reboot(channel):
    global buttonStatus
    start_time = time.time()

    while GPIO.input(channel) == 0: # Wait for the button up
        pass

    buttonTime = time.time() - start_time    # How long was the button down?

    if buttonTime >= 5: #if press for more than 5 seconds reboot
        Shutdown()
    elif buttonTime >= .1: #else reboot the pi
        Reboot()

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(SHUT_PIN, GPIO.FALLING, callback = shutdown_reboot, bouncetime = 2000)


# Now wait!
while 1:
    time.sleep(1)
