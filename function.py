def Print():
    print("hello functions")


Print()

#passing arguments

def greet(lang):
    if lang=="us":
        print("english")
    elif lang=='fr':
        print("france")
    elif lang=='amharic':
        print("selam")
    else:
        print("not alanguage")


greet("amharic")

      
#return statmen

def returnVal():
    return "hello man" #return may also imlicitly added at the end of functions


print(returnVal(),"wale how are you")

def add(a,b):
    reslt=a+b
    return reslt


print(add(3,5),"is the result")


astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)

def person(name,age=20):#default arguments
    print(name,age)


person('wale',27) #position argument
person(age=26,name="tadese")

def sums(*b):#variable length arguments
    c=0
    for i in b:
        c=c+i
    print(c)


sums(6,8,34,12,45)