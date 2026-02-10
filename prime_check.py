x= int(input("enter the starting number: "))
y= int(input("enter the ending number: "))
count=0
i= 0
for i in range(x, y+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
            count= count+1
print("number of prime numbers between", x, "and", y, "is: ", count)