from analysis_service import (
    analyze_github_user
)

from tool_selector import (
    select_tool
)

from tool_registry import (
    register_tool,
    execute_tool,
    list_tools
)

import json

register_tool(
    "github",
    analyze_github_user,
    "Analyze GitHub profile and repositories",
    {
        "username": "string"
    }
)


def main():

    print("\nAvailable tools:")

    for tool in list_tools():
        print(f"- {tool}")

    user_prompt = input(
        "\nWhat would you like to analyze? "
    )

    tool_name = select_tool(
        user_prompt
    )

    print(
        f"\nSelected tool: {tool_name}"
    )

    if tool_name == "github":

        username = input(
            "GitHub username: "
        )

        result = execute_tool(
            tool_name,
            username
        )

    elif tool_name == "resume":

        result = execute_tool(
            tool_name,
            "resume.pdf"
        )

    print(
        json.dumps(
            result,
            indent=2
        )
    )


if __name__ == "__main__":
    main()