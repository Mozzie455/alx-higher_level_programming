#!/usr/bin/python3
"""Use the package request"""


def new_func():
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)


if __name__ == "__main__":
    import sys
    import requests

    new_func()
