name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
count = 0
count_senders = dict()
for line in fh:
    words = line.split()
    if words == [] : continue  #safe guard that skips empty line
    if words[0]!= 'From' : 
        continue

    for word in words:
        if '@' not in word : continue
        count_senders[word] = count_senders.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in count_senders.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count 

print bigword, bigcount
