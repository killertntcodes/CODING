x= int(input("enter a number: "))
t=x
xlen=0
while t > 0:
    xlen= xlen+1
    t= t//10
if xlen>=4:
    xlen= int(xlen/2)
    chk= 0
    while x>0:
        rem= x%10
        if chk== xlen:
            mid1= rem
        elif chk==(xlen-1):
            mid2= rem
        x=int(x/10)
        chk= chk+1
    prod= mid1*mid2
    print("the product of the middle two digits is: ", prod)
else:
    print("the number does not have two or more middle digits")