import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Carrega a chave de API do arquivo .env
load_dotenv()

def criar_cerebro_nutricional():
    # 1. Carregar o conhecimento (seu arquivo de texto)
    # Certifique-se de criar o arquivo 'data/nutricao.txt' com textos sobre dieta!
    path = "data/nutricao.txt"
    if not os.path.exists(path):
        return None, "Erro: Arquivo data/nutricao.txt não encontrado."

    loader = TextLoader(path, encoding='utf-8')
    documentos = loader.load()

    # 2. Criar a memória (Vector Store)
    # Transforma texto em números (Embeddings) para busca rápida
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documentos, embeddings)

    # 3. Configurar o Cérebro (LLM)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # 4. Criar o Prompt Personalizado (A "Personalidade")
    template_prompt = """
    Você é um nutricionista virtual gentil e prestativo.
    Use o contexto abaixo para responder à dúvida do usuário.
    Se a resposta não estiver no contexto, diga que não sabe, mas sugira procurar um médico.
    Não invente informações médicas.
    
    Contexto: {context}
    
    Pergunta do Usuário: {question}
    
    Resposta Nutricional:
    """
    PROMPT = PromptTemplate(
        template=template_prompt, input_variables=["context", "question"]
    )

    # 5. Montar a corrente (Chain)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    return qa_chain, "Sucesso"