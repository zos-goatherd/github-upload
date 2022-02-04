#!/usr/bin/python3
''' Use find and string slicing to extract the portion of the string after
 the colon and convert it to a floating point value'''

str = 'X-DSPAM-Confidence:0.8475'
delim = str.find(':')
numstr = str[delim+1:]
num = float(numstr)
print(num)
