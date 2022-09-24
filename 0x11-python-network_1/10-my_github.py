#!/usr/bin/python3
"""
Takes your Github credentials and uses the GitHub API
to dispaly your ID.
"""

from sys import argv

import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
