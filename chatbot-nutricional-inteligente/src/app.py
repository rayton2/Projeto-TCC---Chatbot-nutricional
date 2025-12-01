import streamlit as st
from bot_logic import criar_cerebro_nutricional
from tools import calcular_imc, calcular_agua, classificar_imc

# Configuração da Página
st.set_page_config(page_title="NutriBot TCC", page_icon="🍎")
st.title("🍎 Chatbot Nutricional Inteligente")

# Barra Lateral (Tools)
with st.sidebar:
    st.header("🧮 Calculadora Rápida")
    peso = st.number_input("Peso (kg)", min_value=0.0, format="%.2f")
    altura = st.number_input("Altura (m)", min_value=0.0, format="%.2f")
    
    if st.button("Calcular"):
        if peso > 0 and altura > 0:
            imc = calcular_imc(peso, altura)
            classif = classificar_imc(imc)
            agua = calcular_agua(peso)
            st.success(f"Seu IMC é **{imc}** ({classif})")
            st.info(f"💧 Beba aprox. **{agua} L** de água por dia.")
        else:
            st.warning("Preencha peso e altura!")

# Área do Chat (RAG)
st.divider()
st.subheader("💬 Tire suas dúvidas")

# Inicializa o chatbot (cache para não recarregar toda hora)
if "chatbot" not in st.session_state:
    chain, status = criar_cerebro_nutricional()
    if chain:
        st.session_state["chatbot"] = chain
        st.success("Cérebro Nutricional carregado!")
    else:
        st.error(status)

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra mensagens antigas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de input do usuário
prompt = st.chat_input("Ex: Quais alimentos ajudam a ganhar massa?")

if prompt:
    # 1. Mostra pergunta do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Gera resposta do bot
    if "chatbot" in st.session_state:
        with st.chat_message("assistant"):
            with st.spinner("Consultando base de conhecimento..."):
                resposta = st.session_state["chatbot"].run(prompt)
                st.markdown(resposta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})