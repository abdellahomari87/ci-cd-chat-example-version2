from Chat.chat_service import get_message

def test_get_message():
    assert get_message() == "Hello to you from the Chat service! oui oui"
