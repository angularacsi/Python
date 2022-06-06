
small=None
items=[2,5,8,45,12,9,10]
for item in items:
    if small is None:# is use for None operator
        small=item
    elif item<small:
        small=item
print(small)