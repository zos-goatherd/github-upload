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

most = -1
topsender = None
for k, v in senders.items():
    if v > most:
        most = v
        topsender = k
# print("You have recieved ", most, " emails from ", topsender)
print(topsender, most)
