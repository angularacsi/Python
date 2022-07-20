file1=open("code.txt","r") #open file inread format
#print(file1.read()) displays the whole data
print(file1.readline(),end="")# displays one line it adds new line
print(file1.readline())# displays one line

file2=open("write_here","w") #creates the file with txe
file2.write("This is the new content added to this file")

fhand = open('code.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)

filename=input("enter the file name : ")
data1=open(filename)
for line1 in data1:
     ly=line1.rstrip()
     print(ly.upper())

