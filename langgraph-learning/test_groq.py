import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

print("Invoking Groq...")
response = model.invoke("Say hello!")
print("Response received:")
print(response.content)