#!/usr/bin/python3
"""Take a URL, sends requests ans analyzes HTTP status code"""

import sys
import requests


def new_func(__name__):
    if __name__ == "__main__":
        url = sys.argv[1]

        r = requests.get(url)
        if r.status_code >= 400:
            print("Error code: {}".format(r.status_code))
        else:
            print(r.text)

new_func(__name__)
