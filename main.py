from analysis_service import (
    analyze_github_user
)

import json


def main():
    username = input(
        "GitHub username: "
    )

    result = analyze_github_user(
        username
    )

    print(
        json.dumps(
            result,
            indent=2
        )
    )


if __name__ == "__main__":
    main()