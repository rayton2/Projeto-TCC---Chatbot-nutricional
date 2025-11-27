# Chatbot Nutricional Inteligente

Este projeto é um Chatbot Nutricional Inteligente desenvolvido em Python 3.10+. O objetivo é fornecer um assistente virtual que ajude os usuários a obter informações nutricionais e suporte em suas jornadas de saúde.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
chatbot-nutricional-inteligente
├── src
│   ├── main.py                     # Ponto de entrada da aplicação
│   ├── core
│   │   └── config.py               # Configurações globais do projeto
│   ├── geracao_base_conhecimento
│   │   ├── generator.py            # Classe para gerenciamento de corpus
│   │   ├── embeddings.py            # Funções auxiliares para embeddings
│   │   ├── storage.py               # Persistência de embeddings
│   │   └── models.py                # Modelos de dados
│   ├── assistente_virtual
│   │   ├── assistant.py             # Classe do assistente virtual
│   │   ├── prompt_manager.py        # Gerenciamento de prompts
│   │   └── responder.py             # Lógica de resposta do assistente
│   ├── gerenciamento_suporte
│   │   ├── message_handler.py       # Gerenciamento de mensagens
│   │   ├── logger.py                # Registro de interações
│   │   └── api.py                   # Implementação da API
│   ├── models
│   │   ├── user.py                  # Estrutura de dados para usuários
│   │   └── message.py               # Estrutura de dados para mensagens
│   └── utils
│       ├── db.py                    # Funções auxiliares para o banco de dados
│       └── nlp.py                   # Funções auxiliares para NLP
├── tests
│   ├── test_geracao_base_conhecimento.py  # Testes para geração de base de conhecimento
│   ├── test_assistente_virtual.py          # Testes para assistente virtual
│   └── test_gerenciamento_suporte.py       # Testes para gerenciamento e suporte
├── docs
│   └── arquitetura.md                      # Documentação da arquitetura
├── data
│   ├── corpus.sql                          # Dados estruturados
│   └── structured_text                     # Textos estruturados
├── pyproject.toml                          # Configuração do projeto
├── requirements.txt                        # Bibliotecas necessárias
├── .gitignore                              # Arquivos a serem ignorados
└── README.md                               # Documentação do projeto
```

## Instalação

Para instalar as dependências do projeto, execute:

```
pip install -r requirements.txt
```

## Uso

Para iniciar o chatbot, execute o seguinte comando:

```
python src/main.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.