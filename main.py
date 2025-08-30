import asyncio
import os

from dotenv import load_dotenv
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
    print("Hello from langchain-mcp-integration!")

if __name__ == "__main__":
    asyncio.run(main())




