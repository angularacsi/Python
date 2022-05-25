sh=input("Enter the working hour: ")
sr=input("enter the rate : ")
try:
    fh=float(sh)
    fr=float(sr)
except:
    print("please enter numeric values ")
    quit()
     

if fh > 40:
    rp=fh*fr
    ep=(fh-40.0)*(fr*0.5)
    total=rp+ep
    print(total)
else:
    print(fh*fr)