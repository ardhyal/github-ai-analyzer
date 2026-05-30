from agent_executor import (
    execute_agent
)

from tool_registry import (
    register_tool
)

from analysis_service import (
    analyze_github_user
)

from resume_service import (
    analyze_resume
)

register_tool(
    "github",
    analyze_github_user,
    "Analyze GitHub profile and repositories"
)

register_tool(
    "resume",
    analyze_resume,
    "Analyze resume and provide career insights"
)

result = execute_agent(
    "Analyze GitHub user torvalds"
)

print(result)