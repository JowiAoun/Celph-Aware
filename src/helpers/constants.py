import os

from dotenv import load_dotenv


load_dotenv()


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
LLM_MAX_RETRIES = 3