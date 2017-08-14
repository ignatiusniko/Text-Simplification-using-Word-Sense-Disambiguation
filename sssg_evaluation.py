import sssg_readDataset
import sssg_main
import pickle
from os.path import isfile, join

from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()

def readDataset(metode) :
    data = sssg_readDataset.readNNSeval2()
    tmp = []
    i = 0
    for line in data :
        synset = sssg_main.get_synset(metode, line[1], line[0])
        try:
            words = sssg_main.get_word_synonym(synset)
        except :
            print(i,"No Synonyms : ",line[1])
            words = [line[1]]
        tmp.append(words)
        i+=1

    return tmp

def readDatasetnoWSD() :
    data = sssg_readDataset.readNNSeval2()
    tmp = []
    for line in data :
        words = sssg_main.get_word_synonym_noWSD(lemma.lemmatize(line[1]))
        tmp.append(words)

    return tmp

def readDataset_file(metode, outputFile) :
    data = sssg_readDataset.readNNSeval2()
    tmp = []
    for line in data :
        synset = sssg_main.get_synset(metode, line[1], line[0])
        # print(synset)
        words = sssg_main.get_word_synonym(synset)
        tmp.append(words)

    with open(outputFile, 'wb') as f:
        pickle.dump(tmp, f)
    if isfile(outputFile):
        print("File", outputFile, "Created")

def readHasil(fileName) :
    if isfile(fileName):
        print("File Loaded")
        f = open(fileName, 'rb')
        s = pickle.load(f)
        f.close()

        return s
    else:
        print("File Tidak Ada")
        return 0

def evaluation(hasil, noWSD) :
    dataset = sssg_readDataset.readNNSeval3()
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for i in range(len(hasil)) :
        for line in hasil[i] :
            if line in dataset[i] :
                tp+=1
            else :
                fp+=1

        for line in noWSD[i] :
            if line not in hasil[i] and line not in dataset[i] :
                tn+=1
            elif line not in hasil[i] :
                fn+=1

    akurasi = (tp + tn + 1) / (tp + tn + fp + fn + 1)
    precision = (tp + 1) / (tp + fp + 1)
    recall = (tp + 1) / (tp + fn + 1)
    f1 = (2 * precision * recall) / (precision + recall)
    g = pow(precision * recall, 1 / 2)
    return round(akurasi, 4), round(precision, 4), round(recall, 4), round(f1, 4), round(g, 4)


# print(readDataset_file("adapted_lesk","hasil_adapted_lesk.txt"))
# print(readHasil("hasil_adapted_lesk.txt"))
print("original_lesk")
print(evaluation(readDataset("original_lesk"), readDatasetnoWSD()))
print("simple_lesk")
print(evaluation(readDataset("simple_lesk"), readDatasetnoWSD()))
print("adapted_lesk")
print(evaluation(readDataset("adapted_lesk"), readDatasetnoWSD()))
print("cosine_lesk")
print(evaluation(readDataset("cosine_lesk"), readDatasetnoWSD()))
print("random_sense")
print(evaluation(readDataset("random_sense"), readDatasetnoWSD()))
print("first_sense")
print(evaluation(readDataset("first_sense"), readDatasetnoWSD()))
print("most_frequent_sense")
print(evaluation(readDataset("most_frequent_sense"), readDatasetnoWSD()))
print("path")
print(evaluation(readDataset("path"), readDatasetnoWSD()))