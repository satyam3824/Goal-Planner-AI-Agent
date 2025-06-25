# agent.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from memory import save_to_memory
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Get API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "your-fallback-key")

# LLM setup
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7,
)

# Prompt
prompt = PromptTemplate(
    input_variables=["input"],
    template="""You are a helpful AI assistant that helps users plan their goals and track progress.

User Input: {input}

Give a structured and motivating response with actionable steps."""
)

# Chain
chain = prompt | llm

# Agent function
def ask_agent(user_input):
    response = chain.invoke({"input": user_input})
    save_to_memory(user_input, response.content)
    return response.content
