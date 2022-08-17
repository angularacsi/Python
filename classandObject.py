class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is ",self.cpu,self.ram)

com1=computer("core i7","4gb")
com2=computer("core i5","8gb")

com1.config()
com2.config()

class man:

    sex="male" #class variable(static variable)
    def __init__(self): #function used to declar avariables
        self.name="wale" #instance variables
        self.age=27
    
    def compare(self,other): #method used to compare the value
        #self is the calling object and other is the argument object
        if self.age==other.age:
            return True
        else:
            return False

m1=man()
m2=man()
#m1.age=30   update the value
man.sex="female" #use the class to change class variable and affects all object

if m1.compare(m2):# calling the function and comparing the values &passing object as argument 
    print("they are the same")
else:
    print("they are different")
        


         