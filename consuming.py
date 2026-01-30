x=int(input("enter how many units u consumed: "))
if x<50:
    print("the bill is : ", (x*2.60)+25)
elif x<100 and x>=50:
    print("the bill is : ", (x*3.25)+35)
elif x<200 and x>=100:
    print("the bill is : ", (x*5.26)+45)
else:
    print("the bill is : ", (x*8.45)+75)