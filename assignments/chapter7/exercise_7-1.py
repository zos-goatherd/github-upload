#!/usr/bin/python3
# Python for Everybody chapter 7 exercise 1


myFile = input('Enter a file name: ')
try:
    fhand = open(myFile)
except:
    print("Oops, file can't be opened:", myFile)
    exit()
for line in fhand:
    print(line.upper())
fhand.close()
