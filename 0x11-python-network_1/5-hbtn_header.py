#!/usr/bin/python3


import requests
import sys

def get_x_request_id(url):
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    return x_request_id

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    print(x_request_id)
