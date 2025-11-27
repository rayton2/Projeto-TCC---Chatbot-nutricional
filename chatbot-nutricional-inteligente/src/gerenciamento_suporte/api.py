from fastapi import FastAPI
from gerenciamento_suporte.message_handler import MessageManager
from gerenciamento_suporte.logger import LogManager

class ChatbotAPI:
    def __init__(self):
        self.app = FastAPI()
        self.message_manager = MessageManager()
        self.log_manager = LogManager()
        self.setup_routes()

    def setup_routes(self):
        @self.app.post("/message/")
        async def handle_message(message: str):
            self.log_manager.log_message(message)
            response = self.message_manager.process_message(message)
            return {"response": response}

    def run(self, host="0.0.0.0", port=8000):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)

if __name__ == "__main__":
    chatbot_api = ChatbotAPI()
    chatbot_api.run()