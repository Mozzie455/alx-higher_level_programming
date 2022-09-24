#!/usr/bin/python3
"""Script that sends a POST request with data in the variable q"""

from sys import argv

import requests

def new_func(__name__):
    if __name__ == '__main__':
        url = "http://0.0.0.0:5000/search_user"
        data = {"q": argv[1][0] if len(argv) > 1 else ""}
        response = requests.post(url, data=data)
        try:
            d = response.json()
            if not d:
                print("No result")
            else:
                print("[{}] {}".format(d.get("id"), d.get("name")))
        except ValueError:
            print("Not a valid JSON")

new_func(__name__)
