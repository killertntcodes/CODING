class vehicle:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
    def display(self):
        print("The name of the vehicle is ", self.name)
        print("The fare of the vehicle is ", self.fare)
class bus(vehicle):
    def __init__(self, name, fare):
        super().__init__(name, fare)
    def display(self):
        print("The name of the vehicle is", self.name)
        print("The bus fare is", self.fare)
vehicle = vehicle("Car", 10)
vehicle.display()
bus = bus("Volvo", 6)
bus.display()