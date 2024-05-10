#!/usr/bin/python3
"""POST an email"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
