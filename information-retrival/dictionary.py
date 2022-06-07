import json
import math
import ast
import  manipulate as manipulate

filecount = 1461
# imppppppppportant you should change file couunt
dictionary = dict()
def Build():
    global dictionary
    Docdictionary = dict()

    for i in range(1, filecount):
        print("Building ",i)
        doc = open('./corpus/'+i.__str__()+'.txt', 'r').read()
        doc=manipulate.ManipulatingText(doc,False)
        # //print(doc)
        Docdictionary[i]={'length':len(doc)}
        doc=WordsFrequent(doc,i)
        for word in doc.keys():
            if dictionary.get(word):
                dictionary.get(word).get('files').append({'file': i, 'repetition': doc[word].get('value')})
                dictionary.get(word).update({
                        'value': dictionary[word].get('value') + doc[word].get('value'),
                        'files': dictionary[word].get('files')
                    })
            else:
                dictionary[word] = {'value': doc[word].get('value'), 'files': [{'file': i, 'repetition': doc[word].get('value')}]}
                # dictionary[word] = {'value': doc[word].get('value'), 'files': [i] }
    dictionary=Idf(dictionary)
    js = json.dumps(dictionary)
    f = open("C:\\Users\\Wissam\\Desktop\\project\\generalDict.json", "w")
    f1 = open("C:\\Users\\Wissam\\Desktop\\project\\files length.json", "w")
    f.write(js)
    f.close()
    js = json.dumps(Docdictionary)
    f1.write(js)
    f1.close()

def WordsFrequent(WordsArray,fileNumber):
    dic=dict()
    for word in WordsArray:
        if dic.get(word):
            dic[word]={'value':1+dic[word].get('value'),'file':fileNumber}
        else:dic[word] = {'value': 1}
    return dic

def Idf(Dic):
    for word in Dic.keys():
        Dic.get(word).update({
            'value': Dic[word].get('value'),
            'files': Dic[word].get('files'),
            'idf': 1.0 + math.log10(filecount/float(len(Dic[word].get('files')))),
        })
    return Dic

def Load():
    file = open('C:\\Users\\Wissam\\Desktop\\project\\generalDict.json', "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    return dictionary



