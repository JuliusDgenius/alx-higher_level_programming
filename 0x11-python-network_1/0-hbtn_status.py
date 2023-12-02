#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status
import urllib.request

with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status'
            ) as response:
    html = response.read()
print("Body content:")
print("\t- type: ", html.__class__)
print("\t- content: ", html)
print("\t- utf8 content: ", html.decode())
