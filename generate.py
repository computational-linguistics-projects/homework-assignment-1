""""This file contains the main module of the system. It imports the previous modules and consists of two senctions: 
the regular modeule section and a executable protected test section.
Since our version of choose succesor does not yet include weights, we had to choose a way to end the sentences 
non-probabilistically, as otherwise the loop would take too long to finish or be infinite. This way the rest of
the code can still run even tough it is not behaving fully as desired.
authors: Rita Ruano, Adrian Wojcik, Marilea Canul"""

#Importing necessary modules and methods from said modules 
from corpusreader import CorpusReader
from model import NgramModel
import re
from nltk import word_tokenize
import random

def generate_sentence(ngram_model):
    """This function takes a Ngrammodel created by the class NgramModels and creates sentences
    based on its class function choose_successor. It therefore takes the corpus associated with
    the instantiated model into account."""
    #Initiates a sentence with a start symbol 
    sentence = ['<s>']
    #Initiates the counter that will stop the loop
    counter=0
    #Creates a list of numbers to choose a lenght from untill 20
    listofnumbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #Randomly selects a lenght from the list, as it returns a list, it selects an indexed item to use it as an integer later
    sentencelength=random.choices(listofnumbers)[0]
    #Uses the lenght to repeat the loop a 'random amount of times'
    while counter<=sentencelength:
        #Uses the choose successor function to select a possible successor for the sentence, with bigram occurences in mind
        newword = ngram_model.choose_successor(sentence)
        word = newword[-1]     
        #Appends the word to the list
        sentence.append(word)
        #Adds one to the counter to eventually stop the loop
        counter+=1
    #After the loop is done, ends the sentence appending an end symbol  
    sentence.append('</s>') 
    return sentence

      

if __name__=="__main__":
    #1
    corpus= CorpusReader("./train")
    sentences = corpus.sents() 
    model1=NgramModel(sentences,2) 

    #2
    #generates a sentence, takes out the start and end symbols, apends a periodt,
    # joins them into a string and capitalizes them. Prints them with a new line
    sentence1=generate_sentence(model1)
    sentence1=sentence1[1:-1]
    sentence1.append('.')
    sentence2=generate_sentence(model1)
    sentence2=sentence2[1:-1]
    sentence2.append('.')
    string1=(' '.join(sentence1)).capitalize()
    string2=(' '.join(sentence2)).capitalize()
    print(f'{string1}\n{string2}')
    
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

    print(f'The perplexity of sentence: {sent1}, is {model1.perplexity(sent1_t)}.\n'
        f'The perplexity of sentence: {sent2}, is {model1.perplexity(sent2_t)}.\n'
        f'The perplexity of sentence: {sent3}, is {model1.perplexity(sent3_t)}.\n'
        f'The perplexity of sentence: {sent4}, is {model1.perplexity(sent4_t)}.\n'
        f'The perplexity of sentence: {sent5}, is {model1.perplexity(sent5_t)}.\n')
 

