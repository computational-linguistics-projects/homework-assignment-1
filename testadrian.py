import unittest
from corpusreader import CorpusReader
from model import NgramModel
from generate import generate_sentence

class TestCorpusReader(unittest.TestCase):
    
    def test_sents(self):
        # Create a sample directory and file
        import os
        sample_dir = 'test_corpus'
        os.makedirs(sample_dir, exist_ok=True)
        with open(os.path.join(sample_dir, 'sample.txt'), 'w', encoding='utf-8') as f:
            f.write("Hello world. This is a test.")
        
        # Test CorpusReader
        reader = CorpusReader(sample_dir)
        sentences = reader.sents()
        
        # Expected output
        expected = [['Hello', 'world', '.'], ['This', 'is', 'a', 'test', '.']]
        
        # Assertions
        self.assertEqual(sentences, expected)
        
        # Clean up
        os.remove(os.path.join(sample_dir, 'sample.txt'))
        os.rmdir(sample_dir)


class TestNgramModel(unittest.TestCase):
    
    def setUp(self):
        # Example corpus
        self.sentences = [
            ["hello", "world", "."],
            ["hello", "there", "world", "."],
            ["world", "of", "words", "."]
        ]
        self.model = NgramModel(self.sentences, 2)

    def test_probability(self):
        self.assertGreater(self.model.probability(('hello', 'world')), 0)
        self.assertEqual(self.model.probability(('world', 'nonexistent')), 0)

    def test_perplexity(self):
        sentence = ["hello", "world"]
        pp = self.model.perplexity(sentence)
        self.assertGreater(pp, 0)

    def test_choose_successor(self):
        prefix = ['hello']
        successor = self.model.choose_successor(prefix)
        self.assertIn(successor, ['world', 'there'])


class TestGenerateSentence(unittest.TestCase):

    def setUp(self):
        # Example corpus
        self.sentences = [
            ["this", "is", "a", "test", "."],
            ["test", "the", "ngram", "model", "."],
            ["ngram", "models", "are", "fun", "."]
        ]
        self.model = NgramModel(self.sentences, 2)

    def test_generate_sentence(self):
        generated = generate_sentence(self.model)
        self.assertIsInstance(generated, str)
        self.assertGreater(len(generated), 0)
        print(f"Generated Sentence: {generated}")


if __name__ == '__main__':
    unittest.main()
