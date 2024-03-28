#!/usr/bin/python3
"defines a function"


import requests
import sys


def get_github_id(username, token):
    "function definition"
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        return None


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    github_id = get_github_id(username, token)
    print(github_id)
