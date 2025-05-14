"""This file defines the class CorpusReader. It provides an initializer that accepts any directory path name for the corpus it will read.
It has the method sents() that returns the text of the corpus as a list of tokenized sentences, i.e., the corpus becomes a list of lists of tokens."""

#%%

import os
import nltk
import re

#Defining the class CorupusReader
class CorpusReader:

    def __init__(self,directory):
        """
        Initialize a CorpusReader object. This function stores the path to 
        the corpus directory.
        """
        self.directory=directory
        
        
    def sents(self):
        """Read the contents of a directory of files, and return the results as
        either a list of lines or a list of words.
        """   
        #loops over the files in directory
        for filename in os.listdir(self.directory):
            #if file in directory is a text file
            if filename[-4:]==r"\.txt":
            #opens each file and reads it
                with open(self.directory+'/'+filename) as connection:
                    text=connection.readlines()
                    #creates list of sentences
                    sentences=nltk.tokenize.sent_tokenize(text,language='english')
                    #creates list of lists words
                    words=nltk.tokenize.word_tokenize(sentences,language='english')
                    return text
                    
        



corpus = CorpusReader("path")
sentences = corpus.sents()  # a list of lists of tokens
print(sentences)


# %%
