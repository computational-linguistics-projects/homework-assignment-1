import os
from nltk.tokenize import sent_tokenize, word_tokenize

class CorpusReader:
    def __init__(self, directory):
        self.directory = directory

    def sents(self):
        listoftokens = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.txt'):
                filepath = os.path.join(self.directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                    sentences = sent_tokenize(text)
                    for sent in sentences:
                        words = word_tokenize(sent)
                        listoftokens.append(words)
        return listoftokens
    
    # Import the CorpusReader class
reader = CorpusReader("C:/Users/Adrian/OneDrive/Desktop/comput ling/small-corpus")
sentences = reader.sents()

print(sentences)
    
                    
