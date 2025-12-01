# filepath: chatbot-nutricional-inteligente/chatbot-nutricional-inteligente/src/core/config.py

class Config:
    DATABASE_URL = "sqlite:///data/corpus.sql"  # URL de conexão com o banco de dados
    EMBEDDING_MODEL = "bert-base-uncased"  # Modelo de embeddings a ser utilizado
    MAX_TOKENS = 512  # Número máximo de tokens para o modelo LLM
    API_KEY = "sua_api_key_aqui"  # Chave da API, se necessário
    DEBUG_MODE = True  # Modo de depuração
    LOGGING_LEVEL = "INFO"  # Nível de log para o sistema

    @staticmethod
    def get_database_url():
        return Config.DATABASE_URL

    @staticmethod
    def get_embedding_model():
        return Config.EMBEDDING_MODEL

    @staticmethod
    def is_debug_mode():
        return Config.DEBUG_MODE

    @staticmethod
    def get_logging_level():
        return Config.LOGGING_LEVEL