#!/usr/bin/python3
"""
Search API
"""
import requests
from sys import argv


def main(argv):
    """
    This script takes in a letter and sends a POST request
    to the URL with the letter as a parameter.
    """
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)
    try:
        result = r.json()
        if bool(result) is False:
            print("No result")
        else:
            print("[{}] {}".format(result['id'], result['name']))
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    main(argv)
