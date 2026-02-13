import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()



model = ChatGoogleGenerativeAI(
    model = os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=os.getenv("TEMPERATURE")
)

agent_config = {"configurable": {"thread_id": "user-123"}}
