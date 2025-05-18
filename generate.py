""""This file contains the main module of the system. It imports the previous modules and consists of two senctions: 
the regular modeule section and a executable protected test section."""

#%%

from corpusreader import CorpusReader
from model import NgramModel
import random
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# def generate_sentence(ngram_model=NgramModel):
#     sentence = ['<s>']
#     newword = ngram_model.choose_successor(sentence)
#     word = newword[0]
#     while word != '</s>':
#         sentence.append(word)

#     return sentence

def test (text): 
    tokenized_words = []
    for sentence in text: 
        sentences=sent_tokenize(sentence,language='english')
        tokenized_words.append(sentences)
    return tokenized_words

print(test("Suggestive, Watson, is it not?"))
          
# Suggestive, Watson, is it not?
# It is amazing that a family can be torn apart by something as simple as a pack of wild dogs!
# So spoke Sherlock Holmes and turned back to the great scrapbook in which he was arranging and indexing some of his recent material.
# What I like best about my friends is that they are few.
# Friends what is like are they about I best few my that.


        
        # if re.search('</s>', word):
        #     sentence.append('</s>')
        #     return sentence
        # else:
        #     for _ in range (1,50):       
        #         sentence.append(word)
       
    


#__name__=="__main__"
# testcorpus= CorpusReader("C:/Users/maril/Downloads/train/train")
# sentences = testcorpus.sents()  # a list of lists of tokens
# test=NgramModel(sentences,2) 
# print(generate_sentence(test))