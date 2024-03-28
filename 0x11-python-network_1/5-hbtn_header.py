#!/usr/bin/python3


import requests
import sys


def get_request_id(url):
    try:
        response = requests.get(url)
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            return request_id
        else:
            return "X-Request-Id header not found in the response"
    except requests.RequestException as e:
        return f"Error making request: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = get_request_id(url)
    print(request_id)
