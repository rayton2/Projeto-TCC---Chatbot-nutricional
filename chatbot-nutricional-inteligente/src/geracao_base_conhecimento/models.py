class KnowledgeBaseModel:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

    def __repr__(self):
        return f"KnowledgeBaseModel(id={self.id}, title='{self.title}')"


class UserModel:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username

    def __repr__(self):
        return f"UserModel(user_id={self.user_id}, username='{self.username}')"


class MessageModel:
    def __init__(self, message_id: int, user_id: int, content: str):
        self.message_id = message_id
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return f"MessageModel(message_id={self.message_id}, user_id={self.user_id})"