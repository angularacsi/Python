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