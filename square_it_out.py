start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

squares = []
even = []
odd = []

for x in range(start, end + 1):
    sq = x**2
    squares.append(sq)
    
    if sq % 2 == 0:
        even.append(sq)
    else:
        odd.append(sq)

print("Square values:", squares)
print("Even squares:", even)
print("Odd squares:", odd)