x=eval(input("enter the first tuple: "))
y=eval(input("enter the second tuple: "))
print("the product of the two tuples is: ", tuple(a*b for a in x for b in y))