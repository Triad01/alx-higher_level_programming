#!/usr/bin/python3
# script fetches a url using requests package

import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t -type:", format(type(response.text)))
    print(f"\t -content: OK".format(response.text))
