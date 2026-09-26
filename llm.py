from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

GROQ_MODEL = "groq:openai/gpt-oss-20b"
groq = init_chat_model(GROQ_MODEL)
llm = groq
