amount= int(input("enter how much money u want to withdraw"))
n1= amount//100
n2= (amount%100)//50
n3= ((amount%100))//10
print("notes of 100 rupee notes:", n1)
print("notes of 50 rupee notes:", n2)
print("notes of 10 rupee notes:", n3)