# Arquitetura do Chatbot Nutricional Inteligente

## Visão Geral

O Chatbot Nutricional Inteligente é um sistema projetado para fornecer informações nutricionais e suporte aos usuários por meio de um assistente virtual. O sistema é estruturado em várias camadas, cada uma responsável por uma parte específica da funcionalidade do chatbot.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
chatbot-nutricional-inteligente
├── src
│   ├── main.py
│   ├── core
│   │   └── config.py
│   ├── geracao_base_conhecimento
│   │   ├── generator.py
│   │   ├── embeddings.py
│   │   ├── storage.py
│   │   └── models.py
│   ├── assistente_virtual
│   │   ├── assistant.py
│   │   ├── prompt_manager.py
│   │   └── responder.py
│   ├── gerenciamento_suporte
│   │   ├── message_handler.py
│   │   ├── logger.py
│   │   └── api.py
│   ├── models
│   │   ├── user.py
│   │   └── message.py
│   └── utils
│       ├── db.py
│       └── nlp.py
├── tests
│   ├── test_geracao_base_conhecimento.py
│   ├── test_assistente_virtual.py
│   └── test_gerenciamento_suporte.py
├── docs
│   └── arquitetura.md
├── data
│   ├── corpus.sql
│   └── structured_text
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Componentes Principais

### 1. Geração de Base de Conhecimento

- **generator.py**: Implementa a classe `CorpusManager`, responsável por carregar, limpar e segmentar documentos, além de gerar embeddings.
- **embeddings.py**: Contém funções auxiliares para a geração e manipulação de embeddings.
- **storage.py**: Gerencia a persistência dos embeddings no banco de dados vetorial.
- **models.py**: Define modelos de dados utilizados na geração da base de conhecimento.

### 2. Assistente Virtual

- **assistant.py**: Implementa a classe `RAGCoreAssistant`, que gerencia o fluxo de conversação e a interação com o modelo LLM.
- **prompt_manager.py**: Contém funções para gerenciar e construir prompts para o modelo LLM.
- **responder.py**: Implementa a lógica de resposta do assistente virtual.

### 3. Gerenciamento e Suporte

- **message_handler.py**: Implementa a classe `MessageManager`, que gerencia a comunicação e a interface do assistente.
- **logger.py**: Implementa a classe `LogManager`, responsável por registrar interações e eventos.
- **api.py**: Contém a implementação da API utilizando FastAPI ou Flask.

### 4. Modelos

- **user.py**: Define a estrutura de dados para usuários que interagem com o assistente.
- **message.py**: Define a estrutura de dados para mensagens trocadas entre o usuário e o assistente.

### 5. Utilitários

- **db.py**: Contém funções auxiliares para interações com o banco de dados.
- **nlp.py**: Contém funções auxiliares para processamento de linguagem natural.

## Conclusão

Este projeto visa criar um assistente virtual que não apenas responde a perguntas sobre nutrição, mas também aprende e se adapta às necessidades dos usuários. A arquitetura modular permite fácil manutenção e expansão das funcionalidades do chatbot.