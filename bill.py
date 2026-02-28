x = float(input("Enter total bill amount: "))
y = float(input("Enter amount paid: "))

due = x - y

if due > 0:
    print("Customer still needs to pay:", due)
elif due < 0:
    print("Change to return:", -due)
else:
    print("Payment complete. No due amount.")