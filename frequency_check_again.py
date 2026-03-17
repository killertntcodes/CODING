test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

value = int(input("Enter value to check: "))

count = list(test_dict.values()).count(value)

print("Frequency:", count)