TOOLS = {}


def register_tool(
    name,
    func,
    description,
    parameters
):

    TOOLS = {
    "github": {
        "function": ...,
        "description": ...,
        "parameters": ...
    }
}


def execute_tool(
    name,
    *args,
    **kwargs
):

    if name not in TOOLS:
        raise ValueError(
            f"Tool '{name}' not found"
        )

    return TOOLS[name]["function"](
        *args,
        **kwargs
    )


def list_tools():
    return list(
        TOOLS.keys()
    )


def get_tools_metadata():
    return TOOLS