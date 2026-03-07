x=[1, 2, 3, 4, 5]
print(sum(x))
print("the average of the list is:", sum(x)/len(x))
if x[0]>x[1] and x[0]>x[2] and x[0]>x[3] and x[0]>x[4]:
    print("the maximum value in the list is:", x[0])
elif x[1]>x[0] and x[1]>x[2] and x[1]>x[3] and x[1]>x[4]:
    print("the maximum value in the list is:", x[1])
elif x[2]>x[0] and x[2]>x[1] and x[2]>x[3] and x[2]>x[4]:
    print("the maximum value in the list is:", x[2])
elif x[3]>x[0] and x[3]>x[1] and x[3]>x[2] and x[3]>x[4]:
    print("the maximum value in the list is:", x[3])
else:
    print("the maximum value in the list is:", x[4])

if x[0]<x[1] and x[0]<x[2] and x[0]<x[3] and x[0]<x[4]:
    print("the minimum value in the list is:", x[0])
elif x[1]<x[0] and x[1]<x[2] and x[1]<x[3] and x[1]<x[4]:
    print("the minimum value in the list is:", x[1])
elif x[2]<x[0] and x[2]<x[1] and x[2]<x[3] and x[2]<x[4]:
    print("the minimum value in the list is:", x[2])
elif x[3]<x[0] and x[3]<x[1] and x[3]<x[2] and x[3]<x[4]:
    print("the minimum value in the list is:", x[3])
else:
    print("the minimum value in the list is:", x[4])