#!/usr/bin/env python3
"""
Parsing XML Assignment from py4e.com Chapter 13 Using Web Services
Jonas Bird
<2021-01-03>
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

total = 0
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_1226411.xml'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urlHandle = urllib.request.urlopen(url, context=ctx)
xmlData = urlHandle.read()
tree = ET.fromstring(xmlData)
counts = tree.findall('.//count')
for count in counts:
    total += int(count.text)
print(total)
