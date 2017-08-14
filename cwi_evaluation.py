import re
import os
import cwi_main
import cwi_readDataset
import cwi_makeModel
from nltk.tag.stanford import StanfordNERTagger
import nltk

os.environ['JAVAHOME'] = "C:/Program Files/Java/jdk1.8.0_65/bin"

classifier = './stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
jar = './stanford-ner/stanford-ner.jar'

st = StanfordNERTagger('stanford-ner\classifiers\english.all.3class.distsim.crf.ser.gz',
                        'stanford-ner\stanford-ner.jar',
                        encoding='utf-8')
st = StanfordNERTagger(classifier, jar)

def evaluation(fileName) :
    model = cwi_main.loadModel(fileName)
    dataset = cwi_readDataset.readNNSeval2()

    eval = []
    for line in dataset :
        try:
            eval.append([line[0],model[line[0]],line[1]])
        except :
            eval.append([line[0], 0, line[1]])

    t = 0
    while(t <= 13):
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        max = 0
        for line in eval :
            if line[1] < t : #Complex
                if line[2] == '1' :
                    tp+=1
                else:
                    fp+=1
            else:
                if line[2] == '0' :
                    tn+=1
                else:
                    fn+=1
        t+=0.01

        akurasi = (tp+tn+1)/(tp+tn+fp+fn+1)
        precision = (tp+1)/(tp+fp+1)
        recall = (tp+1)/(tp+fn+1)
        f1 = (2*precision*recall)/(precision+recall)
        g = pow(precision*recall,1/2)
        print(round(t,4), round(akurasi,4), round(precision,4), round(recall,4), round(f1,4),round(g,4))
        # print(round(t, 8), round(akurasi, 8), round(f1, 8))

def evaluationNER(fileName) :
    model = cwi_main.loadModel(fileName)
    dataset =  cwi_makeModel.loadDatasetNER("Dataset_NER.txt")

    eval = []
    for line in dataset :
        try :
            eval.append([line[0],model[line[0].lower()],line[1],line[2]])
        except :
            eval.append([line[0], 0, line[1], line[2]])

    t = 0
    while(t <= 13):
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for line in eval :
            if line[1] < t and line[3] == 'O': #Complex
                if line[2] == '1' :
                    tp+=1
                else:
                    fp+=1
            else:
                if line[2] == '0' :
                    tn+=1
                else:
                    fn+=1
        t+=0.01

        akurasi = (tp+tn+1)/(tp+tn+fp+fn+1)
        precision = (tp+1)/(tp+fp+1)
        recall = (tp+1)/(tp+fn+1)
        f1 = (2*precision*recall)/(precision+recall)
        g = pow(precision*recall,1/2)
        print(round(t,4), round(akurasi,4), round(precision,4), round(recall,4), round(f1,4),round(g,4))
        # print(round(t, 8), round(akurasi, 8), round(f1, 8))

def test(fileName, inputText) :
    treshold = 7.42

    model = cwi_main.loadModel(fileName)
    model2 = cwi_main.loadModel("Model_Simple.txt")
    text = re.sub(r'[^a-z]+',' ',inputText.lower()).split()
    # text = nltk.word_tokenize(inputText)
    # text = st.tag(text)
    for line in text :
        try :
            freq = model[line[0].lower()]
            freq = model[line.lower()]*len(line)/model2[line.lower()]
            if freq < treshold :
                print(line, '->', freq,"-> Complex")
            else:
                print(line,'->',freq)
        except :
            print(line, '->', 0)


evaluationNER("Model_Normal+Simple(LOG).txt")
# test("Model_Normal.txt",
# "abundance	18	1:amount	2:plenty	3:wealth	3:large amount	4:excess	4:plenitude	5:profusion	5:outpouring	5:a lot	5:portion	5:great amount	5:heap	5:availability	5:quantity"
# )