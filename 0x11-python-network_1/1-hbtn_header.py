#!/usr/bin/python3
"""Takes a URL, sends req and displays the value of the X-Request-Id
    variable found in the header of the response.
"""

import urllib.request
import sys

url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
