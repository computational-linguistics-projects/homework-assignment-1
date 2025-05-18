""""This file contains the main module of the system. It imports the previous modules and consists of two senctions: 
the regular modeule section and a executable protected test section."""


#%%

from corpusreader import CorpusReader
from generate import NgramModel
import random
import re

def generate_sentence(ngram_model=NgramModel):
    sentence = ['<s>']
    newword = ngram_model.choose_successor(sentence)
    word = newword[0]
    if re.search('</s>', word):
        sentence.append('</s>')
        return sentence
    else:
        for _ in range (1,50):       
            sentence.append(word)
       

    
    

#__name__=="__main__"
testcorpus= CorpusReader("C:/Users/ritav/OneDrive - Universiteit Utrecht/A computational linguistics/train")
sentences = testcorpus.sents()  # a list of lists of tokens
test=NgramModel(sentences,2) 
print(generate_sentence(test))
