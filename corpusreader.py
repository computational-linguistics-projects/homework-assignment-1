
<<<<<<< Updated upstream
=======
#Importing necessary modules and methods from said modules 
import os
from nltk import(all) 

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

#Defining the class CorupusReader
class CorpusReader:
    #Initializing 
    def __init__(self,directory):
        """
        Initializes a CorpusReader object.
        Takes the directory path name of the corpus that will be read."""
        self.directory=directory
          
          
    def sents(self):
        """ Reads the contents of a directory of files.
            returns: list of sentences which are themselves lists of their words"""   
        #Creates an empty list to which the list sentences will be appended to
        listoftokens=[]
        #Loops over the files in the given directory
        for filename in os.listdir(self.directory):
            #Considers only the text files in the corpus directory
            if filename.endswith('.txt'):
            #Opens each file and reads it
                with open(self.directory+'/'+filename) as connection:
                    text=connection.read()
                    #Creates a list of sentences
                    sentences=sent_tokenize(text,language='english')
                    #Loops over each sentence in the list
                    for sentence in sentences:
                        #Creates a list of words per sentence
                        words=word_tokenize(sentence,language='english')
                        #Appends each word to the final list, within it's respective sentence
                        listoftokens.append(words)
                #Returns the final list
                return listoftokens
                    
>>>>>>> Stashed changes
