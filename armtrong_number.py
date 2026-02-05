x=int(input("Enter a number: "))
y=0
temp=x
while temp>0:
    digit=temp%10
    y+=digit**3
    temp//=10
if x==y:
    print(f"{x} is an armstrong number")
else:
    print(f"{x} is not an armstrong number")