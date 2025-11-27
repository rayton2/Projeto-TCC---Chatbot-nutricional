import unittest
from src.assistente_virtual.assistant import RAGCoreAssistant

class TestRAGCoreAssistant(unittest.TestCase):

    def setUp(self):
        self.assistant = RAGCoreAssistant()

    def test_initialization(self):
        self.assertIsNotNone(self.assistant)

    def test_response_to_query(self):
        query = "Qual é a importância de uma alimentação balanceada?"
        response = self.assistant.get_response(query)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

    def test_handle_invalid_query(self):
        query = ""
        response = self.assistant.get_response(query)
        self.assertEqual(response, "Desculpe, não consegui entender sua pergunta.")

if __name__ == '__main__':
    unittest.main()