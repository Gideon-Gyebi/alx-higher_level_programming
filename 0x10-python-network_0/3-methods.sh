#!/bin/bash
# Taking in a URL & displays all HTTP methods the server will accept
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
