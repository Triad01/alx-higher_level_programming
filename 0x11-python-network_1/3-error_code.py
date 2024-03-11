#!/usr/bin/python3
# script takes in a URL, sends a request to the URL
# and displays the body of the response (decoded in utf-8).

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body_response = response.read()
            print(body_response.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
