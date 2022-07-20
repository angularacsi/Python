list1=['kebed','alemu','aster']
list2=[2,3,6,8]
list3=['red','yellow',4,8]
list4=[1,2,[5,6],8,9] #with 5 elements
print(len(list4))
list1.extend(list3) #add together
a=[2,4,5,8,0]
b=[10,20,4,]
print(a+b) #adding lists
print(b+list4)
print(a)
print(20 in a) #false answer
list1.sort()
print(list1) #sorted lists
print("Maximum value :=",max(a))
print("minimum value :=",min(a))
print("the sum of elements :=",sum(a))
print("avarege value of the elements :=",sum(a)/len(a)) #avarage
data="how to split the strings"
splits=data.split()
print(splits)
print(len(splits))
print(splits[4])
split2=data.split(';')
print(split2)