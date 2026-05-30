import requests


def get_github_user(username):
    response = requests.get(
        f"https://api.github.com/users/{username}",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def get_github_repositories(username):
    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def get_top_repositories(repos, limit=5):
    """
    Sort repositories by stars and return top repositories.
    """

    sorted_repos = sorted(
        repos,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

    return sorted_repos[:limit]


def extract_repository_summary(repos):
    """
    Keep only important repository information.
    """

    summary = []

    for repo in repos:
        summary.append({
            "name": repo["name"],
            "description": repo["description"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"]
        })

    return summary