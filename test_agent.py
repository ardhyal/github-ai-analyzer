from agent_service import (
    select_tool_with_ai
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


result = select_tool_with_ai(
    "Analyze GitHub user torvalds"
)

print(result)
