import turtle
x= turtle.Screen()
x.bgcolor("gray")
x.title("turtle")
y=turtle.Turtle()
z=int(input("Enter the number of sides: "))
size=10
while True:
    for i in range(4):
        y.forward(size+1)
        y.right(90)
    size+= 10
turtle.done()