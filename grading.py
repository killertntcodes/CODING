print("enter marks obtained in 5 subjects")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())
totalMarks = markOne + markTwo + markThree + markFour + markFive
avg= totalMarks / 5
if avg>=91 and avg<=100:
    print("Grade A1")
elif avg>=81 and avg<=90:
    print("Grade A2")
elif avg>=71 and avg<=80:
    print("Grade B1")
elif avg>=61 and avg<=70:
    print("Grade B2")
elif avg>=51 and avg<=60:
    print("Grade C1")
elif avg>=41 and avg<=50:
    print("Grade C2")
elif avg>=33 and avg<=40:
    print("Grade D")
elif avg>=21 and avg<=32:
    print("E1")
elif avg>=0 and avg<=20:
    print("E2")
else:
    print("Invalid marks")