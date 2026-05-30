from llm_client import generate_summary


response = generate_summary(
    """
    Explain what GitHub is in 3 sentences.
    """
)

print(response)