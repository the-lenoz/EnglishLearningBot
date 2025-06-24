import json
import os

_messages = None

def load_messages():
    """Load and cache interface texts from messages.json."""
    global _messages
    if _messages is None:
        here = os.path.dirname(__file__)
        path = os.path.join(here, 'messages.json')
        with open(path, 'r', encoding='utf-8') as f:
            _messages = json.load(f)
    return _messages
