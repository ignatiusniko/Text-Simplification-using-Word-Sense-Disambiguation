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
        for line2 in line[3:] :
            tmp.append(line2.split(":"))
        textar.append(tmp)
    return textar

# print(readNNSeval2())