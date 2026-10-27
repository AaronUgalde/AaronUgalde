"""Rewrite the "Lately" block in README.md with my most recently pushed public repos."""
import datetime
import json
import os
import re
import urllib.request

USER = os.environ.get("GITHUB_USER", "AaronUgalde")
SKIP = {USER}
LIMIT = 5
README = "README.md"


def fetch_repos():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=30&type=owner",
        headers={"Accept": "application/vnd.github+json"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def ago(iso):
    days = (datetime.datetime.now(datetime.timezone.utc) - datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))).days
    if days == 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 30:
        return f"{days} days ago"
    return datetime.date.fromisoformat(iso[:10]).strftime("%b %Y")


def render(repos):
    lines = []
    for r in repos:
        if r["fork"] or r["archived"] or r["name"] in SKIP:
            continue
        parts = [f'[{r["name"]}]({r["html_url"]})']
        if r["description"]:
            parts.append(r["description"].strip().rstrip("."))
        meta = " · ".join(x for x in (r["language"], ago(r["pushed_at"])) if x)
        lines.append(f'- {" · ".join(parts)} <sub>{meta}</sub>')
        if len(lines) == LIMIT:
            break
    return "\n".join(lines)


def main():
    with open(README, encoding="utf-8") as f:
        text = f.read()
    block = f"<!-- recent:start -->\n{render(fetch_repos())}\n<!-- recent:end -->"
    text = re.sub(r"<!-- recent:start -->.*?<!-- recent:end -->", lambda _: block, text, flags=re.S)
    with open(README, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
