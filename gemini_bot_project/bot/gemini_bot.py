# bot/gemini_bot.py
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from .tools import search_internet, marcar_presenca, listar_presencas
from .config import load_model


class GeminiBot:
    def __init__(self, model_name="gemini-2.0-flash"):
        """Inicializa o bot com modelo e ferramentas."""
        self.model = load_model(model_name)
        self.tools = [search_internet, marcar_presenca, listar_presencas]
        self.agent_executor = create_react_agent(self.model, self.tools)
        self.chat_history = []

    def ask(self, user_input: str) -> str:
        """Processa uma pergunta do usuário e retorna a resposta do modelo."""
        self.chat_history.append(HumanMessage(content=user_input))
        response = self.agent_executor.invoke({"messages": self.chat_history})
        ai_message = response["messages"][-1]
        self.chat_history.append(ai_message)
        return ai_message.content

    def run_loop(self):
        """Executa o loop de interação com o usuário via terminal."""
        print("🤖 GeminiBot (TCC) iniciado. Pergunte algo! (digite 'sair' para encerrar)")
        while True:
            user_input = input("Você: ")
            if user_input.lower() in ["sair", "exit", "quit"]:
                print("Bot: Até logo!")
                break
            resposta = self.ask(user_input)
            print("Bot:", resposta)
