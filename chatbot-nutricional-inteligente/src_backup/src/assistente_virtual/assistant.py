class RAGCoreAssistant:
    def __init__(self, knowledge_base, llm_model):
        self.knowledge_base = knowledge_base
        self.llm_model = llm_model

    def process_user_input(self, user_input):
        # Processa a entrada do usuário e gera uma resposta
        response = self.generate_response(user_input)
        return response

    def generate_response(self, user_input):
        # Gera uma resposta utilizando o modelo LLM e a base de conhecimento
        context = self.retrieve_context(user_input)
        response = self.llm_model.generate(context, user_input)
        return response

    def retrieve_context(self, user_input):
        # Recupera o contexto relevante da base de conhecimento
        context = self.knowledge_base.get_relevant_info(user_input)
        return context

    def update_knowledge_base(self, new_data):
        # Atualiza a base de conhecimento com novos dados
        self.knowledge_base.add_data(new_data)