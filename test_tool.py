from tool_registry import (
    register_tool,
    execute_tool,
    list_tools
)


def hello(name):
    return f"Hello {name}"


register_tool(
    "hello",
    hello
)

print(list_tools())

print(
    execute_tool(
        "hello",
        "Ardi"
    )
)