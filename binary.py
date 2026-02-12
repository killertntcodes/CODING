x = int(input("Enter a decimal number: "))

bin = ""

while x > 0:
    bin = str(x % 2) + bin
    x = x // 2

print("Binary number:", bin)