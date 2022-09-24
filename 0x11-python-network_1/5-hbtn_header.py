#!/usr/bin/python3
"""the package request"""

def new_func(__name__):
    if __name__ == "__main__":
        import requests
        import sys

        r = requests.get(sys.argv[1])
        print(r.headers.get('X-Request-Id'))


new_func(__name__)
