#!/usr/bin/python3
"""Python script that takes 2 args in order to list 10 commits
    (from the most recent to the oldest) of the repository "rails"
    by the user "rails"
"""
import sys
import requests


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url =  'https://api.github.com/repos/{}/{}/commits'.format(
        repo_name, owner_name)

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
