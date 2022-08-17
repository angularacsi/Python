import re
strg="wale 2 with regx 20 and find 32 "
y=re.findall('[0-9]+',strg)
print(y)

y="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

print(re.findall('[..@\S+..]+',y))

print(re.findall('F.+:',y))
print(re.findall('\S+?@\S+',y))




