#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8). Handles HTTP errors and prints
the error code if encountered."""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
