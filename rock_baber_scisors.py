import random
print("1=rock 2=paper 3=sisors 4=quit")
x=""
a=""
y=int(input("enter ur choise: "))
if y==1:
    x="rock"
elif y==2:
    x="paper"
elif y==3:
    x="sisors"
elif y==4:
    x="quit"
while True:
    z=random.randint(1,3)
    if z==1:
        a="rock"
    elif z==2:
        a="paper"
    elif z==3:
        a="sisors"
    print("computer choise",a)
    if x=="rock" and a=="rock":
        print("its a tie")
    elif x=="paper" and a=="paper":
        print("its a tie")
    elif x=="sisors" and a=="sisors":
        print("its a tie")
    elif x=="rock" and a=="sisors":
        print("player wins")
    elif x=="paper" and a=="rock":
        print("player wins")
    elif x=="sisors" and a=="paper":
        print("player wins")
    elif x=="rock" and a=="paper":
        print("computer wins")
    elif x=="paper" and a=="sisors":
        print("computer wins")
    elif x=="sisors" and a=="rock":
        print("computer wins")
    y=int(input("enter ur choise:"))
    if y==1:
        x="rock"
    elif y==2:
        x="paper"
    elif y==3:
        x="sisors"
    elif y==4:
        break
    print("the user choise is",x)