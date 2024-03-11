#!/usr/bin/python3
"""
    Module implementing a script that takes a url
    sends a request to the url and displays the value
    of the X-Request-Id
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.headers.get("X-Request-Id")
        print(x_request_id)
