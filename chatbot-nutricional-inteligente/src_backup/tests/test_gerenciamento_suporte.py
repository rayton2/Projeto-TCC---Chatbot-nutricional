import unittest
from src.gerenciamento_suporte.message_handler import MessageManager
from src.gerenciamento_suporte.logger import LogManager

class TestMessageManager(unittest.TestCase):
    def setUp(self):
        self.message_manager = MessageManager()
        self.logger = LogManager()

    def test_send_message(self):
        response = self.message_manager.send_message("Hello")
        self.assertEqual(response, "Message sent: Hello")

    def test_receive_message(self):
        self.message_manager.receive_message("Hi")
        self.assertIn("Hi", self.message_manager.messages)

    def test_log_message(self):
        self.logger.log("Test log message")
        self.assertIn("Test log message", self.logger.logs)

if __name__ == '__main__':
    unittest.main()