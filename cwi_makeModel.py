import operator
import codecs
import re
from collections import Counter
import math
import pickle
from os.path import isfile, join
from nltk.corpus import stopwords
import cwi_readDataset
from nltk.tag.stanford import StanfordNERTagger
import nltk
import os


stop = set(stopwords.words('english'))

os.environ['JAVAHOME'] = "C:/Program Files/Java/jdk1.8.0_65/bin"

classifier = './stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
jar = './stanford-ner/stanford-ner.jar'

st = StanfordNERTagger('stanford-ner\classifiers\english.all.3class.distsim.crf.ser.gz',
                        'stanford-ner\stanford-ner.jar',
                        encoding='utf-8')
st = StanfordNERTagger(classifier, jar)


data = []

def spasi(number):
    return " " * number

def output(dict):
    for (word, value) in dict:
        data.append([word,value])
        if len(word) < 30:
            print(word + spasi(30 - len(word)) + ": " + str(value))
        else:
            print(word + ": " + str(value))

def create_Model(inputFile, outputFile, log=False) :
    fd = codecs.open(inputFile, 'r', 'utf-8')
    text = fd.read()
    fd.close()

    all_words = re.findall(r'[a-z]+', text.lower())

    words = [w for w in all_words if w not in stop]

    # Counter
    word_count = Counter(words)
    total_words = len(words)

    indices = {}
    for w in word_count:
        if log :
            indices[w] = math.log(word_count[w] / total_words)
        else:
            indices[w] = word_count[w] / total_words

    sorted_indices = sorted(indices.items(), key=operator.itemgetter(1), reverse=True)

    data = dict(sorted_indices)
    with open(outputFile, 'wb') as f:
        pickle.dump(data, f)
    if isfile(outputFile):
        print("File ",outputFile," Created")

    return sorted_indices

def bigrams(input_list):
  bigram_list = []
  j = len(input_list)-1
  for i in range(len(input_list)-1):
      bigram_list.append(input_list[i]+" "+input_list[i+1])
      print(i,"->",j)
  return bigram_list


def create_ModelBigram(inputFile, outputFile, log=False) :
    fd = codecs.open(inputFile, 'r', 'utf-8')
    text = fd.read()
    fd.close()

    all_words = re.findall(r'[a-z]+', text.lower())

    # words = [w for w in all_words if w not in stop]

    words = bigrams(all_words)

    # Counter
    word_count = Counter(words)
    print(word_count)

    indices = {}
    for w in word_count:
        if log :
            indices[w] = math.log(word_count[w])
        else:
            indices[w] = word_count[w]

    # sorted_indices = sorted(indices.items(), key=operator.itemgetter(1), reverse=True)

    # data = dict(indices)
    with open(outputFile, 'wb') as f:
        pickle.dump(data, f)
    if isfile(outputFile):
        print("File ",outputFile," Created")

    return indices

def datasetNER(outputFile) :
    dataset = cwi_readDataset.readNNSeval()

    eval = []
    for line in dataset :
        print(line)
        text = line[0]
        text = st.tag(text.split())
        i = 0
        for line2 in text :
            line2 = list(line2)
            line2[0] = line2[0].lower()
            if re.sub(r'[^a-z]','',line2[0]) :
                if i == int(line[1][1]) :
                    eval.append([line2[0],'1',line2[1]])
                else:
                    eval.append([line2[0],'0', line2[1]])
            i+=1

    with open(outputFile, 'wb') as f:
        pickle.dump(eval, f)
    if isfile(outputFile):
        print("File ", outputFile, " Created")

def loadDatasetNER(fileName) :
    if isfile(fileName):
        print("File Loaded")
        f = open(fileName, 'rb')
        s = pickle.load(f)
        f.close()

        return s
    else:
        print("File Tidak Ada")
        return 0

def loadModel(fileName) :
    if isfile(fileName):
        print("File Loaded")
        f = open(fileName, 'rb')
        s = pickle.load(f)
        f.close()

        return s
    else:
        print("File Tidak Ada")
        return 0

create_ModelBigram("normal.txt",'bigram_normal.txt',log=True)
# for k,v in loadModel("bigram_simple.txt").items() :
#     if v > 4 :
#         print(k,v)
# print(loadModel("bigram_simple.0txt")["even out"])