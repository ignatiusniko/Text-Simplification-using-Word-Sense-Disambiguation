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
        i = 0
        for line2 in line[0].split() :
            if i == int(line[2]) :
                textar.append([line2,'1'])
            else :
                textar.append([line2, '0'])
            i+=1
    return textar



# print(readNNSeval())