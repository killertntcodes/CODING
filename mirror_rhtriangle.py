x = int(input("Enter number of rows: "))

for i in range(1, x + 1):
    print(" " * (x - i) + "*" * i)