#!/usr/bin/python3
"""
Script that takes a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.error
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request(req) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))