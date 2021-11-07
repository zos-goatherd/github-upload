#!/usr/bin/env python3

import re

filename = input('Enter a file')
if len(filename) < 1:
    filename = 'regex_sum_42.txt'
hours = dict()
with open("filename") as handler:
    for lines in handler:
