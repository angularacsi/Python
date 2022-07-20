fname=input("enter the file name")
fhan=open(fname)
list1=list()
for line in fhan:
    for word in line.split():
        if word in list1:
            continue
        else:
            list1.append(word)
list1.sort()
print(list1)
