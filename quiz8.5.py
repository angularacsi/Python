
count=0
fname=input("Enter a file name")
fhand=open(fname)
for line in fhand:
    if line.startswith("From"):#this method is for starting of the word 
        if line.startswith('From: '):#we can use like this line.starswitch("from",3,20) begin and end
            continue
        else:
            count=count+1
            listz=line.split()
            print(listz[1])
print("There were", count, "lines in the file with From as the first word")