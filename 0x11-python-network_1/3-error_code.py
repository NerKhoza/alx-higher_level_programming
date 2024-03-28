#!/usr/bin/python3
"Python script that takes in a URL"


import urllib.request
import urllib.error
import sys


def fetch_url(url):
"function definition"

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url)
