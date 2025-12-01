class Responder:
    def __init__(self, assistant):
        self.assistant = assistant

    def generate_response(self, user_message):
        # Lógica para gerar uma resposta com base na mensagem do usuário
        response = self.assistant.process_message(user_message)
        return response

    def handle_feedback(self, user_feedback):
        # Lógica para lidar com o feedback do usuário
        self.assistant.update_model(user_feedback)