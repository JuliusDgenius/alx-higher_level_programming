#!/bin/bash
# server prints you got me
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" http://0.0.0.0:5000/catch_me
