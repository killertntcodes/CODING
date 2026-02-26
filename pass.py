x=int(input("Enter a number: "))
for i in range(x):
    if x%20==0:
        print("twist")
        break
    elif x%15==0:
        pass
        break
    elif x%5==0:
        print("fizz")
        break
    elif x%3==0:
        print("buzz")
        break
    else:
        print(x)
        break