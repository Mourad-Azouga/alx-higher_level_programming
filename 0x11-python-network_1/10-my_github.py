#!/usr/bin/python3
"""a little python stuffy that does
- takes in a URL,
- sends a request to the URL
-displays X-Request-Id var found in the header res.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
