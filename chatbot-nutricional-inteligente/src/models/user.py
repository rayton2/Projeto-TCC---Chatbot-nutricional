class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.preferences = {}

    def update_preferences(self, preferences: dict):
        self.preferences.update(preferences)

    def get_user_info(self) -> dict:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "preferences": self.preferences
        }