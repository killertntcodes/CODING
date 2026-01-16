bp=float(input("Enter the buying price: "))
sp=float(input("Enter the selling price: "))
if bp>sp:
    print("is is a loss of", bp-sp)
elif sp==bp:
    print("theres no profit nor loss")
else:
    print("there is a profit of", sp-bp)