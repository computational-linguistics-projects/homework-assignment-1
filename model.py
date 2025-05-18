""""This file contains the main module of the system. It imports the previous modules and consists of two senctions: 
the regular modeule section and a executable protected test section."""

import re
import random
import corpusreader
import generate


class NgramModel:
    def __init__(self, sentences, n):
        self.n = n
        self.ngrams = {}
        self.vocab = set()
        
        # Preprocess sentences
        processed = []
        for sent in sentences:
            # Remove punctuation-only tokens and lowercase
            clean = [w.lower() for w in sent if not re.fullmatch(r'^\W+$', w)]
            # Add markers
            clean = ['<s>'] * (n-1) + clean + ['</s>']
            processed.append(clean)
            self.vocab.update(clean)
            
        # Build n-gram counts
        for sent in processed:
            for i in range(len(sent)-n+1):
                ngram = tuple(sent[i:i+n])
                if ngram in self.ngrams:
                    self.ngrams[ngram] += 1
                else:
                    self.ngrams[ngram] = 1

    def probability(self, ngram, k=0.0):
        if len(ngram) != self.n:
            return 0.0
        
        prefix = ngram[:-1]
        count = self.ngrams.get(ngram, 0)
        prefix_total = sum(v for kg, v in self.ngrams.items() if kg[:-1] == prefix)
        V = len(self.vocab)
        
        if k == 0:
            return count / prefix_total if prefix_total > 0 else 0.0
        else:
            return (count + k) / (prefix_total + k * V)

    def perplexity(self, sentence, k=1.0):
        # Clean input
        clean = [w.lower() for w in sentence if not re.fullmatch(r'^\W+$', w)]
        clean = ['<s>'] * (self.n-1) + clean + ['</s>']
        
        # Check for unknown words
        for w in clean:
            if w not in self.vocab:
                return float('inf')
        
        # Calculate perplexity
        product = 1.0
        num_ngrams = 0
        for i in range(len(clean)-self.n+1):
            ngram = tuple(clean[i:i+self.n])
            p = self.probability(ngram, k)
            if p <= 0:
                return float('inf')
            product *= p
            num_ngrams += 1
            
        return product ** (-1/num_ngrams) if num_ngrams > 0 else float('inf')

    def choose_successor(self, prefix):
        candidates = []
        weights = []
        target = tuple(prefix)
        for ngram, count in self.ngrams.items():
            if ngram[:-1] == target:
                candidates.append(ngram[-1])
                weights.append(count)
        return random.choices(candidates, weights=weights)[0] if candidates else None
    
