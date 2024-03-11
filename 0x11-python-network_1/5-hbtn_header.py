#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

url = sys.argv[1]
response = requests.get(url)
res = response.headers.get("X-Request-Id")
print(res)
