a=4
b=2
try:
    print(a/b)
    k=int(input("Enter the number"))
    print(k)

except ZeroDivisionError as e:
    print("impossible action",e)
except ValueError as e:
    print("Invalid input",e)
except Exception as e:
    print("Something wrong...",e)
finally:
    print("resource closed")