from os.path import isfile
import pickle
import re
import os

from nltk.tag.stanford import StanfordNERTagger
import nltk

# os.environ['JAVAHOME'] = "C:/Program Files/Java/jdk1.8.0_65/bin"
#
# classifier = './stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
# jar = './stanford-ner/stanford-ner.jar'
#
# st = StanfordNERTagger('stanford-ner\classifiers\english.all.3class.distsim.crf.ser.gz',
#                         'stanford-ner\stanford-ner.jar',
#                         encoding='utf-8')


st = StanfordNERTagger('/media/ignatiusniko/A2C85A12C859E4D7/Users/ignat/PycharmProjects/TS/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        '/media/ignatiusniko/A2C85A12C859E4D7/Users/ignat/PycharmProjects/TS/stanford-ner/stanford-ner.jar',
                        encoding='utf-8')

def loadModel(fileName) :
    fileName="/media/ignatiusniko/A2C85A12C859E4D7/Users/ignat/PycharmProjects/TS/"+fileName
    if isfile(fileName):
        print("CWI ## File Loaded :",fileName)
        f = open(fileName, 'rb')
        s = pickle.load(f)
        f.close()

        return s
    else:
        print("CWI ## File Tidak Ada")
        return 0

def complexWordIdentification(text, model, treshold) :
    model = loadModel(model)

    tmp = []
    i = 0
    for line in text.split(" "):
        try:
            freq = model[line.lower()]
            print(freq)
            # print(line,freq)
            if freq < treshold:
                tmp.append([line,i])
        except:
            j = 0
        i+=1

    return tmp

def complexWordIdentificationNER(text, model, treshold) :
    model = loadModel(model)

    tmp = []
    i = 0
    text = st.tag(text.split())
    for line in text:
        try:
            freq = model[list(line)[0].lower()]
            # print(line,freq)
            if freq < treshold and list(line)[1] == 'O':
                tmp.append([list(line)[0],i])
        except:
            j = 0
        i+=1

    return tmp

# print(complexWordIdentificationNER(""
# "it lies on the southern side of lake constance ."
#                                 "","Model_Simple(LOG).txt",7))