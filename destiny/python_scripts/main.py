'''             
THIS IS THE SOURCE CODE USED FOR raspberry Pi linux computer written by Saurabh Datta, 
partner @ automato.farm. Saurabh Datta ---- [www.dattasaurabh.com, hi@dattasaurabh.com]
Copyright (C) 2019 automato.farm - 2019 hi@automato.farm [www.automato.farm] 
- All Rights Reserved
Unauthorized copying of this work, via any medium is strictly prohibited without permission.

NOTE: CHECK license.txt for details
'''

import listener
import name_recognizer as nr
import destiny
import speak_module as sadhu
import time
import bell_module
import led_status as LED_STATUS
import os
import serial_module
from random import randint

# a mapping fucntion similar to arduino and processing
#  we will need it later
def valmap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))


portOpen = False
incoming_serial_data = ""
data_for_atmega = ""


def get_data_from_serial_string(string_data):
    if len(string_data) > 2:
        # to avoid numbers
        return string_data
    else:
        return "None"


def get_heard_sentence():
    listened_result = listener.listen()
    LED_STATUS.recognizing()

    if listened_result["success"] == True:
        sentence = str(listened_result["transcription"])
        return sentence
    else:
        print(listened_result["error"])
        return "None"


def extract_names(sentence):
    names = nr.get_names(sentence)
    if names == 'no valid names found':
        return "None"
    else:
        return names


def say_destiny_from_number_only(n):
    DN = int(n)
    D = str(destiny.soul_desires_of_number_only(DN))

    print("\n => STATUS: PREDICTION:")
    print("-----------------------------------------")
    print("Destiny Number and Heart Desire: " + DN)
    print(D)
    print("-----------------------------------------")

    # ring the bell (hit solenoid 10 for 0.1 sec)
    print(" => Ringing auspicious bell")
    bell_module.ring(10, 0.1)

    # Chant before starting prediction
    sadhu.say("om")

    sadhu.say("desire_header")
    sadhu.say_number(DN)
    time.sleep(1)
    sadhu.say('su' + str(DN))

    # ring the bell (hit solenoid 4 timesfor 0.25 sec) marking
    # the end of one prediction
    print(" => Ringing auspicious bell")
    bell_module.ring(10, 0.1)
    LED_STATUS.deactivate()
    

def assign_destiny_and_destiny_number(name):
    found_name = ''.join(e for e in name if e.isalnum())
    found_name = str(found_name.lower())

    DN = str(destiny.soul_number(found_name))
    D = str(destiny.soul_desires(found_name))

    print("\n => STATUS: PREDICTION:")
    print("-----------------------------------------")
    print(" => NAME: " + found_name)
    print("-----------------------------------------")
    print("Destiny Number and Heart Desire: " + DN)
    print(D)
    print("-----------------------------------------")

    # ring the bell (hit solenoid 10 for 0.1 sec)
    print(" => Ringing auspicious bell")
    bell_module.ring(10, 0.1)

    # Chant before starting prediction
    sadhu.say("om")

    sadhu.say("name_header")
    sadhu.say_name(found_name)
    sadhu.say("desire_header")
    sadhu.say_number(DN)
    time.sleep(1)
    sadhu.say('su' + str(DN))

    # ring the bell (hit solenoid 4 timesfor 0.25 sec) marking
    # the end of one prediction
    print(" => Ringing auspicious bell")
    bell_module.ring(10, 0.1)
    LED_STATUS.deactivate()

    return found_name,DN


