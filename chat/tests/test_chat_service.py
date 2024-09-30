import unittest
from chat.chat_service import get_message

class TestChatService(unittest.TestCase):
    def test_get_message(self):
        self.assertEqual(get_message(), "Hello to you from the Chat service! oui oui")

if __name__ == '__main__':
    unittest.main()
