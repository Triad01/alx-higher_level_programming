#!/usr/bin/python3
"""Script takes a url and en email
and sends a POST request to the url,
displays the body of the response, in decoded form
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    with urllib.request.urlopen(url, data=data) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
