import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(500, 500)
polygon = turtle.Turtle()
num_sides= 4
side_length = 70
angle = 360 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)
turtle.done()