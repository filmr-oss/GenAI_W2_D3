from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain what artificial intelligence is in one simple paragraph.",
    "What is LangChain and why is it useful?",
    "Explain LangSmith to a beginner in three sentences."
]

for prompt in prompts:
    response = llm.invoke(prompt)
    print("\nPrompt:", prompt)
    print("Answer:", response.content)