def starting_process_assignment(serial_data):
    # 1 --- > EXTRACRT STRING SENTENCE/TEXT < --- #
    # 1.1 --- > Do speech recognition and SST < --- #
    if serial_data == "start":
        print("\n => Starting the listening process")
        time.sleep(2)
        sadhu.say("start")
        LED_STATUS.listening()
        time.sleep(0.5)

        sentence = get_heard_sentence()
        if sentence != "None" and len(sentence) > 0:
            print("\n => STATUS: RECOGNIZED SST")
            print("\n => SST: " + sentence)
            # ::2:: --- > Do name recognition within speech < --- #
            names = extract_names(sentence)
            if names != "None":
                print("\n => STATUS: FOUND NAMES:")
                sadhu.say("found_names")
                LED_STATUS.found_names()
                # ---> pretty print the names list <--- #
                for name in names:
                    print("     " + name)
                # ::3:: --- > Do destiny findings < --- #
                # Send ony one name from the names list if there is many
                if(len(names) >= 1):
                    found_name,DN = assign_destiny_and_destiny_number(names[randint(0, len(names)-1)]);
                    # return the name and number for sending it via serial
                    return found_name,DN
                else:
                    found_name,DN = assign_destiny_and_destiny_number(names[0])
                    # return the name and number for sending it via serial
                    return found_name,DN
            else:
                print("\n => STATUS: No names found. Try Again!")
                print("\n => Start Again! hit the Bell")
                LED_STATUS.no_names()
                sadhu.say("noNames")
                found_name = "None"
                DN = "None"
                return found_name,DN
        else:
            print("\n => STATUS: SST unsuccessful. Try Again!")
            print("\n => Start Again! hit the Bell")
            LED_STATUS.no_names()
            sadhu.say("noNames")
            found_name = "None"
            DN = "None"
            return found_name,DN

    # 1.2 --- > Do String text reception < --- #
    elif (serial_data != "start" and serial_data != "stop" and len(serial_data) > 0) and !serial_data.isdigit():
        print("\n => Starting the string reading process")
        time.sleep(2)
        LED_STATUS.listening()
        time.sleep(0.5)
      
        sentence = get_data_from_serial_string(serial_data)
        if sentence != "None" and len(sentence) > 0:
            print("\n => STATUS: RECOGNIZED VALID STRING")
            print("\n => STRING: " + sentence)
            # ::2:: --- > Do name recognition within speech < --- #
            names = extract_names(sentence)
            if names != "None":
                print("\n => STATUS: FOUND NAMES:")
                sadhu.say("found_names")
                LED_STATUS.found_names()
                # ---> pretty print the names list <--- #
                for name in names:
                    print("     " + name)
                # ::3:: --- > Do destiny findings < --- #
                # Send ony one name from the names list if there is many
                if(len(names) >= 1):
                    found_name,DN = assign_destiny_and_destiny_number(names[randint(0, len(names)-1)]);
                    # return the name and number for sending it via serial
                    return found_name,DN
                else:
                    found_name,DN = assign_destiny_and_destiny_number(names[0])
                    # return the name and number for sending it via serial
                    return found_name,DN
            else:
                print("\n => STATUS: No names found. Try Again!")
                print("\n => Start Again! hit the Bell")
                LED_STATUS.no_names()
                sadhu.say("noNames")
                found_name = "None"
                DN = "None"
                return found_name,DN
        else:
            print("\n => STATUS: serial string not valid. Try Again!")
            print("\n => Try Again by sending valid string. Normal string, you know :)")
            LED_STATUS.no_names()
            sadhu.say("noString")
            found_name = "None"
            DN = "None"
            return found_name,DN

    # 1.3 --- > Do analog value / number reception < --- #
    elif (serial_data != "start" and serial_data != "stop" and len(serial_data) > 0) and serial_data.isdigit():
        print("\n => Starting the numer reading process")
        time.sleep(2)
        LED_STATUS.listening()
        time.sleep(0.5)

        found_name = "noname"
        DNN = int(serial_data)
        DN = int(valmap(DNN, 0, 1022, 1, 9))

        # ::2:: --- > Assign predictions based on numbers < --- #
        if DN != 0 and DN in range(1, 10): # range (5, 8) >>> 5, 6, 7
            print("\n => STATUS: FOUND NUMBER:")
            sadhu.say("numReceived")
            sadhu.say_number(DN)
            LED_STATUS.found_names() # same blink seq doesn't matter

            # ::3:: --- > Do destiny findings < --- #
            say_destiny_from_number_only(DN)
            return found_name,DN
        else:
            print("\n => STATUS: No number found or it was a string or it is not in required range. Try Again!")
            print("\n => Try Again by sending valid number. 1-1022, you know :)")
            LED_STATUS.no_names()
            sadhu.say("noNumber")
            found_name = "None"
            DN = "None"
            return found_name,DN

    elif serial_data == "stop":
        print("\n => STATUS: STOP Flag received! Do not Do anything!")
        found_name = "None"
        DN = "None"
        return found_name,DN
    else:
        found_name = "None"
        DN = "None"
        return found_name,DN


if __name__ == "__main__":
    print("\n => System Firing Up!")
    portOpen = serial_module.initialize()

    try:
        if portOpen:
            #  reset arduino at begining
            print("\n => Resetting Ardunio!")
            serial_module.write_data("rst,0:".encode('utf-8'))
            time.sleep(7)
            print("\n => Reset complete Ardunio! Hopefully :). There was enough delay in between. Fuck handshake!")
            print("\n => Reinitilaizing serial port.. ")
            portOpenedAgain = serial_module.initialize()

            if portOpenedAgain:
                print("\n => SERIAL PORT opened!")
                print("\n => WAITING for Data :)")
                LED_STATUS.defaultOn()

                while True:
                    incoming_serial_data = serial_module.read_data()
                    if incoming_serial_data != None:
                        found_name,DN = starting_process_assignment(str(incoming_serial_data))
                        
                        if found_name != "None" and DN != "None":
                            data_for_atmega = str(found_name) + "," + str(DN) + ":"
                            data_for_atmega = data_for_atmega.encode('utf-8')

                            print("\n => Process finished. Data to be sent to ATMEGA: " + str(data_for_atmega))
                            serial_module.write_data(data_for_atmega)
                            time.sleep(2)

                        if found_name == "None" and DN == "None":
                            print("\n => process Finished. Sending \"no_data\" flag to re-enable ATMEGA: no_data,0:")
                            serial_module.write_data("no_data,0:".encode('utf-8'))
                            time.sleep(2)

                            print("\n--------------------------------------------\n")
                            LED_STATUS.defaultOn()

    except KeyboardInterrupt:
        time.sleep(1)
        print("")
        print(" Resetting atmega ...")
        serial_module.write_data("rst,0:".encode('utf-8'))
        time.sleep(6)
        print(" Closing ..,")
        serial_module.close()
        bell_module.cleanupGPIO()
        LED_STATUS.cleanupGPIO()
        exit()
    except NameError:
        time.sleep(1)
        print("")
        print(" Resetting atmega ...")
        serial_module.write_data("rst,0:".encode('utf-8'))
        time.sleep(6)
        print(" Closing ..,")
        serial_module.close()
        bell_module.cleanupGPIO()
        LED_STATUS.cleanupGPIO()
        exit()
