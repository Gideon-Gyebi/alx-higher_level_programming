#!/usr/bin/python3
"""
Error code
"""
import urllib.request
from sys import argv


def main(argv):
    """
    This manage urllib.error.HTTPError exceptions
    print: Error code: followed by the HTTP status code
    """
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main(argv)
