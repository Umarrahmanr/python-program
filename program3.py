def big():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=int(input("enter a number"))
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
print("the biggest number is:",big()) 
