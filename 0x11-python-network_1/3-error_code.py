#!/usr/bin/python3
"""Send EMAIL"""
import sys
import urllib.error
import urllib.request


def new_func(__name__):
    if __name__ == "__main__":
        url = sys.argv[1]

        request = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(request) as response:
                print(response.read().decode("ascii"))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))

new_func(__name__)