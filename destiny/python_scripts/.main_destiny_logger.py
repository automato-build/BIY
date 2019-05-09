'''
-----------------------------------------------------------------------------------------
TBD: 
[....] 11. Network Setup for first boots . Also STYLE it
-----------------------------------------------------------------------------------------
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


# sadhu.say("filename_from_the_voices_dir") # aplay plays a file 
# sadhu.say_name("") # espeak speaks under the hood by system call
# sadhu.say_number("") # espeak speaks under the hood by system call
destiny_number = 0

def utter_namank_from_received_string(string_data):
	print ("== starting the process == \n")
	bell_module.ring(20, 0.2)
	print("STATUS: FOUND NAMES\n")
	sadhu.say("found_names")
	LED_STATUS.found_names()
	print(string_data)
	print("============\n")
	print("\nSTATUS: PREDICTIONS.")
	# ring the bell (hit solenoid 15 for 0.1 sec)
	bell_module.ring(15, 0.1)
	# Chant before starting prediction
	sadhu.say("om")
	sadhu.say("name_header")
	sadhu.say_name(str(string_data))

	SN = destiny.soul_number(string_data)
	destiny_number = SN
	SD = destiny.soul_desires(string_data)
	# IDN = destiny.inner_dream_number(string_data)
	# IDS = destiny.inner_dreams(string_data)

	print("\n")
	print("-----------------------------------------")
	print("Soul Urge Number / Heart Desire Number: " + str(SN))
	print("-----------------------------------------")
	print(SD)
	print("\n")
	sadhu.say("desire_header")
	sadhu.say_number(str(SN))
	time.sleep(1)
	sadhu.say('dt'+str(SN))
	# time.sleep(1)
	# print("\n")
	# print("------------------------------------------------------")
	# print("Personality Number / Inner Dream Number: " + str(IDN))
	# print("------------------------------------------------------")
	# print(IDS)
	# print("\n")
	# sadhu.say("personality_header")
	# sadhu.say_number(str(IDN))
	# time.sleep(1)
	# sadhu.say('su'+str(IDN))

	print("\n*************** ^^^ **************")

	# ring the bell (hit solenoid 4 timesfor 0.25 sec) marking the ned of one prediction
	bell_module.ring(20, 0.2)
	LED_STATUS.deactivate()


def find_names_utter_namank():
	print ("== starting the process == \n")
	
	time.sleep(2)

	sadhu.say("start")
	LED_STATUS.listening()
	time.sleep(0.5)

	# 1. --- > do speech recognition and SST < --- # 
	listened_result = listener.listen()
	LED_STATUS.recognizing()

	if listened_result["success"] == True and listened_result["error"] == None:
		sentence = str(listened_result["transcription"])
		print("STATUS: RECOGNIZED SST\n")
		print("SST: " + sentence + "\n")

		# 2. --- > Do name recognition within speech < --- # 
		names = nr.get_names(sentence)

		if names == 'no valid names found':
			print("STATUS: No names found. Try Again!")
			LED_STATUS.no_names()
			sadhu.say("noNames")
		else:
			print("STATUS: FOUND NAMES\n")
			sadhu.say("found_names")
			LED_STATUS.found_names()

			# pretty print the names list
			for name in names:
				print(name)

			print("============\n")
			print("\nSTATUS: PREDICTIONS..")
			# 3. --- > Do destiny findings < --- #
			for name in names:
				print("\n" + name + "\n")

				# ring the bell (hit solenoid 15 for 0.1 sec)
				bell_module.ring(20, 0.2)
				# Chant before starting prediction
				sadhu.say("om")
				sadhu.say("name_header")
				sadhu.say_name(str(name))

				SN = destiny.soul_number(name)
				destiny_number = SN
				SD = destiny.soul_desires(name)
				# IDN = destiny.inner_dream_number(name)
				# IDS = destiny.inner_dreams(name)

				print("\n")
				print("-----------------------------------------")
				print("Soul Urge Number / Heart Desire Number: " + str(SN))
				print("-----------------------------------------")
				print(SD)
				print("\n")
				sadhu.say("desire_header")
				sadhu.say_number(str(SN))
				time.sleep(1)
				sadhu.say('dt'+str(SN))
				# time.sleep(1)
				# print("\n")
				# print("------------------------------------------------------")
				# print("Numerology Personality Number / Inner Dream Number " + str(IDN))
				# print("------------------------------------------------------")
				# print(IDS)
				# print("\n")
				# sadhu.say("personality_header")
				# sadhu.say_number(str(IDN))
				# time.sleep(1)
				# sadhu.say('su'+str(IDN))

				# serial.pritn("name,6,jhsfgbhsbf,6, sdghvfsghdf;")
				print("\n*************** ^^^ **************")

			# ring the bell (hit solenoid 4 timesfor 0.25 sec) marking the ned of one prediction
			bell_module.ring(20, 0.2)
			LED_STATUS.deactivate()
	else:
		print(listened_result["success"])
		print(listened_result["error"])
		print("\n=> Start Again! hit the Bell <=\n")

		LED_STATUS.no_names()
		sadhu.say("noNames")



portOpen = False
incoming_serial_data = ""
process_finish_flag = "finished".encode('utf-8')
process_start_flag = "start"
data_for_atmega = ""


if __name__ == "__main__":
	print("\n => System Ready! \n")

	portOpen = serial_module.initialize()

	try:
		if portOpen:
			print (" => SERIAL PORT opened!")
			time.sleep(2)
			print (" => WAITING for Data :)")
			while True:
				incoming_serial_data = serial_module.read_data()
				if incoming_serial_data != None:
					# print(incoming_serial_data)
					if(incoming_serial_data == process_start_flag):
						print(" => Received \"start\" flag..")
						print("		The process of listening, finding name and numerology should start here")
						#----
						find_names_utter_namank()
						#----
						print(" => Process finished")
						print("		Sending flag \"finished\"\n")
						# serial_module.write_data(process_finish_flag)
						data_for_atmega = str(incoming_serial_data)+","+str(destiny_number)+","+process_finish_flag+":"
						data_for_atmega = data_for_atmega.encode('utf-8')
						serial_module.write_data(data_for_atmega)
					if len(incoming_serial_data) > 1 and incoming_serial_data != "start":
						# that means if it received a string/name from other sensors
						print(" => Received a STRING: " + str(incoming_serial_data))
						print("		The process of numerology should start here")
						#----
						utter_namank_from_received_string(str(incoming_serial_data))
						#----
						print(" => Process finished")
						print("		Sending flag \"finished\"\n")
						# serial_module.write_data(process_finish_flag)
						data_for_atmega = str(incoming_serial_data)+","+str(destiny_number)+","+process_finish_flag+":"
						data_for_atmega = data_for_atmega.encode('utf-8')
						serial_module.write_data(data_for_atmega)

	except KeyboardInterrupt:
		serial_module.close()
		bell_module.cleanupGPIO()
		LED_STATUS.cleanupGPIO()
		exit()


	# try:
	# 	utter_main_namank()
	# except KeyboardInterrupt:
	# 	# GPIO.cleanup()
	# 	exit()