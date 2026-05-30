def build_summary_prompt(user, repositories):
    return f"""
You are a Senior Software Architect, Technical Recruiter, and Engineering Manager.

Analyze the following GitHub profile.

====================
PROFILE
====================

Name: {user.get('name')}
Username: {user.get('login')}
Bio: {user.get('bio')}
Followers: {user.get('followers')}
Following: {user.get('following')}
Public Repositories: {user.get('public_repos')}
Company: {user.get('company')}
Location: {user.get('location')}

====================
TOP REPOSITORIES
====================

{repositories}

====================
TASK
====================

Based on the profile and repositories:

1. Professional Summary
2. Estimated Seniority Level
3. Technical Expertise
4. Main Programming Languages
5. Industry Influence
6. Open Source Contribution Impact
7. Career Insights
8. Key Strengths
9. Areas of Specialization
10. Interesting Observations

Be objective and data-driven.

Important Rules:

- Base conclusions only on the provided data.
- Do not make assumptions without evidence.
- If information is missing, state "Unknown".
- Keep responses concise.
- Technical expertise must be returned as an array.
- Main programming languages must be returned as an array.
- Career insights must be returned as an array.
- Key strengths must be returned as an array.
- Specializations must be returned as an array.
- Interesting observations must be returned as an array.

====================
OUTPUT FORMAT
====================

Return ONLY valid JSON.

Do not include:
- markdown
- code fences
- explanations
- additional text

Use this exact structure:

{{
  "professional_summary": "",
  "seniority_level": "",
  "technical_expertise": [],
  "main_languages": [],
  "industry_influence": "",
  "open_source_impact": "",
  "career_insights": [],
  "key_strengths": [],
  "specializations": [],
  "interesting_observations": []
}}
"""

def format_repositories(repositories):
    lines = []

    for repo in repositories:
        lines.append(
            f"""
Repository: {repo['name']}
Description: {repo['description']}
Language: {repo['language']}
Stars: {repo['stars']}
Forks: {repo['forks']}
"""
        )

    return "\n".join(lines)

