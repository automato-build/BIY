#!/usr/bin/env python3
#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
BIY_SEE.

Runs continuous image classification on camera frames and s detected object
classes.

Classes are converted to smorfia numbers sent via serial port to the display.

Example:
image_classification_camera.py --num_frames 10
"""
import argparse
import contextlib
import json
import sys
import time


import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.

SHUT_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SHUT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)



# then do the rest
import serial

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,timeout=1
)

def Shutdown():
    ser.write(("BYE").encode())
    ser.write(str.encode('\n'))
    ser.close()
    os.system("sudo shutdown -h now")


def Reboot():
    ser.write(("BYE").encode())
    ser.write(str.encode('\n'))
    ser.close()
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



from aiy.vision.inference import CameraInference
from aiy.vision.models import image_classification
from picamera import PiCamera


smorfia_data= []#setting those two global variables to 0 because python is stupid
visionToSmorfia_data= []

import os
dir = os.path.dirname(__file__)

def classes_info(classes):
    return ', '.join('%s (%.2f)' % pair for pair in classes)

@contextlib.contextmanager
def CameraPreview(camera, enabled):
    if enabled:
        camera.start_preview()
    try:
        yield
    finally:
        if enabled:
            camera.stop_preview()


def importJsonData():
    with open(os.path.join(dir, "./smorfia.json") , "r", encoding="utf-8" ) as read_file:
        global smorfia_data
        smorfia_data = json.load(read_file)
        #before ing we need to convert everything from unicode to ascii

        smorfia=json.JSONEncoder().encode(smorfia_data)
        (smorfia)

    with open(os.path.join(dir, "./visionToSmorfia.json"), "r", encoding="utf-8" ) as read_file:
        global visionToSmorfia_data
        visionToSmorfia_data = json.load(read_file)
        #before ing we need to convert everything from unicode to ascii
        visionToSmorfia=json.JSONEncoder().encode(visionToSmorfia_data)
        print(visionToSmorfia)

def getClassIndex(className):
    global visionToSmorfia_data

    index=-1;

    for classes in visionToSmorfia_data:
        if classes["classes"][0]==className:
            index=classes["index"]
            return index
    return index

def getSmorfiaNumber(class_index):
    global visionToSmorfia_data
    smorfia_number=0;

    if (visionToSmorfia_data[class_index]["smorfia"]!=None):
        smorfia_number=visionToSmorfia_data[class_index]["smorfia"]

    return(smorfia_number)

def getSmorfiaLabel(number):
    global smorfia_data
    if number>0 and number<=90:
        return(smorfia_data[number]["neopolitan"])
    else:
        return("je nunn' sacc")

def main():
    importJsonData()

    ser.write(("START").encode())
    ser.write(str.encode('\n'))

    parser = argparse.ArgumentParser('Image classification camera inference example.')
    parser.add_argument('--num_frames', '-n', type=int, default=None,
        help='Sets the number of frames to run for, otherwise runs forever.')
    parser.add_argument('--num_objects', '-c', type=int, default=3,
        help='Sets the number of object interences to print.')
    parser.add_argument('--nopreview', dest='preview', action='store_false', default=True,
        help='Enable camera preview')
    args = parser.parse_args()



    with PiCamera(sensor_mode=4, framerate=10) as camera, \
        CameraPreview(camera, enabled=args.preview), \
        CameraInference(image_classification.model()) as inference:
        camera.vflip=True;
        for result in inference.run(args.num_frames):
            classes = image_classification.get_classes(result, top_k=args.num_objects)

            className=classes[0][0].split('/')[0] #this is because I only want one category at the time
            print(className)

            index = getClassIndex(className)
            print(index)

            smorfia_number=getSmorfiaNumber(index)
            print(smorfia_number)

            smorfia_label=getSmorfiaLabel(smorfia_number)
            print(smorfia_label)

            ser.write((str(smorfia_number)).encode())
            ser.write(str.encode(':'))
            ser.write(smorfia_label.encode())
            ser.write(str.encode('\n'))

            print ('\n')
            time.sleep(1)   # Delays for 5 seconds. You can also use a float value.

            if classes:
                camera.annotate_text = '%s (%.2f)' % classes[0]

def closeEverything():
    print("bye bye!")
    ser.write(("BYE").encode())
    ser.write(str.encode('\n'))
    ser.close()

import atexit
atexit.register(closeEverything)

if __name__ == '__main__':
    main()
