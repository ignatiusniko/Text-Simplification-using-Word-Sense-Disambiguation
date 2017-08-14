import cwi_main
import sssg_main
import sr_main

text = "Dodd simply retained his athletic director position , which he had acquired in 1950 ."
model_CWI = "Model_Simple(LOG).txt"
treshold = 6
CWI_NER = True

SSSG_noWSD = True
metode = "original_lesk"

model_SR = "Model_Simple(LOG).txt"


#CWI
hasil_CWI = []
if CWI_NER :
    hasil_CWI = cwi_main.complexWordIdentificationNER(text, model_CWI, treshold)
else :
    hasil_CWI = cwi_main.complexWordIdentification(text, model_CWI, treshold)

print("CWI ## Hasil ",hasil_CWI)


##SSSG
hasil_SSSG_WSD = []
hasil_SSSG_noWSD = []

for word in hasil_CWI :
    tmp = sssg_main.get_synset(metode, word[0], text)
    tmp = sssg_main.get_word_synonym(tmp)
    # print("SSSG ##",word,"->",tmp)
    hasil_SSSG_WSD.append([tmp,word[1]])
    hasil_SSSG_noWSD.append([sssg_main.get_word_synonym_noWSD(word[0]),word[1]])

print("SSSG ## Hasil WSD",hasil_SSSG_WSD)
print("SSSG ## Hasil noWSD",hasil_SSSG_noWSD)

##SR
hasil_SR_WSD = []
hasil_SR_noWSD = []

for words in hasil_SSSG_WSD :
    tmp = sr_main.wordRanking(model_SR,words[0])
    hasil_SR_WSD.append([tmp[0],words[1]])

for words in hasil_SSSG_noWSD :
    tmp = sr_main.wordRanking(model_SR,words[0])
    hasil_SR_noWSD.append([tmp[0],words[1]])

print("SR ## Hasil WSD",hasil_SR_WSD)
print("SR ## Hasil noWSD",hasil_SR_noWSD)

