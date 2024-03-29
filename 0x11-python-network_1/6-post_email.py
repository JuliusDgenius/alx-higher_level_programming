#!/usr/bin/python3
"""Python script that takes a URL and email address, sends a POST
    request to the passed URL with the email as a parameter, and
    finally displays the body of the response.
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    val = sys.argv[2]

    r = requests.post(url, data={'email': val})
    print(r.text)
