import os

# su1
# dt1
# voice_dir = os.getcwd() + '/voices/'/
# command = 'aplay '+ curr_dir + 'unwise.wav'

# sadhu.say("filename_from_the_voices_dir") # aplay plays a file 
# sadhu.say_name("") # espeak speaks under the hood by system call
# sadhu.say_number("") # espeak speaks under the hood by system call

# Note: Adding '>/dev/null 2>&1' to the os.system call commands silences both stdout and stderr. Not very healthy
# Note: In future use subprocess module istead of OS module

voice_dir = os.getcwd() + '/voices/'

def say(file):
	voice_cmd = 'aplay --device=plughw:1,0 '+ voice_dir + file + '.wav >/dev/null 2>&1'
	os.system(voice_cmd)

def say_name(name):
	os.system('espeak ' + name + ' >/dev/null 2>&1')

def say_number(number):
	os.system('espeak ' + number + ' >/dev/null 2>&1')

