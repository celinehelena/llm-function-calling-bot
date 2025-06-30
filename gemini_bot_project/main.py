# main.py
from bot.gemini_bot import GeminiBot
from dotenv import load_dotenv
import os

load_dotenv()


if __name__ == "__main__":
    bot = GeminiBot()
    bot.run_loop()
