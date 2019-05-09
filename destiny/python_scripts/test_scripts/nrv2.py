import spacy 
parser = spacy.load('en_core_web_sm')

example="The is ticking and Robin is churping while Yu-Hsiu is talking with Ricard and John is in class with priya"

#Code "borrowed" from somewhere?!
def entities(example):
    # if show: print(example)
    parsedEx = parser(example)
 
    print("-------------- entities only ---------------")
    # if you just want the entities and nothing else, you can do access the parsed examples "ents" property like this:
    ents = list(parsedEx.ents)
    # tags={}
    # for entity in ents:
    #     #print(entity.label, entity.label_, ' '.join(t.orth_ for t in entity))
    #     term=' '.join(t.orth_ for t in entity)
    #     if ' '.join(term) not in tags:
    #         tags[term]=[(entity.label, entity.label_)]
    #     else:
    #         tags[term].append((entity.label, entity.label_))
    # print(tags)
    print(ents)

entities(example)