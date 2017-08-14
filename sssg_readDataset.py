def readNNSeval() :
    text = open("NNSeval.txt").read()
    textar = []
    for line in text.split("\n") :
        line = line.split("\t")
        tmp = []
        tmp.append(line[0])
        tmp.append(line[1:3])
        textar.append(tmp)
    return textar

def readNNSeval2() :
    text = open("NNSeval.txt").read()
    textar = []
    for line in text.split("\n") :
        line = line.split("\t")
        tmp = []
        tmp.append(line[0])
        tmp.append(line[1])
        textar.append(tmp)
    return textar

def readNNSeval3():
    from nltk.stem import WordNetLemmatizer
    lemma = WordNetLemmatizer()

    text = open("NNSeval.txt").read()
    textar = []
    for line in text.split("\n"):
        line = line.split("\t")
        tmp = []
        hasil = line[3:]
        for line in hasil :
            tmp.append(lemma.lemmatize(line.split(":")[1]))
        textar.append(tmp)
    return textar

# print(readNNSeval3())