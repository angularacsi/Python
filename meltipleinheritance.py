class A:
    def __init__(self):
        print("init in the main A class")
    def feature1(self):
        print("this is main A class")
    def feature2(self):
        print("this also the main A class")
class B: 
    def __init__(self):
        super().__init__()  
        print("init in the main B class ")
    def feature2(self):
        print("this is main B class")
    def feature4(self):
        print("this also the main B class")
class C(A,B): 
    def __init__(self):
        super().__init__()  
        print("init in the sub C class ")
    def feature3(self):
        print("this is sub C class")
    def feature6(self):
        # super().feature2( ) #calling the method in the main class
         super().feature4()


b1=B() #prints all init methods due to super method
c1=C()
c1.feature6()
c1.feature2() #the same function name and it calls by order of function