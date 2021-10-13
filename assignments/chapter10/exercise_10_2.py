#!/usr/bin/env python

# Exercise 1 from py4e chapter on tuples, builds on the previous chapters exercise that read the file and put the senders and the number of emails sent in a dictionary

filename = input('Enter a file: ')
if len(filename) < 1:
    filename = 'mbox-short.txt'
handler = open(filename)


hours= dict()
for line in handler:
    words = line.split()
    if len(words) < 6 or words[0] != 'From': continue
    sendername = words[1]
    time = words[5]
    hour = time.split(':')
    hour_string = hour[0]
    hours[hour_string] = hours.get(hour_string, 0) + 1


loft = list()
 
# this is the new part
for time_of_day, msg_in_hr in hours.items():
     loft.append( (time_of_day, msg_in_hr) )

loft = sorted(loft)
for time_of_day, msg_in_hr in loft:
    print(time_of_day, msg_in_hr)

