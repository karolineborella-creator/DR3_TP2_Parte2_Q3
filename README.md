Questão 3 — API de Tradução Inglês-Alemão

1. Objetivo

Desenvolver uma API REST para traduzir textos do inglês para o alemão, utilizando FastAPI, LangChain e o modelo de tradução "Helsinki-NLP/opus-mt-en-de", disponibilizado pelo Hugging Face.

A aplicação utiliza processamento local, sem necessidade de contratar serviços pagos de tradução.

2. Tecnologias utilizadas

- Python 3.12: linguagem de programação.
- FastAPI: criação dos endpoints da API REST.
- Pydantic: validação dos dados de entrada e saída.
- LangChain: gerenciamento da chamada ao modelo por meio de "RunnableLambda".
- Hugging Face Transformers: carregamento e execução do modelo de tradução.
- Helsinki-NLP/opus-mt-en-de: modelo de tradução inglês-alemão.
- Uvicorn: servidor ASGI utilizado para executar a aplicação.

3. Arquitetura da aplicação

flowchart TD
    A["Cliente / Swagger UI"] -->|POST /traduzir| B["FastAPI"]
    B --> C["Validação Pydantic"]
    C --> D["LangChain - RunnableLambda"]
    D --> E["Hugging Face Transformers"]
    E --> F["Helsinki-NLP/opus-mt-en-de"]
    F -->|Texto em alemão| E
    E --> D
    D --> B
    B -->|Resposta JSON| A

Descrição do fluxo

1. O cliente envia um texto em inglês ao endpoint "POST /traduzir".
2. O FastAPI recebe a requisição e o Pydantic valida os dados.
3. O LangChain utiliza "RunnableLambda" para executar a função de tradução.
4. A biblioteca Transformers processa o texto utilizando o modelo "Helsinki-NLP/opus-mt-en-de".
5. O resultado retorna ao FastAPI, que fornece uma resposta JSON com o texto original e a tradução para o alemão.

O modelo é carregado durante a inicialização da aplicação, evitando seu recarregamento a cada requisição.

4. Instalação e execução

Instale as dependências:

python -m pip install -r requirements.txt

Inicie a aplicação:

python -m uvicorn main:app --reload

Acesse a documentação interativa:

"http://127.0.0.1:8000/docs"

Na primeira execução, os arquivos do modelo poderão ser baixados automaticamente do Hugging Face.

5. Teste da API

Endpoint: "POST /traduzir"

Requisição JSON:

{
  "texto": "Good morning, how are you today?"
}

Resposta obtida no teste:

{
  "texto_original": "Good morning, how are you today?",
  "texto_traduzido": "Guten Morgen, wie geht's dir heute?"
}

Código HTTP: "200 OK"

O teste foi realizado pelo Swagger UI, confirmando o funcionamento da tradução e o retorno da resposta em formato JSON.

6. Considerações finais

A aplicação atende ao objetivo de integrar FastAPI, LangChain e Hugging Face em um serviço de tradução automática.

A execução local permite realizar traduções sem cobrança por requisição de API externa. Entretanto, o desempenho depende dos recursos computacionais disponíveis, e o carregamento inicial do modelo pode demandar tempo adicional.