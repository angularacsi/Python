(x,y)=(4,5)
print(x)#tuples are unchangable at all
data=dict()
data['age']=25
data['hight']=150
for (x,y) in data.items():
    print(x,y)
tups=data.items()
print(tups)
print((1,3,5)<(6,9,8))# we can compare tuples true
print((0,10,500)<(1,30,23))
d={'a':10,'c':1,'b':12}
print(sorted([(v,k) for k,v in d.items()]))
print(d.items())
print(sorted(d.items())) #sorted based on keys
tmp=list()
for (k,v) in d.items():
    tmp.append((v,k))
print(tmp)#prints the reverse list of the above data
tmp=sorted(tmp,reverse=True)
print(tmp)# sorted by value

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
days.index()