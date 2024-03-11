#!/usr/bin/python3
# Script takes GitHub credentials (username and personal access token)
# and uses the GitHub API to display the user's id.

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Construct the URL for the GitHub API
    url = "https://api.github.com/user"

    # Set up Basic Authentication with username and personal access token
    auth = (username, password)

    # Send GET request to GitHub API with Basic Authentication
    response = requests.get(url, auth=auth)

    # Check if request was successful
    if response.status_code == 200:
        # Extract and print user's id
        user_id = response.json().get("id")
        print(user_id)
    else:
        # Print None if request failed
        print(None)
