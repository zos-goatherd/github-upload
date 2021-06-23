#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Valid scores are between 0.0 and 1.0")
scoreStr = input("Enter a score: ")
try:
    score = float(scoreStr)
except:
    score = -1.0
if (score < 0.0) or (score > 1.0):
    print("Bad score")
elif score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 0.6 :
    print("D")
else :
    print("F")

 
