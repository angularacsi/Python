class student:
    school="Gelila"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avrg(self): #instance method
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def schoolinfo(cls): # class method
        print(cls.school)

    @staticmethod
    def info():#independant of all method type static method
        print("outside of all method types")

s1=student(34,56,78)
s2=student(23,54,76)
s3=student(12,34,65)

print(s1.avrg())       
print(student.school)
student.info()