x=int(input("enter the number of rows: "))
if x%2==0:
    hdrow=int(x/2)
else:
    hdrow=int(x/2)+1
space= hdrow-1
for i in range(1,hdrow+1):
    for j in range(1,space+1):
        print(end=" ")
    space= space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,hdrow):
    for j in range(1,space+1):
        print(end=" ")
    space= space+1
    num=1
    for j in range(1,2*(hdrow -i)):
        print(end=str(num))
        num=num+1
    print()