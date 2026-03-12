x=eval(input("enter a tuple: "))
pal=True
for i in range(len(x)):
    if x[i]!=x[len(x)-1-i]:
        pal=False
        break
if pal:
    print("the tuple is a palindrome")
    print("the reverse of the tuple is: ", x[::-1])
else:
    print("the tuple is not a palindrome")