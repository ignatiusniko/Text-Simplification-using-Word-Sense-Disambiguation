# from os.path import isfile
# import pickle
#
# def loadModel(fileName) :
#     if isfile(fileName):
#         # print("File Loaded")
#         f = open(fileName, 'rb')
#         s = pickle.load(f)
#         f.close()
#
#         return s
#     else:
#         print("File Tidak Ada")
#         return 0
#
# def getKey(item):
#     return item[1]
#
# model2 = loadModel("Model_Normal.txt")
#
# def wordRanking(model, arr) :
#     tmp = []
#     for line in arr:
#         try:
#             freq = model[line.lower()]
#             tmp.append([line,round(freq,1)])
#         except:
#             tmp.append([line, 0])
#     print(tmp)
#     tmp = sorted(tmp, key=getKey, reverse=True)
#     print(tmp)
#     tmp2 = []
#     for line in tmp :
#         tmp2.append(line[0])
#     return tmp2
#
# def wordRanking2(model, arr) :
#     tmp = []
#     for line in arr:
#         try:
#             freq = model[line.lower()]
#             tmp.append([line,freq])
#         except:
#             tmp.append([line, 0])
#     tmp = sorted(tmp, key=getKey, reverse=True)
#     return tmp
#
# model = loadModel("Model_Simple(LOG).txt")
#
# print(wordRanking(model,["amazing","incredible","great","impressive","awesome","interesting","real","huge","noteworthy","exceptional","notably","beautiful","wonderful","significant","super"]))
#
#
#

from nltk.corpus import wordnet as wn

text = []
for line in wn.synsets('assume') :
    # text.append(line)
    print(line, line.lemma_names())
        # print(line2)
print(text)