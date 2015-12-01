# fname = raw_input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

# fh = open(fname)
# count = 0
# for line in fh:
#     line = line.strip()
#     if line != '':
#         words = line.split('\n') 
#     for word in words:
#         word = word.split() 
#         if word[0]!= 'From' : 
#             continue
#         count = count + 1
#         print word[1]

# print "There were", count, "lines in the file with From as the first word"


# #####Alternative###### #

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    word = line.split()
    if word == [] : continue  #safe guard that skips empty line
    if word[0]!= 'From' : 
        continue
    count = count + 1
    print word[1]

print "There were", count, "lines in the file with From as the first word"

