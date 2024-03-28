#!/usr/bin/python3
"Python script that takes in a URL and an email"


import urllib.parse
import urllib.request
import sys

if len(sys.argv) < 3:
    print("Usage: python 2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')
with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print("Your email is:", email)
    print(body)
