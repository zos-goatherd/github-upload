#!/usr/bin/env python3
"""
Exercise Extracting Data from JSON from Python for Everybody Chapter 13
Jonas Bird
<2021-01-03>
"""
import urllib.request, urllib.parse, urllib.error
import json
import ssl

TEST_URL = "http://py4e-data.dr-chuck.net/comments_42.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def parse_json(jdata):
    total = 0
    for comment in jdata['comments']:
        total += int(comment['count'])
    return total


def get_json(json_url):
    uhandle = urllib.request.urlopen(json_url, context=ctx)
    return uhandle.read()


def main():
    url_to_call = input("Please enter the url to retrieve(leave blank for test data): ")
    if len(url_to_call) < 1:
        url_to_call = TEST_URL
    data = get_json(url_to_call)
    jdata = json.loads(data)
    print("The total number of comments: ", parse_json(jdata))


if __name__ == "__main__":
    main()
