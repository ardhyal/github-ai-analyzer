from agent_executor import (
    execute_agent
)

from tool_registry import (
    register_tool
)

from analysis_service import (
    analyze_github_user
)


register_tool(
    "github",
    analyze_github_user,
    "Analyze GitHub profile and repositories",
    {
        "username": "string"
    }
)

from tool_registry import get_tools_metadata

print(get_tools_metadata())

result = execute_agent(
    "Analyze GitHub user torvalds"
)

print(result)