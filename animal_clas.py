from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can run and have two legs")
class snake(animal):
    def move(self):
        print("I can hiss and have no legs")
class dog(animal):
    def move(self):
        print("I can bark and have four legs")
class lion(animal):
    def move(self):
        print("I can roar and have four legs")
h = human()
h.move()
s = snake()
s.move()
d = dog()
d.move()
l = lion()
l.move()