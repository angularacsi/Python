file1=open("code.txt","r") #open file inread format
#print(file1.read()) displays the whole data
print(file1.readline(),end="")# displays one line it adds new line
print(file1.readline())# displays one line

file2=open("write_here","w") #creates the file with txe
file2.write("This is the new content added to this file")