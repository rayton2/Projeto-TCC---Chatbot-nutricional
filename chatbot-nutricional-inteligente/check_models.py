import google.generativeai as genai

# --- COLE SUA CHAVE NOVA AQUI DENTRO DAS ASPAS ---
MINHA_CHAVE="AIzaSyCWMto7L_3DImwGxpgYDuZwagavtzhgsNQ" 

if "COLE_SUA_CHAVE" in MINHA_CHAVE:
    print("❌ Erro: Você esqueceu de colar a chave no código acima!")
else:
    print(f"🔑 Testando chave: {MINHA_CHAVE[:5]}...")
    
    try:
        genai.configure(api_key=MINHA_CHAVE)
        print("📡 Perguntando ao Google quais modelos você pode usar...")
        
        # Lista modelos
        modelos = list(genai.list_models())
        encontrou = False
        
        print("\n--- ✅ MODELOS DISPONÍVEIS NA SUA CONTA ---")
        for m in modelos:
            if 'generateContent' in m.supported_generation_methods:
                # Mostra o nome exato que devemos usar
                nome_limpo = m.name.replace("models/", "")
                print(f"👉 {nome_limpo}")
                encontrou = True
        
        if not encontrou:
            print("⚠️ A chave conectou, mas nenhum modelo de chat foi encontrado.")
            
    except Exception as e:
        print(f"\n❌ A chave não funcionou. Erro: {e}")