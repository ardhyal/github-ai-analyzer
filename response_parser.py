import json


def parse_ai_response(response):

    try:

        response = response.replace(
            "```json",
            ""
        )

        response = response.replace(
            "```",
            ""
        )

        response = response.strip()

        return json.loads(response)

    except Exception:

        return {
            "error": True,
            "raw_response": response
        }