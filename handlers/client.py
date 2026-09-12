from os import getenv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=getenv("AI_KEY"),
    base_url="https://speshu.ai/api/v1"
)