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
from multiprocessing import Process


destiny_number = 0
found_name = ""


def utter_namank_from_received_string(string_data):
    global destiny_number
    global found_name

    # clean strings of any speacial character as
    # softwareserial from ATMEGA sometimes introduces garbage
    str_data = ''.join(e for e in string_data if e.isalnum())
    str_data = str_data.lower()
    # string_data = string_data.lower()


    found_name = str_data

    print(" => Starting the process\n")
    print("\n => Ringing auspicious bell")
    bell_module.ring(10, 0.1)
    print("\n => STATUS: FOUND NAMES:")
    sadhu.say("found_names:")
    LED_STATUS.found_names()
    print("\n" + found_name + "\n")
    print("\nSTATUS: PREDICTIONS.")
    # ring the bell (hit solenoid 15 for 0.1 sec)
    bell_module.ring(10, 0.1)
    # Chant before starting prediction
    sadhu.say("om")
    sadhu.say("name_header")
    sadhu.say_name(str(found_name))

    SN = destiny.soul_number(found_name)
    destiny_number = SN
    SD = destiny.soul_desires(found_name)

    print("\n")
    print("-----------------------------------------")
    print("Soul Desire Destiny Number: " + str(SN))
    print("-----------------------------------------")
    print(SD)
    print("\n")
    sadhu.say("desire_header")
    sadhu.say_number(str(SN))
    time.sleep(1)
    sadhu.say('su' + str(SN))
    
    # ring the bell (hit solenoid 4 timesfor 0.25 sec) marking
    # the end of one prediction
    print("\n => Ringing auspicious bell")
    bell_module.ring(10, 0.1)
    LED_STATUS.deactivate()


def find_names_utter_namank():
    global destiny_number
    global found_name

    print(" => Starting the process")
    time.sleep(2)
    sadhu.say("start")
    LED_STATUS.listening()

    time.sleep(0.5)
  

    # 1. --- > do speech recognition and SST < --- #
    listened_result = listener.listen()
    LED_STATUS.recognizing()

    if listened_result["success"] == True and listened_result["error"] == None:
        sentence = str(listened_result["transcription"])
        print("\n => STATUS: RECOGNIZED SST")
        print("\n => SST: " + sentence)

        # 2. --- > Do name recognition within speech < --- #
        names = nr.get_names(sentence)

        if names == 'no valid names found':
            print("\n => STATUS: No names found. Try Again!")
            print("\n => Start Again! hit the Bell")

            LED_STATUS.no_names()
            sadhu.say("noNames")

            destiny_number = None
            found_name = None
        else:
            print("\n => STATUS: FOUND NAMES:")
            sadhu.say("found_names")
            LED_STATUS.found_names()

            # pretty print the names list
            for name in names:
                # clean strings of any speacial character as we need one piece of string
                name = ''.join(e for e in name if e.isalnum())
                name = name.lower()
                print(name)
                found_name = name

            print("\n => STATUS: PREDICTIONS:")
            # 3. --- > Do destiny findings < --- #
            for found_name in names:
                found_name = ''.join(e for e in name if e.isalnum())
                found_name = found_name.lower()
                print("\n" + found_name + "\n")
                print("\n => Ringing auspicious bell")
                # ring the bell (hit solenoid 15 for 0.1 sec)
                bell_module.ring(10, 0.1)
                # Chant before starting prediction
                sadhu.say("om")
                sadhu.say("name_header")
                sadhu.say_name(str(found_name))

                SN = destiny.soul_number(found_name)
                destiny_number = SN
                SD = destiny.soul_desires(found_name)

                print("\n")
                print("-----------------------------------------")
                print("Destiny Number and Heart Desire: " + str(SN))
                print("-----------------------------------------")
                print(SD)
                print("\n")
                sadhu.say("desire_header")
                sadhu.say_number(str(SN))
                time.sleep(1)
                sadhu.say('su' + str(SN))

                

            # ring the bell (hit solenoid 4 timesfor 0.25 sec) marking
            # the end of one prediction
            print("\n => Ringing auspicious bell")
            bell_module.ring(10, 0.1)
            LED_STATUS.deactivate()
    else:
        print(listened_result["success"])
        print(listened_result["error"])
        print("\n => Start Again! hit the Bell")

        LED_STATUS.no_names()
        sadhu.say("noNames")

        destiny_number = None
        found_name = None


portOpen = False
incoming_serial_data = ""
process_start_flag = "start"
process_stop_flag = "stop"
data_for_atmega = ""


if __name__ == "__main__":

    print("\n => System Ready! \n")

    portOpen = serial_module.initialize()

    try:
        if portOpen:
            print(" => SERIAL PORT opened!")
            time.sleep(1)
            print(" => WAITING for Data :)")
            LED_STATUS.defaultOn()

            while True:
                incoming_serial_data = serial_module.read_data()
                if incoming_serial_data != None:
                    if incoming_serial_data == process_stop_flag:
                        print(" xxx -- stop flag: do nothing --- xxx")

                    if incoming_serial_data == process_start_flag:
                        print(" => Received \"start\" flag..")

                        find_names_utter_namank()

                        # ----> If the process takes too long here.. make some adjustments <----#
                        # We create a Process
                        # recognition_process = Process(target=find_names_utter_namank())
                        # We start the process and we block for certain time .
                        # recognition_process.start()
                        # recognition_process.join(timeout=20)
                        # recognition_process.join(20)
                        # If thread is still active
                        # if recognition_process.is_alive():
                            # print "It's still running, meaning it's hung, let's kill it"
                            # Terminate
                            # recognition_process.terminate()
                            # recognition_process.join()
                            # found_name == None
                            # destiny_number == None
                            # put a voice here : Okay the nlp hung again. Please restart after 6 sec
                            # sadhu.say("noNames")
                        # ---------------------------------->><<--------------------------------#


                        data_for_atmega = str(found_name) + "," + str(destiny_number) + ":"
                        data_for_atmega = data_for_atmega.encode('utf-8')

                        if found_name != None and destiny_number != None:
                            print("\n => Process finished. Data to be sent to ATMEGA: " + str(data_for_atmega))
                            serial_module.write_data(data_for_atmega)
                            time.sleep(2)
                        elif found_name == None and destiny_number == None:
                            print("\n => process Finished. Sending \"no_data\" flag to enable ATMEGA: no_data,0:")                        
                            serial_module.write_data("no_data,0:".encode('utf-8'))
                            time.sleep(2)

                    if (incoming_serial_data != process_start_flag and 
                            incoming_serial_data != process_stop_flag and 
                            len(incoming_serial_data) > 1):
                        print(" => Received a STRING: " + str(incoming_serial_data))

                        utter_namank_from_received_string(str(incoming_serial_data))


                        data_for_atmega = str(incoming_serial_data) + "," + str(destiny_number) + ":" 
                        data_for_atmega = data_for_atmega.encode('utf-8')

                        if found_name != None and destiny_number != None:
                            print("\n => Process finished. Data to be sent to ATMEGA: " + str(data_for_atmega))
                            serial_module.write_data(data_for_atmega)
                            time.sleep(2)
                        elif found_name == None and destiny_number == None:
                            print("\n => process Finished. Sending \"no_data\" flag to enable ATMEGA: no_data,0:")                        
                            serial_module.write_data("no_data,0:".encode('utf-8'))
                            time.sleep(2)


                    print("\n--------------------------------------------\n")
                    LED_STATUS.defaultOn()
        else:
            print("Serial port can not be opened. Check if it is engaged somewhere else")
            bell_module.cleanupGPIO()
            LED_STATUS.cleanupGPIO()
            exit()
                        
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