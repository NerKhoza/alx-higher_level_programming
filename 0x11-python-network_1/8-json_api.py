#!/usr/bin/python3
"defines a function"


import requests
import sys


def search_user(letter):
    "function definition"
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter} if letter else {}
    response = requests.post(url, data=params)

    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
