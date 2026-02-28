try:
    num1 , num2= eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result of division:", result)
except ZeroDivisionError:
    print("division by zero is not allowed.")
except SyntaxError:
    print("Invalid input format. Please enter two numbers separated by a comma.")
except:
    print("wrong input")
else:
    print("division successful")
finally:
    print("This block will always execute.")