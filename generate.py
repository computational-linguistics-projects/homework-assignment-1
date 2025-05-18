""""This file contains the main module of the system. It imports the previous modules and consists of two senctions: 
the regular modeule section and a executable protected test section.
authors: Rita Ruano, Adrian Wojcik, Marilea Canul"""

#%%

from corpusreader import CorpusReader
from model import NgramModel
import re
from nltk import word_tokenize

def generate_sentence(ngram_model=NgramModel):
    sentence = []
    newword = ngram_model.choose_successor(sentence)
    word = newword[0]
    while re.search('</s>', word)==False:
        for _ in range (1,50):    
            sentence.append(word)
    else:
        sentence.append('</s>')
        return sentence
       
    

if __name__=="__main__":
    #1
    corpus= CorpusReader("C:/Users/ritav/OneDrive - Universiteit Utrecht/A computational linguistics/train")
    sentences = corpus.sents() 
    model1=NgramModel(sentences,2) 
    #2
    space=' '
    sentence1=generate_sentence(model1)
    sentence1=sentence1[1:-1]
    sentence1.append('.')
    sentence2=generate_sentence(model1)
    sentence2=sentence2[1:-1]
    sentence2.append('.')
    (space.join(sentence1)).capitalize()
    (space.join(sentence2)).capitalize()
    print(sentence1,'\n',sentence2)
    #3
    sent1='Suggestive, Watson, is it not?'
    sent2='It is amazing that a family can be torn apart by something as simple as a pack of wild dogs!'
    sent3='So spoke Sherlock Holmes and turned back to the great scrapbook in which he was arranging and indexing some of his recent material.'
    sent4='What I like best about my friends is that they are few.'
    sent5='Friends what is like are they about I best few my that.'

    sent1_t=word_tokenize(sent1)
    sent2_t=word_tokenize(sent2)
    sent3_t=word_tokenize(sent3)
    sent4_t=word_tokenize(sent4)
    sent5_t=word_tokenize(sent5)

    print(f'The perplexity of sentence:{sent1}, is {model1.perplexity(sent1_t)}.\n'
        f'The perplexity of sentence:{sent2}, is {model1.perplexity(sent2_t)}.\n'
        f'The perplexity of sentence:{sent3}, is {model1.perplexity(sent3_t)}.\n'
        f'The perplexity of sentence:{sent4}, is {model1.perplexity(sent4_t)}.\n'
        f'The perplexity of sentence:{sent5}, is {model1.perplexity(sent5_t)}.\n')
 
