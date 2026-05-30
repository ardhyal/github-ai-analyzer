from llm_client import generate_summary

from agent_response_parser import (
    parse_agent_response
)

from tool_registry import (
    get_tools_metadata
)

def build_tool_description():

    tools = get_tools_metadata()

    lines = []

    for name, info in tools.items():

        lines.append(
            f"""
Tool: {name}

Description:
{info["description"]}
"""
        )

    return "\n".join(lines)

def select_tool_with_ai(user_prompt):
    tool_descriptions = (
        build_tool_description()
    )
    
    prompt = f"""
You are an AI agent.

Available tools:

{tool_descriptions}

Analyze the user request.

Return ONLY valid JSON.

Rules:

If user wants GitHub analysis:

{{
    "tool": "github",
    "args": {{
        "username": "<github_username>"
    }}
}}

If user wants resume analysis:

{{
    "tool": "resume",
    "args": {{
        "file_path": "resume.pdf"
    }}
}}

User request:

{user_prompt}
"""

    response = generate_summary(prompt)

    return parse_agent_response(
        response
    )