#!/usr/bin/python3
"""HTTPError code"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.Request(url) as responce:
            print(responce.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if hasattr(e, "code"):
            print("Error code: {}".format(e.code))
