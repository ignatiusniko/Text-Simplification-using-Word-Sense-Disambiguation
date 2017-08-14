import sr_main
import sr_readDataset

def cleanArray(arr) :
    tmp = []
    for line in arr :
        tmp.append(line[1])
    return tmp

def rankArray(arr) :
    tmp = []
    tmp2 = []
    tmp3 = '0'
    for line in arr :
        if tmp3 != line[0] :
            tmp.append(tmp2)
            tmp3 = line[0]
            tmp2 = []
            tmp2.append(line[1])
        else:
            tmp2.append(line[1])
    tmp.append(tmp2)
    return tmp[1:]

def getRankN(arr, n) :
    tmp = []
    for line in arr[:n] :
        for line2 in line :
            tmp.append(line2)
    return tmp

def evaluationTRank(fileName,n) :
    model = sr_main.loadModel(fileName)
    dataset = sr_readDataset.readNNSeval2()

    i = 0
    for line in dataset:
        hasil = sr_main.wordRanking(model,cleanArray(line))
        data = rankArray(line)
        if hasil[0] in getRankN(data, n) :
            i+=1
    return i/len(dataset)

for i in range(1,6) :
    print(round(evaluationTRank("Model_Simple(LOG).txt", i),3))
