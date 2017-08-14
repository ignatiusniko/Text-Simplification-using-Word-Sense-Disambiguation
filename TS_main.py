import cwi_main
import sssg_main
import sr_main
import verb as en

text = "Automatic sense disambiguation using machine readable dictionaries"
model_CWI = "Model_Normal(LOG).txt"
treshold = 7.0
CWI_NER = True

SSSG_WSD = True
metode = "adapted_lesk"

model_SR = "Model_Simple(LOG).txt"

def main(text, model_CWI, treshold, CWI_NER, SSSG_WSD, metode, model_SR) :
    definition = []
    #CWI
    hasil_CWI = []
    if CWI_NER :
        hasil_CWI = cwi_main.complexWordIdentificationNER(text, model_CWI, treshold)
    else :
        hasil_CWI = cwi_main.complexWordIdentification(text, model_CWI, treshold)

    print("CWI ## Hasil ",hasil_CWI)


    ##SSSG
    hasil_SSSG= []
    tenses = []
    if SSSG_WSD :
        for word in hasil_CWI :
            try :
                tenses.append(en.verb_tense(word[0].lower()))
            except :
                tenses.append("")
            tmp = sssg_main.get_synset(metode, word[0], text)
            try :
                print("SSSG ## Definition", word[0], ":", sssg_main.get_word_definition(tmp))
                definition.append(word[0]+ " : "+ sssg_main.get_word_definition(tmp))
            except :
                print("SSSG ## Definition", word[0])

            try :
                tmp = sssg_main.get_word_synonym(tmp)
            except :
                tmp = [word[0]]
            hasil_SSSG.append([tmp,word[1]])

    else :
        for word in hasil_CWI:
            hasil_SSSG.append([sssg_main.get_word_synonym_noWSD(word[0]),word[1]])

    print("SSSG ## Hasil",hasil_SSSG)

    ##SR
    hasil_SR = []

    for words in hasil_SSSG :
        tmp = sr_main.wordRanking(model_SR,words[0])
        print(tmp, words)
        try:
            hasil_SR.append([tmp[0][0],words[1]])
        except :
            continue

    print("SR ## Hasil",hasil_SR)

    ##Hasil
    hasil_text = text.split()
    i = 0
    for word in hasil_SR :
        try:
            hasil_text[word[1]] = en.verb_conjugate(word[0], tense=tenses[i])
        except :
            hasil_text[word[1]] = word[0]
        i+=1

    hasil_text = " ".join(hasil_text)

    #Output
    print("")
    print(text)
    print(hasil_text)
    return hasil_text,definition

# main(text, model_CWI, treshold, CWI_NER, SSSG_WSD, metode, model_SR)