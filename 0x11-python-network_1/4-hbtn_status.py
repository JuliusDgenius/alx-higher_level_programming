#!/usr/bin/python3
"""A python script that fetches 'https://alx-intranet.hbtn.io/status'
"""
import requests


if __name__ == '__main__':
    request = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(request.text))
    print("\t- content:", request.text)
