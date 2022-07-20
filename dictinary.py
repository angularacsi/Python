data1=dict()
data1['age']=35
data1['hight']=42.5
data1['width']=62

print(data1)

counts=0
print("enter the line of text")
line=input('')
words=line.split()
print(words)
for word in words:
    counts[word]=counts.get(word,0)+1
print("counts",counts)

count1={1.5:"One and Half", 2.5: "Two and Half", 3.5:"Three and Half"}
 