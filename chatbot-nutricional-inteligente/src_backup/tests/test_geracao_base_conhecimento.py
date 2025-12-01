import unittest
from src.geracao_base_conhecimento.generator import CorpusManager

class TestCorpusManager(unittest.TestCase):

    def setUp(self):
        self.corpus_manager = CorpusManager()

    def test_load_corpus(self):
        # Test if the corpus loads correctly
        corpus = self.corpus_manager.load_corpus('data/corpus.sql')
        self.assertIsNotNone(corpus)
        self.assertGreater(len(corpus), 0)

    def test_clean_corpus(self):
        # Test if the corpus cleaning function works
        raw_corpus = ["This is a sample text.", "Another sample text!"]
        cleaned_corpus = self.corpus_manager.clean_corpus(raw_corpus)
        self.assertEqual(len(cleaned_corpus), 2)

    def test_segment_corpus(self):
        # Test if the corpus segmentation works
        cleaned_corpus = ["This is a sample text.", "Another sample text!"]
        segments = self.corpus_manager.segment_corpus(cleaned_corpus)
        self.assertGreater(len(segments), 0)

    def test_generate_embeddings(self):
        # Test if embeddings are generated correctly
        segments = ["This is a sample text.", "Another sample text!"]
        embeddings = self.corpus_manager.generate_embeddings(segments)
        self.assertIsNotNone(embeddings)
        self.assertEqual(len(embeddings), len(segments))

if __name__ == '__main__':
    unittest.main()