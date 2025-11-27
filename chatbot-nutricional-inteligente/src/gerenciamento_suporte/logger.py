class LogManager:
    def __init__(self, log_file='chatbot.log'):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, 'a') as file:
            file.write(f"{self._get_timestamp()} - {message}\n")

    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")