from tool_registry import (
    register_tool,
    get_tools_metadata
)

def dummy():
    pass

register_tool(
    "github",
    dummy,
    "Analyze GitHub profile",
    {
        "username": "string"
    }
)

print(
    get_tools_metadata()
)