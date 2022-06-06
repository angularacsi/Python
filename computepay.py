
def pay(hours,rate):
    if hours > 40:
        rp=hours*rate
        ep=(hours-40.0)*(rate*0.5)
        total=rp+ep
        return total
        
    else:
        return(hours*rate)
 
sh=input("Enter the working hour: ")
sr=input("enter the rate : ")
fh=float(sh)
fr=float(sr)

pays=pay(fh,fr)
print(pays)



