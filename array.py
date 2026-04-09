x=eval(input("Enter the values: "))
y=0
z=100
print(type(x))
for i in x:
    if i > y:
        y = i
    if i < z:
        z = i
print("the highest temperature is: ",y)
print("the lowest temperature is: ",z)
print("the average temperature is: ",int(sum(x)/len(x)))