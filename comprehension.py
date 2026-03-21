x = int(input("Enter a number: "))

odd_under = [i for i in range(x) if i % 2 != 0]
odd_all = [i for i in range(1, x + 1, 2)]

print("Odd numbers under:", odd_under)
print("Odd numbers list:", odd_all)

fruits = ["apple", "banana", "mango", "orange"]
updated = [fruit.capitalize() for fruit in fruits]
print("Updated list:", updated)