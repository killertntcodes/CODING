number = input("Enter a number: ")

count = 0
for digit in number:
    if digit.isdigit():
        count= count+1
print("Number of digits entered:", count)