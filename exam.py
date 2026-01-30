x= input("do u have a medical condition : ")
if x=="yes":
    print("You are eligible for the exam") 
else:
    attendence= int(input("Enter your attendence% : "))
    if attendence<75:
        print("You are not eligible for the exam")
    else:
        print("You are eligible for the exam")