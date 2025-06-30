# Projeto: Integração de LLM com API via Function Calling

Este repositório reúne dois componentes principais que demonstram a integração de **Modelos de Linguagem Grandes (LLMs)** com sistemas externos por meio da funcionalidade **Function Calling**, utilizando o modelo **Gemini da Google**, a biblioteca **LangChain**, e uma **API acadêmica simulada** desenvolvida com FastAPI.

## Estrutura do Repositório
📁 api_fast → API simulando um sistema acadêmico (marcação de presença e listagem de registro).

📁 gemini-bot-project → Bot genérico em Python com suporte a LLM e Function Calling.


## 💡 Objetivo

Explorar como os LLMs podem interagir com APIs externas por meio da funcionalidade de **chamadas de função (Function Calling)**, interpretando comandos em linguagem natural e executando ações de forma automatizada com suporte do **LangChain**.

## 🚀 Como Rodar o Projeto

### 1. Clonando o repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Executando a API (FastAPI)
#### Pré-requisitos:
- Python 3.10+
- FastAPI
- Uvicorn
#### Passos:
```bash
cd api_fast
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Executando o Bot com LLM
#### Pré-requisitos:
- Python 3.10+
- LangChain
- Google Generative AI SDK (Gemini)
- python-dotenv
  
#### Passos:
```bash
cd ../gemini-bot-project
pip install -r requirements.txt
```
Crie um arquivo .env com as seguintes variáveis:
```bash
GOOGLE_API_KEY=your_gemini_api_key
API_URL=http://localhost:8000
```

Então, execute:

```bash
python main.py
```

O bot estará pronto para receber comandos e interagir com a API.
