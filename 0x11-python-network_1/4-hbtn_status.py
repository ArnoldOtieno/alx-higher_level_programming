#!/usr/bin/python3
"""fetching url"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(body)))
        print("\t - content: {}".format(body.decode("utf-8")))
