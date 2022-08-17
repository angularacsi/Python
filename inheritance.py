class A:
    def __init__(self):
        print("init in the main class")
    def feature1(self):
        print("this is main class")
    def feature2(self):
        print("this also the main class")
class D:
    def feature1(self):
        print("this is main class")
    def feature2(self):
        print("this also the main class")

class B(A):#this is the sub class inherited from the main class
    def __init__(self):
        print("init in the sub class class")
    def feature3(self):
        print("this is sub class")
    def feature4(self):
        print("this also the sub class")
class c(D,B):# inherit from both D and B class
    def feature5(self):
        print("this also the sub sub  class") #multi level inheritance


a1=A()
b1=B()# we can call all function by this object
c1=c()

a1.feature1()
a1.feature2()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
c1.feature5()
