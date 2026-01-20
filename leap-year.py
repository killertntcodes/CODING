yr=int(input("enter a the year"))
if (yr%4==0) and (yr%400==0):
    print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")