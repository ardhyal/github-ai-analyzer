from github_client import (
    get_github_user,
    get_github_repositories,
    get_top_repositories,
    extract_repository_summary
)

from prompt_builder import (
    build_summary_prompt,
    format_repositories
)

from llm_client import generate_summary

from response_parser import parse_ai_response


def analyze_github_user(username):
    user = get_github_user(username)

    if not user:
        return {
            "error": "GitHub user not found"
        }

    repos = get_github_repositories(username)

    top_repos = get_top_repositories(repos)

    repo_summary = extract_repository_summary(
        top_repos
    )

    repository_text = format_repositories(
        repo_summary
    )

    prompt = build_summary_prompt(
        user,
        repository_text
    )

    summary = generate_summary(prompt)

    return parse_ai_response(summary)