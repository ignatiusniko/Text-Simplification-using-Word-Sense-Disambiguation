from os.path import isfile
import pickle

def loadModel(fileName) :
    if isfile(fileName):
        print("SR ## File Loaded",fileName)
        f = open(fileName, 'rb')
        s = pickle.load(f)
        f.close()

        return s
    else:
        print("SR ## File Tidak Ada")
        return 0

def getKey(item):
    return item[1]


def wordRanking(model, arr) :
    model = loadModel(model)

    tmp = []
    for line in arr:
        try:
            freq = model[line.lower()]
            tmp.append([line,round(freq,3)])
        except:
            tmp.append([line, 0])
    tmp = sorted(tmp, key=getKey, reverse=True)
    return tmp

# print(wordRanking(model,['owner','holder','buyer','master','teacher']))


