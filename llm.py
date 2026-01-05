import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

llm = ChatGroq(
    api_key="",
    model="openai/gpt-oss-20b",
    temperature=0
)

def generate_doc(prompt: str) -> str:
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
