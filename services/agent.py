from deepagents import create_deep_agent
from core.config import model
from utils.tavily_search_tool import web_search
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()

agent = create_deep_agent(model=model,
                          tools=[web_search],
                          checkpointer=checkpointer,
                          system_prompt="""You are a methodical researcher. ALWAYS:
                            1. Use `write_todos` FIRST to plan your approach
                            2. Break complex tasks into steps
                            3. Use `web_search` for current info
                            4. Update todos as you progress
                            5. Write final summary"""
                        )
