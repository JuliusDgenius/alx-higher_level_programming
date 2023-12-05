#!/usr/bin/python3
"""A python script that takes ina letter and sends a POST request to
    'http://0.0.0.0:5000/search_user' with the letter as parameter.
"""
import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post(url, data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")