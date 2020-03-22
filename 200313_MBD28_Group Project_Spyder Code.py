# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:22:53 2020

@author: phil
"""

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 50)
import matplotlib.pyplot as plt

raw=pd.read_csv("C:/Users/phili/OneDrive/Documents/ESCP/MBD28 Machine Learning with Python/Group Project/train2.csv")

positions=6418659
unique=1570365
keywords_non_unique=20496903

subset=raw

keywords_list=[]
for i in list(subset.keywords):
    keywords_list.append(i)

progress=0    
keywords_dict={}
ID_length={}
for i,j in zip(list(subset.ID),keywords_list):
    keywords_dict[i]=j
    ID_length[i]=len(j.split(";"))
    if progress != 100000:
        progress=progress+1
    else:
        print(len(ID_length)/unique*100)
        progress=0

sum([ v for v in ID_length.values() ])

counter=0
progress=0
index_list=[]
for x,c in zip(range(0,len(ID_length.values()),1),ID_length.values()):
        while counter < (c):    
            index_list.append(list(ID_length.keys())[x])
            counter=counter+1
            if progress != 100:
                progress=progress+1
            else:
                status=round(len(index_list)/positions*100,2)
                progress=0
        counter=0 
        print(status)


progress=0    
keywords_lst=[]
for i in keywords_dict.values():
    keywords_lst.append(i.split(";"))
    if progress != 10000:
        progress=progress+1
    else:
        status=round(len(keywords_lst)/unique*100,2)
        print(status)
        progress=0


progress=0
keywords_names=[]
keywords_count=[]
for i in keywords_lst:
    for j in i:
        keywords_names.append(j.split(":")[0])
        try:
            keywords_count.append(j.split(":")[1])
        except:
            keywords_count.append(0)
        if progress != 10000:
            progress=progress+1
        else:
            status=round(len(keywords_names)/keywords_non_unique*100,2)
            print(status)
            progress=0

import nltk 
from nltk.corpus import stopwords

raw_stopword_list_1 = stopwords.words('french')
raw_stopword_list_2 = ["Ap.", "Apr.", "GHz", "MHz", "USD", "a", "afin", "ah", "ai", "aie", "aient", "aies", "ait", "alors", "après", "as", "attendu", "au", "au-delà", "au-devant", "aucun", "aucune", "audit", "auprès", "auquel", "aura", "aurai", "auraient", "aurais", "aurait", "auras", "aurez", "auriez", "aurions", "aurons", "auront", "aussi", "autour", "autre", "autres", "autrui", "aux", "auxdites", "auxdits", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avez", "aviez", "avions", "avons", "ayant", "ayez", "ayons", "b", "bah", "banco", "ben", "bien", "bé", "c", "c'", "c'est", "c'était", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles", "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "celà", "cent", "cents", "cependant", "certain", "certaine", "certaines", "certains", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là", "cf.", "cg", "cgr", "chacun", "chacune", "chaque", "chez", "ci", "cinq", "cinquante", "cinquante-cinq", "cinquante-deux", "cinquante-et-un", "cinquante-huit", "cinquante-neuf", "cinquante-quatre", "cinquante-sept", "cinquante-six", "cinquante-trois", "cl", "cm", "cm²", "comme", "contre", "d", "d'", "d'après", "d'un", "d'une", "dans", "de", "depuis", "derrière", "des", "desdites", "desdits", "desquelles", "desquels", "deux", "devant", "devers", "dg", "différentes", "différents", "divers", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept", "dl", "dm", "donc", "dont", "douze", "du", "dudit", "duquel", "durant", "dès", "déjà", "e", "eh", "elle", "elles", "en", "en-dehors", "encore", "enfin", "entre", "envers", "es", "est", "et", "eu", "eue", "eues", "euh", "eurent", "eus", "eusse", "eussent", "eusses", "eussiez", "eussions", "eut", "eux", "eûmes", "eût", "eûtes", "f", "fait", "fi", "flac", "fors", "furent", "fus", "fusse", "fussent", "fusses", "fussiez", "fussions", "fut", "fûmes", "fût", "fûtes", "g", "gr", "h", "ha", "han", "hein", "hem", "heu", "hg", "hl", "hm", "hm³", "holà", "hop", "hormis", "hors", "huit", "hum", "hé", "i", "ici", "il", "ils", "j", "j'", "j'ai", "j'avais", "j'étais", "jamais", "je", "jusqu'", "jusqu'au", "jusqu'aux", "jusqu'à", "jusque", "k", "kg", "km", "km²", "l", "l'", "l'autre", "l'on", "l'un", "l'une", "la", "laquelle", "le", "lequel", "les", "lesquelles", "lesquels", "leur", "leurs", "lez", "lors", "lorsqu'", "lorsque", "lui", "lès", "m", "m'", "ma", "maint", "mainte", "maintes", "maints", "mais", "malgré", "me", "mes", "mg", "mgr", "mil", "mille", "milliards", "millions", "ml", "mm", "mm²", "moi", "moins", "mon", "moyennant", "mt", "m²", "m³", "même", "mêmes", "n", "n'avait", "n'y", "ne", "neuf", "ni", "non", "nonante", "nonobstant", "nos", "notre", "nous", "nul", "nulle", "nº", "néanmoins", "o", "octante", "oh", "on", "ont", "onze", "or", "ou", "outre", "où", "p", "par", "par-delà", "parbleu", "parce", "parmi", "pas", "passé", "pendant", "personne", "peu", "plus", "plus_d'un", "plus_d'une", "plusieurs", "pour", "pourquoi", "pourtant", "pourvu", "près", "puisqu'", "puisque", "q", "qu", "qu'", "qu'elle", "qu'elles", "qu'il", "qu'ils", "qu'on", "quand", "quant", "quarante", "quarante-cinq", "quarante-deux", "quarante-et-un", "quarante-huit", "quarante-neuf", "quarante-quatre", "quarante-sept", "quarante-six", "quarante-trois", "quatorze", "quatre", "quatre-vingt", "quatre-vingt-cinq", "quatre-vingt-deux", "quatre-vingt-dix", "quatre-vingt-dix-huit", "quatre-vingt-dix-neuf", "quatre-vingt-dix-sept", "quatre-vingt-douze", "quatre-vingt-huit", "quatre-vingt-neuf", "quatre-vingt-onze", "quatre-vingt-quatorze", "quatre-vingt-quatre", "quatre-vingt-quinze", "quatre-vingt-seize", "quatre-vingt-sept", "quatre-vingt-six", "quatre-vingt-treize", "quatre-vingt-trois", "quatre-vingt-un", "quatre-vingt-une", "quatre-vingts", "que", "quel", "quelle", "quelles", "quelqu'", "quelqu'un", "quelqu'une", "quelque", "quelques", "quelques-unes", "quelques-uns", "quels", "qui", "quiconque", "quinze", "quoi", "quoiqu'", "quoique", "r", "revoici", "revoilà", "rien", "s", "s'", "sa", "sans", "sauf", "se", "seize", "selon", "sept", "septante", "sera", "serai", "seraient", "serais", "serait", "seras", "serez", "seriez", "serions", "serons", "seront", "ses", "si", "sinon", "six", "soi", "soient", "sois", "soit", "soixante", "soixante-cinq", "soixante-deux", "soixante-dix", "soixante-dix-huit", "soixante-dix-neuf", "soixante-dix-sept", "soixante-douze", "soixante-et-onze", "soixante-et-un", "soixante-et-une", "soixante-huit", "soixante-neuf", "soixante-quatorze", "soixante-quatre", "soixante-quinze", "soixante-seize", "soixante-sept", "soixante-six", "soixante-treize", "soixante-trois", "sommes", "son", "sont", "sous", "soyez", "soyons", "suis", "suite", "sur", "sus", "t", "t'", "ta", "tacatac", "tandis", "te", "tel", "telle", "telles", "tels", "tes", "toi", "ton", "toujours", "tous", "tout", "toute", "toutefois", "toutes", "treize", "trente", "trente-cinq", "trente-deux", "trente-et-un", "trente-huit", "trente-neuf", "trente-quatre", "trente-sept", "trente-six", "trente-trois", "trois", "très", "tu", "u", "un", "une", "unes", "uns", "v", "vers", "via", "vingt", "vingt-cinq", "vingt-deux", "vingt-huit", "vingt-neuf", "vingt-quatre", "vingt-sept", "vingt-six", "vingt-trois", "vis-à-vis", "voici", "voilà", "vos", "votre", "vous", "w", "x", "y", "z", "zéro", "à", "ç'", "ça", "ès", "étaient", "étais", "était", "étant", "étiez", "étions", "été", "étée", "étées", "étés", "êtes", "être", "ô"]

stopword_list=[]
for word in raw_stopword_list_1:
    stopword_list.append(word)
for word in raw_stopword_list_2:
    stopword_list.append(word)
stopword_list=set(stopword_list)

len(raw_stopword_list_1), len(raw_stopword_list_2), len(stopword_list),

words=[w.lower() for w in keywords_names] 

progress=0
share=[]
filtered_words = [] 
for word in words: 
    if word not in stopword_list and word.isalpha() and len(word) > 1: 
        filtered_words.append(word) 
    filtered_words.sort() 
    if progress != 10000:
        progress=progress+1
    else:
        status=round(len(filtered_words)/keywords_non_unique*100,2)
        share.append(status)
        print(status)
        progress=0    

filtered_words_set=set(filtered_words)
len(words), len(filtered_words), len(filtered_words_set) 

#stemming? -> from nltk.stem.snowball import FrenchStemmer #import the French stemming library

#or even better: only include relevant words through "is in library x"
#possibly also fuzzy logic for word clustering - but how to apply on test-set?

keywords_table=pd.DataFrame(keywords_names,columns=["keywords"])
keywords_table["counts"]=keywords_count
keywords_table.index=index_list

keywords_table
len(keywords_names),len(set(keywords_names))

data=pd.DataFrame(0,columns=filtered_words_set,index=subset.ID)

empty_table=data

pd.DataFrame.to_csv(empty_table,path_or_buf="C:/Users/phili/OneDrive/Documents/ESCP/MBD28 Machine Learning with Python/Group Project/empty_table.csv",sep=",")

"""
next for-loops can be optimized further (without loop maybe...)
"""

for i in index_list:
    for kw,v in zip(list(keywords_table.keywords.loc[i]),list(keywords_table.counts.loc[i])):
        if kw in filtered_words_set:
            data.at[i, kw] = v

###optimization till here!

data["age"]=list(subset.age)
data["sex"]=list(subset.sex)    

new_cols=["age","sex"]
for i in data.columns[0:(len(data.columns)-2)]:
    new_cols.append(i)

data=data[new_cols]
data.head()