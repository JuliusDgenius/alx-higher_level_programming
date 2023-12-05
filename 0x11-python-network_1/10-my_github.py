#!/usr/bin/python3
"""
A python script that takes your GitHub username and password
and uses the GitHub API to display your id.
"""
import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user/pass'

    r = requests.get(url, auth=(username, password))
    print(dir(r.text))
