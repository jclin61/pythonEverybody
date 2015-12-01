name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
count = 0
count_hours = dict()
for line in fh:
    words = line.split()
    if words == [] : continue  #safe guard that skips empty line
    if words[0]!= 'From' : 
        continue

    for word in words:
        if ':' not in word : continue
        hour = word[0:2]  #to extra hour only
        count_hours[hour] = count_hours.get(hour, 0) + 1   #add count to each hour

lst = list()   #create an empty list for sort method
for key, val in count_hours.items():    #to extract key and values from dict into list for sorting
    lst.append((key, val))    
lst.sort()  #sorting!
for key, val in lst:   #to loop through each key and val for printing
    print key, val
