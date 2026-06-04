from app import agent
print("Agent tools:")
for tool_name, tool in agent.tools.items():
    print(f"- {tool_name}: {tool.description}")
