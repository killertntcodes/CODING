class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circumference(self):
        return 2 * 3.14 * self.radius
c = int(input("Enter the radius of the circle: "))
myCircle = circle(c)
print("Area of the circle is: ", myCircle.area())
print("Circumference of the circle is: ", myCircle.circumference())