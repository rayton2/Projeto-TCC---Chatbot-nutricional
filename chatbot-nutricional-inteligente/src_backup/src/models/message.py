class Message:
    def __init__(self, sender: str, content: str, timestamp: str):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp

    def __repr__(self):
        return f"Message(sender={self.sender}, content={self.content}, timestamp={self.timestamp})"

    def to_dict(self):
        return {
            "sender": self.sender,
            "content": self.content,
            "timestamp": self.timestamp
        }