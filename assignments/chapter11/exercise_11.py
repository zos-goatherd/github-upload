#!/usr/bin/env python3

import re


filename = input('Enter a file')
num_matcher = re.compile(r"[0-9]+")
if len(filename) < 1:
    filename = 'regex_sum_42.txt'

with open(filename) as handler:
    text = handler.read()
    nums = re.findall(num_matcher, text)


sum = 0
if len(nums) > 0:
    for number in nums:
        sum += int(number)

print('There are: ', len(nums))
print('The total is ', sum)
