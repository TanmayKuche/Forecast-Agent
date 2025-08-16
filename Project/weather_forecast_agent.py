from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.tools import tool
import requests

from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city : str) ->str:

    url = f"https://api.*my*_*api*_*key*{city}"

    response = requests.get(url)
    return response.json()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

prompt = hub.pull("hwchase17/react") 

agent = create_react_agent(
    llm = model,
    tools = [search_tool, get_weather_data],
    prompt= prompt
)

agent_executor = AgentExecutor(
    agent= agent,
    tools = [search_tool,get_weather_data],
    verbose=True
)

def invoke(input_query):
    response = agent_executor.invoke({"input" :input_query})

    return response["output"]