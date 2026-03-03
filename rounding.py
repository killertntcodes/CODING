import math
x= float(input("enter a number: "))
print("the floor value of",x,"is:" + str(math.floor(x)) + ',' +  str(math.ceil(x)))
y=10 
z=-15
print("the value of y after copying the sign of z is:",str(math.copysign(y,z)))

print("absolute value of -96 and 56 is:" + str(math.fabs(-96)) + ',' + str(math.fabs(56)))

print("the GCD of 24 and 56 is: " + str(math.gcd(24,56)))