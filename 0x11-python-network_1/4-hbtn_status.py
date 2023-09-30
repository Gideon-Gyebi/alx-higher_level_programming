#!/usr/bin/python3
"""
What's my status?
"""
import requests


def main():
    """
    This fetches https://intranet.hbtn.io/status
    """
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))


if __name__ == "__main__":
    main()
