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
import RPi.GPIO as GPIO
import bell_module
import led_status as LED_STATUS

# GPIO PIN Declarations
voice_change_pin = 25
process_activation_pin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

voice = "male"


def voice_button_callback(pin):
	global voice
	pin_status = int(GPIO.input(pin))
	if pin_status == 0:
		print("\n == > Setting voice for next announcements as FEMALE \n")
		sadhu.set_voice_gender("female")
		voice = "female"
	else:
		print("\n == > Setting voice for next announcements as MALE \n")
		sadhu.set_voice_gender("male")
		voice = "male"



def utter_main_namank():
	print ("== starting the process == \n")

	time.sleep(2)

	# Turn BLUE LED here to indicate :listening:
	LED_STATUS.listening()

	# 1. --- > do speech recognition and SST < --- # 
	listened_result = listener.listen()
	
	# LED_STATUS.recognizing()

	if listened_result["success"] == True and listened_result["error"] == None:

		sentence = str(listened_result["transcription"])
		
		print("STATUS: RECOGNIZED SST\n")
		print("SST: " + sentence + "\n")

		# 2. --- > Do name recognition within speech < --- # 
		names = nr.get_names(sentence)

		if names == 'no valid names found':
			print("STATUS: No names found. Try Again!")

			LED_STATUS.no_names()
			time.sleep(2.5)
			LED_STATUS.deactivate()

			print("\n=> Press Button to start Again! <=\n")
		else:
			print("STATUS: FOUND NAMES\n")
			bell_module.ring(30, 0.1)
			LED_STATUS.found_names()

			# pretty print the names list
			for name in names:
				print(name)

			time.sleep(1)

			print("============\n")
			print("\nSTATUS: PREDICTIONS..")
			# 3. --- > Do destiny findings < --- #
			for name in names:
				# ring the bell (hit solenoid twice for 0.25 sec)
				bell_module.ring(30, 0.1)

				time.sleep(1)

				# Setup the voice here before every loop
				# print(voice)
				sadhu.set_voice_gender(voice)

				# Chant before starting prediction
				sadhu.say_bullshit("ommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
				
				print("\n" + name + "\n")
				
				sadhu.say_bullshit("So for name " + str(name))

				SN = destiny.soul_number(name)
				SD = destiny.soul_desires(name)
				IDN = destiny.inner_dream_number(name)
				IDS = destiny.inner_dreams(name)
				print("-----------------------------------------")
				print("Soul Urge Number / Heart Desire Number: " + str(SN))
				print("-----------------------------------------")
				print(SD)

				sadhu.say_bullshit("Your desire number also called soul urge number is " + str(SN))
				time.sleep(2)
				sadhu.say_bullshit(str(SD))

				time.sleep(3)

				print("------------------------------------------------------")
				print("Numerology Personality Number / Inner Dream Number " + str(IDN))
				print("------------------------------------------------------")
				print(IDS)

				sadhu.say_bullshit("Your personality number also called inner dream number is " + str(IDN))
				time.sleep(2)
				sadhu.say_bullshit(str(IDS))

				# serial.pritn("name,6,jhsfgbhsbf,6, sdghvfsghdf;")

				print("\n*************** ^^^ **************")

			# ring the bell (hit solenoid 4 timesfor 0.25 sec) marking the ned of one prediction
			bell_module.ring(30, 0.1)
			print("\n=> Press Button to start Again! <=\n")
			LED_STATUS.deactivate()
	else:
		print(listened_result["success"])
		print(listened_result["error"])
		print("\n=> Press Button to start Again! <=\n")

		LED_STATUS.no_names()
		time.sleep(2.5)
		LED_STATUS.deactivate()



if __name__ == "__main__":
	GPIO.setup(voice_change_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(process_activation_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.add_event_detect(process_activation_pin, GPIO.BOTH, bouncetime=300)

	print("\n => System Ready. Press Button to start! \n")
	# TBD glow a light here 

	try:
		# for changing voice
		GPIO.add_event_detect(voice_change_pin, GPIO.BOTH, callback=voice_button_callback, bouncetime=300)

		while True:
			if GPIO.event_detected(process_activation_pin):
				if int(GPIO.input(process_activation_pin)) == 0:
					utter_main_namank()
	except KeyboardInterrupt:
		GPIO.cleanup()
		exit()
	finally:
		GPIO.cleanup()