# --------------------------------------------
# -------- LISTENER SST ENGINE THREAD --------
# --------------------------------------------

import json
from os import path
import speech_recognition as sr
import led_status as LED_STATUS


# ----  google cloud speech recognition api call
# -------------------------------------------
google_cred_file = 'api_creds/google_creds.json' # for my mac
# google_cred_file = 'onpi-231216-b5edbccb7198.json.json' # for my pi

def get_google_creds(_google_cred_file):
	with open(_google_cred_file, "r") as f:
		data = f.read()
	return str(data)

def recognize_speech_from_mic_using_google(recognizer, microphone):
	print("\nSTATUS: LISTENING...")
	with microphone as source:
		# recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	# set up the response object
	response = {"success": True, "error": None,"transcription": None}

	GOOGLE_CLOUD_SPEECH_CREDENTIALS = get_google_creds(google_cred_file)

	LED_STATUS.recognizing()
	print("STATUS: RECOGNIZING...")
	try:
		response["transcription"] = recognizer.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
	except sr.UnknownValueError:
		# API was unreachable or unresponsive
		response["success"] = False
		response["error"] = "Unable to recognize speech"
		pass
	except sr.RequestError as e:
		# speech was unintelligible
		response["error"] = "API unavailable"
		pass
	return response



# ----  wit.ai speech recognition api call
# -------------------------------------
wit_ai_cred_file = 'api_creds/wit_ai_creds.json'
def get_wit_ai_creds(_wit_ai_cred_file):
	with open(_wit_ai_cred_file) as f:
		key = json.load(f)
		key_val = str(key["KEY"])
	return str(key_val)

def recognize_speech_from_mic_using_wit_ai(recognizer, microphone):
	print("\nSTATUS: LISTENING...")
	with microphone as source:
		# recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	# set up the response object
	response = {"success": True, "error": None,"transcription": None}

	WIT_AI_CREDENTIALS = get_wit_ai_creds(wit_ai_cred_file)

	print("STATUS: RECOGNIZING...")
	try:
		# wit.ai results doen't capitalize and without capilatization we later cxan't find names. 
		# So that's why .title()
		response["transcription"] = str(recognizer.recognize_wit(audio, key=WIT_AI_CREDENTIALS)).title() 
	except sr.UnknownValueError:
		# API was unreachable or unresponsive
		response["success"] = False
		response["error"] = "Unable to recognize speech"
		pass
	except sr.RequestError as e:
		# speech was unintelligible
		response["error"] = "API unavailable"
		pass
	return response




# ----  microsoft azure speech recognition api call
# -------------------------------------
azzure_cred_file = 'api_creds/azzure_creds.json'

def get_azzure_creds(_azzure_cred_file):
	with open(_azzure_cred_file) as f:
		key = json.load(f)
		key_val = str(key["KEY"])
	return str(key_val)

def recognize_speech_from_mic_using_azzure(recognizer, microphone):
	print("\nSTATUS: LISTENING...")
	with microphone as source:
		# recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	# set up the response object
	response = {"success": True, "error": None,"transcription": None}

	AZZURE_CREDENTIALS = get_azzure_creds(azzure_cred_file)

	print("STATUS: RECOGNIZING...")
	try:
		response["transcription"] = recognizer.recognize_bing(audio, key=AZZURE_CREDENTIALS)
	except sr.UnknownValueError:
		# API was unreachable or unresponsive
		response["success"] = False
		response["error"] = "Unable to recognize speech"
		pass
	except sr.RequestError as e:
		# speech was unintelligible
		response["error"] = "API unavailable"
		pass
	return response



# ----  houndify speech recognition api call
# -------------------------------------
houndify_cred_file = 'api_creds/houndify_creds.json'

def get_houndify_creds(_houndify_cred_file):
	with open(_houndify_cred_file) as f:
		creds = json.load(f)
	return creds

def recognize_speech_from_mic_using_houndify(recognizer, microphone):
	print("\nSTATUS: LISTENING...")
	with microphone as source:
		# recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	# set up the response object
	response = {"success": True, "error": None,"transcription": None}

	HOUNDIFY_CREDENTIALS = get_houndify_creds(houndify_cred_file)
	HOUNDIFY_CLIENT_ID = HOUNDIFY_CREDENTIALS["CLIENT_ID"]
	HOUNDIFY_CLIENT_KEY = HOUNDIFY_CREDENTIALS["KEY"]

	print("STATUS: RECOGNIZING...")
	try:
		# houndify results doen't capitalize and without capilatization we later cxan't find names. 
		# So that's why .title()
		response["transcription"] = str(recognizer.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, 
			client_key=HOUNDIFY_CLIENT_KEY)).title()
	except sr.UnknownValueError:
		# API was unreachable or unresponsive
		response["success"] = False
		response["error"] = "Unable to recognize speech"
		pass
	except sr.RequestError as e:
		# speech was unintelligible
		response["error"] = "API unavailable"
		pass
	return response





counter = 0
def listen():
	global counter
	# -------- >> create recognizer and microphone instances << ------- #
	recognizer = sr.Recognizer()

	# Most of the times default will work but in SBCs like Pi, one might not have a default 
	# mic then you can use this below static method to list your device and use it with 
	# device_index in the mic instance
	# print(sr.Microphone.list_microphone_names())
	# microphone = sr.Microphone(device_index=3)

	microphone = sr.Microphone()

	print("\n>> Using Microsoft Azzure cloud speech api")
	sst_guess = recognize_speech_from_mic_using_azzure(recognizer, microphone)

	# if counter < 10:
	# 	print("\n>> Using Google cloud speech api")
	# 	sst_guess = recognize_speech_from_mic_using_google(recognizer, microphone)
	# if counter >= 10 and counter < 20:
	# 	print("\n>> Using Microsoft Azzure cloud speech api")
	# 	sst_guess = recognize_speech_from_mic_using_azzure(recognizer, microphone)
	# if counter >=20 and counter < 40:
	# 	print("\n>> Using WIT.AI speech api")
	# 	sst_guess = recognize_speech_from_mic_using_wit_ai(recognizer, microphone)
	# if counter >=40 and counter < 60:
	# 	print("\n>> Using Houndify speech api")
	# 	sst_guess = recognize_speech_from_mic_using_houndify(recognizer, microphone)
	# if counter >= 60:
	# 	counter = 0

	# counter = counter+1

	# print(sst_guess)
	return sst_guess

# print(listen())