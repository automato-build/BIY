import pyttsx3
import time

engine = pyttsx3.init("espeak")

rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

# voices = engine.getProperty('voices')

def set_voice_gender(gender):
	gender.lower()
	if gender == 'male':
		voices = engine.getProperty('voices')
		engine.setProperty('voice', 'english+v1') 
	elif gender == 'female':
		voices = engine.getProperty('voices')
		engine.setProperty('voice', 'english+f4') 
	else:
		voices = engine.getProperty('voices')
		engine.setProperty('voice', 'english+v1') 

def say_bullshit(text):
	if isinstance(text, str):
		engine.say(text)
	else:
		engine.say("Can not say these unwise words !")
	engine.runAndWait()


# set_voice_gender("male")
# bullshit("Hello there Matthiew. Howdy!")