fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

mydic = dict()
for lin in hand:
lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        mydic[w] = mydic.get(w, 0) + 1


# now that we have the frequency of each word we need to find the most
# common word
largest = -1
theword = None
for k, v in mydic.items():
    if v > largest:
        largest = v
        theword = k
print(theword, "appears ", largest, " times")

