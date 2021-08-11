#!/usr/bin/env python3

words = list()
count = 0
# open file 
fhand = open('romeo.txt')
for line in fhand:
    line = line.rstrip()
    linewords = line.split()
    if len(line) == 0: continue 
    for i in range(len(linewords)):
        if linewords[i] in words: continue 
        words.append(linewords[i]) 

count = len(words)
print("number of words: ", count)
print("They are in order: ")
words.sort()
for word in words:
    print(word)
