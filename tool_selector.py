def select_tool(user_prompt):
    prompt = user_prompt.lower()

    if "github" in prompt:
        return "github"

    if "resume" in prompt:
        return "resume"

    raise ValueError(
        "Unable to determine tool"
    )