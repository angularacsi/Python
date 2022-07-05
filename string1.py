fruit="banana"
print(fruit[1])
x=3
print(fruit[x-1])
print(len(fruit))
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
for char in fruit:
    print(char)

count=0
for chars in fruit:
    if chars=='a':
        count=count+1
print(count)

for letters in "walelign":
    print(letters)

name="ayenewtilaye"
print(name[0:5])
print(name[:6])
print(name[0:50])