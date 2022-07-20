# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', 'wale': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users.copy().items())
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status#gives all active users to the new list
print(active_users)

print(list(range(2,20,5)))#first num is start,second is stop,third is increment
a=['wale', 'boy', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])
print(list(enumerate(a,start=1)))
print(6//4)#floor division returns only integer
print(6/4)#normal division
print(6%4)

for num in range(2, 10):
    if num % 2 == 0:
       print("Found an even number", num)
       continue
print("Found an odd number ", num)