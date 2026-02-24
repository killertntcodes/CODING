def suming( a,b):
    c=a+b
    return c
def subing( n,i):
    d=n-i
    return d
def muling( m,o):
    e=m*o
    return e
def diving( p,q):
    f=p/q
    return f
x=int(input("enter what u would like to do (addition=1, subtraction=2, multiplication=3, division=4): "))
if x==1:
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    print("the sum is: ", suming(a,b))
elif x==2:
    n=int(input("enter the first number: "))
    i=int(input("enter the second number: "))
    print("the difference is: ", subing(n,i))
elif x==3:
    m=int(input("enter the first number: "))
    o=int(input("enter the second number: "))
    print("the product is: ", muling(m,o))
elif x==4:
    p=int(input("enter the first number: "))
    q=int(input("enter the second number: "))
    print("the quotient is: ", diving(p,q))
else:
    print("invalid input")