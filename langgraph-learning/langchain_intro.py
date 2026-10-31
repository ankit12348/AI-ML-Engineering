import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.7)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a witty assistant that explains technical concepts using funny food analogies.",
        ),
        ("human", "{topic}"),
    ]
)

chain = prompt | model

print("Invoking LangChain pipeline with Gemini...")
result = chain.invoke({"topic": "How do computer databases work?"})

print("\n--- Gemini AI Response ---")
print(result.content)
