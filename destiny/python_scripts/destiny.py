'''
DESTINY NUMBER is known as expression number or Namanak (in Hindi). 
This number says what you are and what the destiny store for you to become. 
Pythagorean method calculates numbers from 1 to 9 with Sciemntific names. 

Under destiny number you have:
1. Pythagorean Numerology Heart Desire Number / Soul Urge Number Meaning 
and Prediction algorithm as envisioned by www.astrolookup.com since 2019
2. Pythagorean Numerology Personality Number or Inner Dream Number Meaning 
and Prediction algorithm as envisioned by www.astrolookup.com since 2019
'''
# character map for destiny numbers

destiny_char_map_list = ['ajs', 'bkt', 'clu', 'dmv', 'enw', 'fox', 'gpy', 'hqz', 'ir']
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'


import json
texts_file = 'destinies.json'

with open(texts_file) as f:
    texts = json.load(f)

soul_urge_texts = texts["soul_urge_texts"]
dream_texts = texts["dream_texts"]


# -------------------------------------------------------
# For Soul Urge or Heart Desire number: Use sum of vowels
# -------------------------------------------------------
def assign_vowels_to_number(_word):
	string = _word.casefold()
	# 
	char = []
	char_numbers = []
	for char in string:
		if char in vowels:
			for destiny_chars in destiny_char_map_list:
				if char in destiny_chars:
					char_numbers.append(int(destiny_char_map_list.index(destiny_chars))+1)	
	return char_numbers

# ------------------------------------------------------------
# For Personality or Inner Dream number: Use sum of consonents
# ------------------------------------------------------------
# def assign_consonants_to_number(_word):
# 	string = _word.casefold()
# 	# 
# 	char = []
# 	char_numbers = []
# 	for char in string:
# 		if char in consonants:
# 			for destiny_chars in destiny_char_map_list:
# 				if char in destiny_chars:
# 					char_numbers.append(int(destiny_char_map_list.index(destiny_chars)))
# 	return char_numbers

# example: 
# 13
# 1+3
# 4
def summation(input_number):
	input_number = str(input_number)
	value = 0
	for x in input_number:
		value += int(x)
	return value

def reduced_sum(_char_numbers_list):
	actual_sum = int(sum(_char_numbers_list))	
	while actual_sum > 9:
		actual_sum = int(summation(actual_sum))
	return actual_sum
 
# ---------------------------------------------------------------------------
# -------- Find Heart Desire / Soul Urge  number and assign findings --------
# ---------------------------------------------------------------------------
def soul_number(_word):
	char_numbers_list = assign_vowels_to_number(_word)
	soul_desire_number = int(reduced_sum(char_numbers_list))
	return soul_desire_number

def soul_desires(_word):
	soul_desire_number = soul_number(_word)
	if int(soul_desire_number) in range(1, 9):
		return soul_urge_texts[soul_desire_number-1]

def soul_desires_of_number_only(_num_only):
	soul_desire_number = _num_only
	if int(soul_desire_number) in range(1, 9):
		return soul_urge_texts[soul_desire_number-1]


# ---------------------------------------------------------------------------
# -------- Find Personality / Inner dream number and assign findings --------
# ---------------------------------------------------------------------------
# def inner_dream_number(_word):
# 	char_numbers_list = assign_consonants_to_number(_word)
# 	dream_number = int(reduced_sum(char_numbers_list))
# 	return dream_number

# def inner_dreams(_word):
# 	dream_number = inner_dream_number(_word)
# 	if int(dream_number) in range(1, 10):
# 		return dream_texts[dream_number-1]