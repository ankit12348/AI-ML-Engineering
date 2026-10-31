# chat_history = [
#     {"role": "user", "content": "Hi, what is LangGraph?"},
#     {"role": "assistant", "content": "LangGraph is a library for building stateful, multi-agent applications."}
# ]

# chat_history.append({"role": "user", "content": "Can it build loops?"})

# print(chat_history)

# class SimpleLLMWrapper:

#     def __int__(self, model_name: str, temperature: float = 0.7):
#         self.model_name = model_name
#         self.temperature = temperature
#         self.call_count = 0;

#     def generate(self, prompt: str) -> str:
#         self.call_count += 1
#         return f"[{self.model_name} (temp: {self.temperature})] Response to: '{prompt}' (Call #{self.call_count})"

# gpt_model = SimpleLLMWrapper(model_name="gpt-4o", temperature=0.2)
# claude_model = SimpleLLMWrapper(model_name="claude-3-5-sonnet", temperature=0.9)

# print(gpt_model.generate("Explain black holes"))
# print(gpt_model.generate("What is quantum computing?"))
# print(claude_model.generate("Write a haiku about code"))

# def sample_node_function(state: dict) -> dict:
#     print("-> Running node logic...")
#     state["processed"] = True
#     return state

# def run_graph_engine(node_func, initial_state: dict):
#     print("Engine starting graph execution...")
#     result_state = node_func(initial_state)
#     print("Engine finished execution.")
#     return result_state

# my_initial_state = {"data": "raw text"}
# final_state = run_graph_engine(sample_node_function, my_initial_state)

# print("Final State Result:", final_state)

class AgentMemory:
    def __init__(self, memory_bank: list = None):
        if memory_bank is None:
            self.memory_bank = []
        else:
            self.memory_bank = memory_bank

    def add_memory(self, item: str):
        self.memory_bank.append(item)

agent_memory = AgentMemory()
agent_memory.add_memory("Ankit")
agent_memory.add_memory("Mahima")

print(agent_memory.memory_bank)

