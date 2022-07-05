 
while True:
    sval=input("enter the value :")
    if sval=='done':
        break
    try:
        fval=int(sval)
    except:
        print("Invalid input ")
        continue
    small=min(fval)
    largest=max(fval)
 
print(small,largest)