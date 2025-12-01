class EmbeddingsManager:
    def __init__(self):
        self.embeddings = {}

    def generate_embedding(self, text):
        # Implementar a lógica para gerar um embedding a partir do texto
        pass

    def save_embedding(self, key, embedding):
        self.embeddings[key] = embedding

    def get_embedding(self, key):
        return self.embeddings.get(key)

    def clear_embeddings(self):
        self.embeddings.clear()