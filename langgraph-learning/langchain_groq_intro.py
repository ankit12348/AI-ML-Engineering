import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a concise technical assistant."), ("human", "{question}")]
)

chain = prompt | model

response = chain.invoke({"question": "What is state management?"})
print(response.content)
