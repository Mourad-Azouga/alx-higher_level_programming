#!/usr/bin/python3
"""A script
- takes in a URL,
- sends a request to the URL and
- disp  X-Request-Id var found in the header.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
