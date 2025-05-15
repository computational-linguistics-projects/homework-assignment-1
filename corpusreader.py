"""This file defines the class CorpusReader. It provides an initializer that accepts any directory path name for the corpus it will read.
It has the method sents() that returns the text of the corpus as a list of tokenized sentences, i.e., the corpus becomes a list of lists of tokens."""
#TODO comment everything sentence by sentence and make it not into a jupyter notebook
#%%
import os
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
#TODO take this out after having importe it once
#import nltk
#nltk.download('all')

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
        #creates an empty list which sentences of tokens will be appended to
        listoftokens=[]
        #loops over the files in directory
        for filename in os.listdir(self.directory):
            #if file in directory is a text file
            if filename.endswith('.txt'):
            #opens each file and reads it
                with open(self.directory+'/'+filename) as connection:
                    text=connection.read()
                    #creates list of sentences
                    sentences=sent_tokenize(text,language='english')
                    for sentence in sentences:
                        words=word_tokenize(sentence,language='english')
                        listoftokens.append(words)
                return listoftokens
                    
        


#TODO take this away when we did our tests
corpus = CorpusReader("C:/Users/ritav/OneDrive - Universiteit Utrecht/A computational linguistics/train")
sentences = corpus.sents()  # a list of lists of tokens
#print(sentences)


# %%
