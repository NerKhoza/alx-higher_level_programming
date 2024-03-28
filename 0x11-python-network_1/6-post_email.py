#!/usr/bin/python3
#  Python script that takes in a URL and an email address


import requests
import sys


def main():
    "function defination"
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        return

    url = sys.argv[1]
    email = sys.argv[2]

    print(f"Your email is: {email}")

    response = requests.post(url, data={'email': email})

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
