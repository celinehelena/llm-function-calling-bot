import requests
from langchain_core.tools import tool

@tool
def marcar_presenca(nome: str) -> str:
    """Marca a presença de uma pessoa chamando uma API local."""
    url = "http://127.0.0.1:8000/presenca"
    payload = {"nome": nome}
    try:
        response = requests.post(url, json=payload)
        return response.json().get("mensagem", "Erro ao marcar presença.")
    except Exception as e:
        return f"Erro ao chamar API: {str(e)}"

@tool
def listar_presencas() -> str:
    """Retorna a lista de presenças marcadas."""
    url = "http://127.0.0.1:8000/presenca"
    try:
        response = requests.get(url)
        lista = response.json()
        return "\n".join([f"{p['nome']} - {p['data_hora']}" for p in lista])
    except Exception as e:
        return f"Erro ao chamar API: {str(e)}"
@tool
def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set the brightness and color temperature of a room light. (mock API).

    Args:
        brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
        color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

    Returns:
        A dictionary containing the set brightness and color temperature.
    """
    return {"brightness": brightness, "colorTemperature": color_temp}
