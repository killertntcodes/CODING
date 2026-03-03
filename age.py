try:
    age = int(input("Enter your age: "))
    
    if age <= 0 or age > 120:
        print("Error: Invalid age entered.")
    else:
        print("Age entered is correct.")
        
        # Check even or odd
        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")

except ValueError:
    print("Error: Please enter numbers only.")