n=5

while n>0:
    print(n)
    n=n-1
print("the condution out of loop")
print(n)


while True:
    lan=input()
    if lan =='done':
        break
    print(lan)
print("loop break")

for i in [5,4,3,2,1]:
    print(i)


friends=['almaz','sewale','ayenew','shituye']
for friend in friends:
    print("Dear " + friend,"happy new year")




#the largest number

lists=[45,34,67,23,12,86,86]

max=0
for large in lists:
    if large>max:
        max=large

print("the largest number is " ,max) 

#count the list contents

cont=0
for thing in [2,4,5,3,1,7,9,9]:
    cont=cont+1
    print(cont,thing)
print("the total value is ",cont)
 
sums=1
list1=[2,4,5,3,1,7,9,9]
for value in list1:
     sums =value + sums
print(sums)


