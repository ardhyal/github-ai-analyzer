import json


def parse_ai_response(response_text):
    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        return {
            "error": True,
            "raw_response": response_text
        }