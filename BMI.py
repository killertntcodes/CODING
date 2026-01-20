height= float(input("enter your height in cm: "))
weight= float(input("enter your weight in kg: "))
bmi= weight/(height/100)**2
print("your bmi is:", round(bmi,2))
if bmi<=18.4:
    print("you are underweight")
elif bmi<=24.9:
    print("you have a normal weight")
elif bmi<=29.9:
    print("you are overweight")
else:
    print("you are obese")