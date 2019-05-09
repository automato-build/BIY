# ----------------------------------
# -------- RECOGNIZING NAME --------
# ----------------------------------

# USING SPACY

# import spacy 
# parser = spacy.load('en')


# def get_names(_sentence):
# 	names = []

# 	parsedEx = parser(_sentence)
# 	entities = list(parsedEx.ents)
# 	# print(entities)

# 	if len(entities) > 0:
# 		for entity in entities:
# 			# name = ' '.join(t.orth_ for t in entity)
# 			name = entity.text
# 			names.append(name)
# 		return names
# 	else:
# 		return "no valid names found"


import spacy 

parser = spacy.load("en_core_web_sm")

parsedEx = parser("My name is Alexander and I'm from Microsoft")
entities = list(parsedEx.ents)


def get_names(_sentence):
	names = []

	parsedEx = parser(_sentence)
	entities = list(parsedEx.ents)

	if len(entities) > 0:
		for entity in entities:
			name = entity.text
			names.append(name)
		return names
	else:
		for token in parsedEx:
			if token.pos_ == "NOUN":
				name = token.text
				names.append(name)
		if len(names) > 0:
			return names
		else:
			return "no valid names found"

# print(get_names("is this John and Sebastian speaking Helen"))
# print(get_names("My name is Helen"))
# print(get_names("is this no name here"))
# print(get_names("This is here"))

