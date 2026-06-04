#!/usr/bin/env python3
import json
import os
import re
import sys
import urllib.error
import urllib.request
from html import unescape
from datetime import datetime, timezone

USER = "AkshantVats"
PROFILE_REPO = "AkshantVats/AkshantVats"
BLOG_REPO = "AkshantVats/Profile"
BLOG_BASE = "https://akshantvats.github.io/Profile"
TRACKED_REPOS = [
    "AkshantVats/infra-ai-streaming",
    "AkshantVats/ebpf-llm-tracer",
    "AkshantVats/Profile",
]


def request_json(url):
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def request_text(url):
    req = urllib.request.Request(url, headers={"Accept": "text/plain"})
    with urllib.request.urlopen(req, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def ago(iso_timestamp):
    if not iso_timestamp:
        return "unknown"
    dt = datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - dt
    days = delta.days
    if days <= 0:
        hours = max(1, delta.seconds // 3600)
        return f"{hours}h ago"
    if days < 30:
        return f"{days}d ago"
    months = days // 30
    if months < 12:
        return f"{months}mo ago"
    return f"{days // 365}y ago"


def replace_section(readme, name, content):
    pattern = re.compile(
        rf"<!-- {re.escape(name)}:START -->.*?<!-- {re.escape(name)}:END -->",
        re.DOTALL,
    )
    replacement = f"<!-- {name}:START -->\n{content.strip()}\n<!-- {name}:END -->"
    if not pattern.search(readme):
        raise RuntimeError(f"Missing section marker: {name}")
    return pattern.sub(replacement, readme)


def repo_pulse():
    rows = []
    for full_name in TRACKED_REPOS:
        repo = request_json(f"https://api.github.com/repos/{full_name}")
        commits = request_json(f"https://api.github.com/repos/{full_name}/commits?per_page=1")
        latest = commits[0] if commits else {}
        commit_message = latest.get("commit", {}).get("message", "").splitlines()[0]
        commit_sha = latest.get("sha", "")[:7]
        pushed = ago(repo.get("pushed_at"))
        name = repo["name"]
        url = repo["html_url"]
        stars = repo.get("stargazers_count", 0)
        forks = repo.get("forks_count", 0)
        issues = repo.get("open_issues_count", 0)
        latest_cell = f"[`{commit_sha}`]({latest.get('html_url', url)}) {commit_message}" if commit_sha else "-"
        rows.append(
            f"| [{name}]({url}) | {stars} | {forks} | {issues} | {pushed} | {latest_cell} |"
        )
    return "\n".join(
        [
            "| Repo | Stars | Forks | Open issues | Last push | Latest commit |",
            "|---|---:|---:|---:|---:|---|",
            *rows,
        ]
    )


def extract_title(html, path):
    for pattern in [
        r"<h1[^>]*>(.*?)</h1>",
        r"<title[^>]*>(.*?)</title>",
    ]:
        match = re.search(pattern, html, re.I | re.S)
        if match:
            title = re.sub(r"<[^>]+>", "", match.group(1))
            title = " ".join(title.split())
            title = re.sub(r"\s*[·|-]\s*Akshant.*$", "", title)
            if title:
                return title
    return path.rsplit("/", 1)[-1].replace(".html", "").replace("-", " ").title()


def blog_posts(limit=5):
    repo = request_json(f"https://api.github.com/repos/{BLOG_REPO}")
    branch = repo.get("default_branch", "main")
    tree = request_json(
        f"https://api.github.com/repos/{BLOG_REPO}/git/trees/{branch}?recursive=1"
    ).get("tree", [])
    paths = [
        item["path"]
        for item in tree
        if item.get("type") == "blob"
        and item.get("path", "").startswith("blog/")
        and item.get("path", "").endswith(".html")
        and not item.get("path", "").endswith("index.html")
    ]

    def score(path):
        nums = [int(n) for n in re.findall(r"day-(\d+)|/(\d+)-", path) for n in n if n]
        return nums[-1] if nums else -1

    selected = sorted(paths, key=score, reverse=True)[:limit]
    if not selected:
        return "_No public blog posts found yet._"
    lines = []
    for path in selected:
        raw = f"https://raw.githubusercontent.com/{BLOG_REPO}/{branch}/{path}"
        try:
            html = request_text(raw)
            title = unescape(extract_title(html, path))
        except Exception:
            title = path.rsplit("/", 1)[-1].replace(".html", "").replace("-", " ").title()
        lines.append(f"- [{title}]({BLOG_BASE}/{path})")
    return "\n".join(lines)


def recent_activity(limit=6):
    try:
        events = request_json(f"https://api.github.com/users/{USER}/events/public?per_page=30")
    except urllib.error.HTTPError:
        return "_Recent activity unavailable from the GitHub API right now._"
    lines = []
    for event in events:
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name", "")
        repo_url = f"https://github.com/{repo}" if repo else "https://github.com/AkshantVats"
        created = ago(event.get("created_at"))
        if event_type == "PushEvent":
            commits = event.get("payload", {}).get("commits", [])
            msg = commits[-1].get("message", "").splitlines()[0] if commits else "pushed commits"
            lines.append(f"- `{created}` pushed to [{repo}]({repo_url}): {msg}")
        elif event_type == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type", "resource")
            lines.append(f"- `{created}` created {ref_type} in [{repo}]({repo_url})")
        elif event_type == "PullRequestEvent":
            action = event.get("payload", {}).get("action", "updated")
            pr = event.get("payload", {}).get("pull_request", {})
            title = pr.get("title") or f"pull request in {repo}"
            lines.append(f"- `{created}` {action} PR [{title}]({pr.get('html_url', repo_url)})")
        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action", "updated")
            issue = event.get("payload", {}).get("issue", {})
            lines.append(f"- `{created}` {action} issue [{issue.get('title', repo)}]({issue.get('html_url', repo_url)})")
        if len(lines) >= limit:
            break
    return "\n".join(lines) if lines else "_No recent public activity found yet._"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    with open(path, "r", encoding="utf-8") as handle:
        readme = handle.read()
    readme = replace_section(readme, "LIVE_REPO_PULSE", repo_pulse())
    readme = replace_section(readme, "LATEST_BLOG_POSTS", blog_posts())
    readme = replace_section(readme, "RECENT_ACTIVITY", recent_activity())
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(readme)


if __name__ == "__main__":
    main()
