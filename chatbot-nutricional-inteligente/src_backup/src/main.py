# filepath: chatbot-nutricional-inteligente/chatbot-nutricional-inteligente/src/main.py

from core.config import Config
from geracao_base_conhecimento.generator import CorpusManager
from assistente_virtual.assistant import RAGCoreAssistant
from gerenciamento_suporte.api import create_api

try:
    from assistente_virtual.nlu import NLUAdapter
except Exception:
    NLUAdapter = None

try:
    # pode ser RAGOrchestrator ou RAGCoreAssistant dependendo da implementação
    from assistente_virtual.assistant import RAGOrchestrator as Orchestrator
except Exception:
    try:
        from assistente_virtual.assistant import RAGCoreAssistant as Orchestrator
    except Exception:
        Orchestrator = None

try:
    from gerenciamento_suporte.api import create_api
except Exception:
    create_api = None

try:
    from gerenciamento_suporte.logger import AuditLogger
except Exception:
    AuditLogger = None

def main():
    # Configuração inicial
    config = Config()
    
    # Carregar o corpus
    corpus_manager = CorpusManager(config)
    if hasattr(corpus_manager, "load_corpus"):
        corpus_manager.load_corpus()
    if hasattr(corpus_manager, "update_knowledge_base"):
        corpus_manager.update_knowledge_base()
    
    # Inicializar o assistente virtual
    nlu = NLUAdapter() if NLUAdapter else None
    audit_logger = AuditLogger() if AuditLogger else None

    # vector_store / llm_client devem ser criados aqui (ou passados como None para implementar depois)
    vector_store = None
    llm_client = None

    # 4. Inicializar o assistente / orquestrador
    if Orchestrator:
        assistant = Orchestrator(nlu, vector_store, llm_client, audit_logger)
    else:
        # fallback simples: instanciar com config (compatibilidade com main original)
        from assistente_virtual.assistant import RAGCoreAssistant
        assistant = RAGCoreAssistant(config)
    
    # 5. Criar e iniciar a API (se disponível)
    if create_api:
        api = create_api(assistant)
        # dependendo da implementação do create_api, pode ser .run() ou uvicorn
        if hasattr(api, "run"):
            api.run()
        else:
            # caso seja uma FastAPI app
            import uvicorn
            uvicorn.run(api, host="0.0.0.0", port=8000)
    else:
        print("API não encontrada. Assistente carregado em modo console.")
        # exemplo de loop de teste simples
        while True:
            q = input("Pergunta (ou 'sair'): ")
            if q.strip().lower() in ("sair", "exit", "quit"):
                break
            try:
                resp = assistant.process_message(q)
            except Exception as e:
                resp = f"Erro ao processar: {e}"
            print(resp)

if __name__ == "__main__":
    main()