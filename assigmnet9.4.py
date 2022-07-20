fname=input("enter the name of file")
fhand=open(fname)
dict=dict()
list1=list()
for line in fhand:
    if line.startswith("From"):
        if line.startswith("From: "):
            continue
        else:
            word=line.split()
            list1.append(word[1])
for word in list1:
    dict[word]=dict.get(word,0)+1
HC=None
HCW=None
for emailid,senttimes in dict.items():
    if HC is None or senttimes >HC:
        HCW=word
        HC=senttimes
print(HCW,HC)