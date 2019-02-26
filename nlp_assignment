import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from collections import Counter

with open("test.txt","r") as file:
    data_file=file.read()

#print(data_file)

data_file_sentences = sent_tokenize(data_file)
#print(data_file_sentences)
#print(len(data_file_sentences))

data_file_single_sentence=[]

for line in data_file_sentences:
    processed_line = line
    data_file_single_sentence.append(word_tokenize(processed_line))

#print(data_file_single_sentence)

postaggedlines=[]
l=len(data_file_single_sentence)

for i in range(0,l-1):
    postaggedlines.append(nltk.pos_tag(data_file_single_sentence[i]))   

#print(postaggedlines) 
#print(postaggedlines[1][1][1])
#le=len(postaggedlines[])

parts_of_speech={
    'NN':[],
    'NNS':[],
    'NNP':[],
    'NNPS':[]
}

all_tuples=()
count=0
#print(parts_of_speech)

for i in range(0,l-1):
    for j in range(0,len(postaggedlines[i])-1):
        tuples= tuple(postaggedlines[i][j])
        if tuples[1] == 'NN':
            parts_of_speech['NN'].append(tuples[0])
        elif tuples[1] == 'NNS':
            parts_of_speech['NNS'].append(tuples[0])
        elif tuples[1] == 'NNP':
            parts_of_speech['NNP'].append(tuples[0])
        elif tuples[1] == 'NNPS':
            parts_of_speech['NNPS'].append(tuples[0])
        else:
            pass
#print(all_tuples)

#print(parts_of_speech)

all_list=[]

for values in parts_of_speech.values():
    #print(values)
    all_list = all_list + values

#print(all_list)
print(Counter(all_list).most_common(5))




'''
z=sent_tokenize(x)
print(len(z))
y=[]
count=0

for i in range(0,21):
    #print(word_tokenize(z[i]))
    y = y + nltk.pos_tag(word_tokenize(z[i]))

print(y)
#print(y[0])
for item in y:
    for item2 in item:
        print(item2)
        if 'NN' in item2[1]:
            print(item2[0] + '\t' + item2[1])
            count=count+1
        

print(count)
'''






