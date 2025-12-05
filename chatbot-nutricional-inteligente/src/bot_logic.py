import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Carrega a chave de API
load_dotenv()

# Classe wrapper para manter compatibilidade com o app.py (que chama .run())
class RAGSimples:
    def __init__(self, chain):
        self.chain = chain
    
    def run(self, query):
        # O LCEL usa .invoke(), mas seu app.py usa .run()
        # Esse método faz a tradução
        return self.chain.invoke(query)

def criar_cerebro_nutricional():
    # 1. Validação do arquivo
    path = "data/nutricao.txt"
    if not os.path.exists(path):
        return None, "Erro: Arquivo data/nutricao.txt não encontrado."

    try:
        loader = TextLoader(path, encoding='utf-8')
        documentos = loader.load()
    except Exception as e:
        return None, f"Erro ao ler arquivo: {e}"

    # 2. Embeddings e Vector Store
    try:
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = FAISS.from_documents(documentos, embeddings)
        retriever = vectorstore.as_retriever()
    except Exception as e:
        return None, f"Erro ao criar Memória Local: {e}"

    # 3. LLM (Gemini)
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)
    except Exception as e:
        return None, f"Erro ao conectar no Gemini: {e}"

    # 4. Prompt
    template = """
    Você é um nutricionista virtual chamado NutriBot.
    Use o contexto abaixo para responder à pergunta.
    Se não souber, diga que não tem essa informação.
    
    Contexto: {context}
    
    Pergunta: {question}
    """
    prompt = PromptTemplate.from_template(template)

    # 5. A Nova Chain (LCEL - Método Moderno)
    # Isso substitui o RetrievalQA antigo e não depende de 'langchain.chains'
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # Retorna nossa classe wrapper para funcionar com o app.py antigo
    return RAGSimples(rag_chain), "Sucesso"