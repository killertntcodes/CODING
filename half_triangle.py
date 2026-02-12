x=int(input("enter the number of rows: "))
y="*"
for i in range(x):
    for j in range(i+1):
         print("* ", end="")
    print()