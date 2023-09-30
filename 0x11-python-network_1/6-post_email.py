#!/usr/bin/python3
"""
POST an email
"""
import requests
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL, email as a parameter,
    and displays the body of the response
    [decoded in utf-8]
    """
    values = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=values)
    print(r.text)


if __name__ == "__main__":
    main(argv)
