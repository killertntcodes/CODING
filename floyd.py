x=int(input("enter the number of rows: "))
y=1
for i in range(x):
    for j in range(i+1):
        print(y , end="")
        y=y+1
    print()