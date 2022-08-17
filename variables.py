a=10 #globale variable
def domains():
    global a # here a takes this value in every where the global also this
    x=globals()['a']#returns all the global values
    print(id(x))# prints the address of the variable
    print(id(a))

    a=15 #local variable
    print("Inside the function",a)

domains()
print("outside the function",a)