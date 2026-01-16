math= int(input("math:"))
english= int(input("english:"))
science= int(input("science:"))
cs= int(input("cs:"))
business=int(input("business:"))
sum = math+english+science+cs
if sum>=450:
    print("Grade A+")
elif sum>=400:
    print("Grade A")
elif sum>=350:
    print("Grade B")
elif sum>=300:
    print("Grade c")
elif sum>=250:
    print("Grade D")
else:
    print("Grade F")