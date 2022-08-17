class A:
    def __init__(self):
        print("init in the main class")
    def feature1(self):
        print("this is main class")
    def feature2(self):
        print("this also the main class")
class B(A):#this is the sub class inherited from the main class
    def __init__(self):
        super().__init__() # we are calling the super class
        print("init in the sub class ")
    def feature3(self):
        print("this is sub class")
    def feature4(self):
        print("this also the sub class")


b1=B() #prints all init methods due to super method