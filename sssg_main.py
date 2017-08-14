from pywsd.lesk import simple_lesk, adapted_lesk, cosine_lesk, original_lesk
from nltk.corpus import wordnet as wn

def get_synset(metode, word, text):
    synset = ""
    if metode == "original_lesk":
        synset = simple_lesk(text, word)
    elif metode == "simple_lesk":
        synset = adapted_lesk(text, word)
    elif metode == "adapted_lesk":
        synset = cosine_lesk(text, word)
    # elif metode == "path" :
    #     synset = max_similarity(text, word, "path")
    # elif metode == "path" :
    #     synset = max_similarity(text, word, "wup")
    # elif metode == "path" :
    #     synset = max_similarity(text, word, "lin")
    # elif metode == "path" :
    #     synset = max_similarity(text, word, "res")
    # elif metode == "random_sense":
    #     synset = random_sense(word)
    # elif metode == "first_sense":
    #     synset = first_sense(word)
    # elif metode == "most_frequent_sense":
    #     synset = most_frequent_sense(word)
    return synset

def get_word_synonym_noWSD(word) :
    tmp = []
    for line in wn.synsets(word) :
        for line2 in line.lemma_names() :
            if line2 not in tmp :
                tmp.append(line2)

    return tmp

def get_word_synonym(synset) :
    return synset.lemma_names()

def get_word_definition(synset) :
    return synset.definition()


# synset = get_synset("adapted_lesk","acquire",
# "dodd simply retained his athletic director position , which he had acquire in 1950 .")
# print(get_word_definition(synset))
# print(get_word_synonym_noWSD("bat"))