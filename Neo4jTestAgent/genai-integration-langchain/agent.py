import os
from llm import llm
from graph import graph
from langchain.tools import Tool
from langchain_neo4j import Neo4jChatMessageHistory
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_vertexai import ChatVertexAI
from langgraph.prebuilt import create_react_agent
from toolbox_langchain import ToolboxClient

from dotenv import load_dotenv
load_dotenv()

model = ChatVertexAI(model_name="gemini-1.5-pro")
client = ToolboxClient("http://localhost:5000")

async def get_agent():
    tools = await client.aload_toolset()
    return create_react_agent(model, tools)

def generate_response(query: str):
    agent = get_agent()
    response = agent.invoke({
        "messages": [("user", query)]
    })
    return response["messages"][-1].content

tools = [
    Tool.from_function(
        name="General Chat",
        description="For general movie questions",
        func=lambda query: "Response from LLM"
    )
]


def get_memory(session_id):
    return Neo4jChatMessageHistory(session_id=session_id, graph=graph)


agent = create_react_agent(llm, tools, prompt=hub.pull("hwchase17/react-chat"))
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

chat_agent = RunnableWithMessageHistory(
    agent_executor,
    get_memory,
    input_messages_key="input",
    history_messages_key="chat_history"
)

def generate_response(query):
    return chat_agent.invoke(
        {"input": query},
        {"configurable": {"session_id": "test-session"}}
    )["output"]