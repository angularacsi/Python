cont=0
big=0
big=float(big)
fname=input("enter the file name")
fh=open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        a=float(line[20:26])
        big=big+a
        cont=cont+1
print("Average spam confidence:",big/cont)