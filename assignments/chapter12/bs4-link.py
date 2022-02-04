#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

start = input('Enter - ')
url = list()
url.append(start)
position = int(input('Enter link position: '))
repeat = int(input('Enter number of repetitions: '))
if len(url[0]) < 1:
    url[0] = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
    position = 3
    repeat = 4

for i in range(repeat + 1):
    print('Retrieving: ', url[i])
    html = urlopen(url[i], context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    link = tags[position - 1]
    url.append(link.get('href', None))
