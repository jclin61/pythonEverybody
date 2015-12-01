fname = raw_input("Enter file name: ")
if fname == "":
    fh = open('romeo.txt')
else:
    fh = open(fname)
paragraph = fh.read()
texts = paragraph.split()

lst = list()
for text in texts:
    if text not in lst:
        lst.append(text)

lst.sort()
print lst
