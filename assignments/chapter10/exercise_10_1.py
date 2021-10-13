#!/usr/bin/env python

# Exercise 1 from py4e chapter on tuples, builds on the previous chapters exercise that read the file and put the senders and the number of emails sent in a dictionary

filename = input('Enter a file: ')
if len(filename) < 1:
    filename = 'mbox-short.txt'
handler = open(filename)

senders = dict()
for line in handler:
    words = line.split()
    if len(words) < 1 or words[0] != 'From': continue
    sendername = words[1]
    senders[sendername] = senders.get(sendername, 0) + 1

# this is the new part
loft = list()
for sen, msgnum in senders.items():
    loft.append( (msgnum, sen) )

loft = sorted(loft, reverse=True)

print(loft[0])
