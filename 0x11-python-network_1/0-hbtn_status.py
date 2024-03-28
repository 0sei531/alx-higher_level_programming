#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib."""

from urllib import request, error

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except error.URLError:
        print("Cannot connect to https://alx-intranet.hbtn.io/status")
