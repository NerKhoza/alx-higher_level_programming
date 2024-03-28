#!/usr/bin/python3
#   Python script that fetches a status

import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)

if response.status_code == 200:
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
else:
    print("Error fetching URL:", response.status_code)
