from agent_service import (
    select_tool_with_ai
)

from tool_registry import (
    execute_tool
)


def execute_agent(user_prompt):

    decision = select_tool_with_ai(
        user_prompt
    )

    print(
        f"\nAgent Decision:"
    )

    print(decision)

    tool_name = decision["tool"]

    tool_args = decision["args"]

    return execute_tool(
        tool_name,
        **tool_args
    )