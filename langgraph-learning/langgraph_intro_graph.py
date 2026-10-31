import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. Load environment variables from .env
load_dotenv()


# 2. Define the State Schema (The shared memory dictionary passing through nodes)
class AgentState(TypedDict):
    topic: str
    draft: str
    critique: str


# 3. Initialize your working Groq model
model = ChatGroq(model="openai/gpt-oss-20b")


# 4. Define Node 1: The Writer
def writer_node(state: AgentState) -> AgentState:
    print("\n--- [NODE: WRITER] Generating content... ---")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You write short, clear technical explanations."),
            ("human", "Write a brief intro about {topic}"),
        ]
    )
    chain = prompt | model
    result = chain.invoke({"topic": state["topic"]})

    # Return updates to the state
    return {"draft": result.content}


# 5. Define Node 2: The Critic
def critic_node(state: AgentState) -> AgentState:
    print("\n--- [NODE: CRITIC] Reviewing content... ---")
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a strict technical editor. Provide one concise sentence of feedback.",
            ),
            ("human", "Review this draft: {draft}"),
        ]
    )
    chain = prompt | model
    result = chain.invoke({"draft": state["draft"]})

    # Return updates to the state
    return {"critique": result.content}


# 6. Build the LangGraph Workflow Blueprint
workflow = StateGraph(AgentState)

# Add our nodes to the graph
workflow.add_node("writer", writer_node)
workflow.add_node("critic", critic_node)

# Define the execution flow edges: START -> writer -> critic -> END
workflow.add_edge(START, "writer")
workflow.add_edge("writer", "critic")
workflow.add_edge("critic", END)

# Compile the graph into an executable application
app = workflow.compile()

# 7. Execute the Graph
print("Initializing LangGraph execution...")
initial_input = {"topic": "State Management in Web Apps"}
final_state = app.invoke(initial_input)

# 8. Print Results
print("\n==============================")
print("=== FINAL GRAPH RESULTS ===")
print("==============================")
print(f"**Topic:** {final_state.get('topic')}\n")
print(f"**Draft Output:**\n{final_state.get('draft')}\n")
print(f"**Critic Feedback:**\n{final_state.get('critique')}")
