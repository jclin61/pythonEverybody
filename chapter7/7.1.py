dataname = raw_input('Enter the file name: ')
if len(dataname) == 0:
    dataname = 'mbox-short.txt'
data = open(dataname)
for line in data:
    line = line.rstrip()
    print line.upper()
