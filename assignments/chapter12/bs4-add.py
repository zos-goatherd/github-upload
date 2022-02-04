#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# define variable to use to accumulate the total
total = 0
count = 0
# choose the url to perform operations on
target = input('Enter the url: ')
if len(target) < 1:
    target = 'http://py4e-data.dr-chuck.net/comments_42.html '

# Ignore SSL certificate errors, copied from urllink2.py
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# this copies the entire target html file
html_data = urlopen(target, context=ctx).read()

# gives the html to BeautifulSoup to parse (as html rather than as xml)
soup = BeautifulSoup(html_data, "html.parser")

# specify the type of tag we are interested in extracting data from
tags = soup('span')

for tag in tags:
    # if I was doing this for real I would put this in a try statement
    total += int(tag.contents[0])
    count += 1

print("Count ", count)
print("Sum ", total)
