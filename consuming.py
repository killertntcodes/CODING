x=int(input("enter how many units u consumed: "))
if x<50:
    print("bill=27.6")
elif x<100 and x>=50:
    print("bill=38.25")
elif x<200 and x>=100:
    print("bill=50.26")
else:
    print("bill=83.45")
