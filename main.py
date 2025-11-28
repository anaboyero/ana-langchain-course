from typing import List
from pydantic import BaseModel, Field 

from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str ) -> str: 
    '''
    Tool that searches over internet
    Args:
        query: the query to search for 
    Return:
        The search results
    '''
    print(f"Searching for {query}...") 
    return "Tokyo weather is snowing with -1 Celsius degrees."
    
#llm = ChatOllama(model="gpt-oss:latest")
llm = ChatOpenAI()
tools = [search] 
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from search-agent!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    print(result)

if __name__ == "__main__":
    main()
