import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/shaunlim/Desktop/personal_projects/llm_applications/langchain-mcp-integration/servers/math_server.py"],
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)

            agent = create_react_agent(llm, tools)

            response = await agent.ainvoke({"messages": [HumanMessage(content="What is 10 + 2 * 43?")]})
            print(response["messages"][-1].content)
            

if __name__ == "__main__":
    asyncio.run(main())




