#!/bin/bash
# Sending a request to a URL passed as an argument & displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
