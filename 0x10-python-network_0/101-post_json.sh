#!/bin/bash
# Sending JSON POST request to a URL passed as the first argument & displays the body of the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
