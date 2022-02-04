#!/usr/bin/python3
''' Python for Everybody chapter 7 exercise 2 '''


myFile = input('Enter a file name: ')
MATCH = "X-DSPAM-Confidence:"
total = 0.0
number = 0
try:
    fhand = open(myFile)
except:
    print("Oops, file can't be opened:", myFile)
    exit()
for line in fhand:
    if line.startswith(MATCH):
        delim = line.find(':')
        numstr = line[delim+1:]
        number = number + 1
        total = float(numstr) + total

print("Average spam confidence:", total/number)
fhand.close()
