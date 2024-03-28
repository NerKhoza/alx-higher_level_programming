#!/usr/bin/python3
"defines a function"


import requests
import sys


def get_commits(repository, owner):
  "function definition"
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error fetching commits:", response.status_code)


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(repository_name, owner_name)
