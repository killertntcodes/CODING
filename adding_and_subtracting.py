def suming( a,b):
    c=a+b
    return c
def subing( n,i):
    d=n-i
    return d
x=int(input("enter what u would like to do (addition=1, subtraction=2): "))
if x==1:
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    print("the sum is: ", suming(a,b))
elif x==2:
    n=int(input("enter the first number: "))
    i=int(input("enter the second number: "))
    print("the difference is: ", subing(n,i))
else:
    print("invalid input")