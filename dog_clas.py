class dog:
    species = "bulldog"
    species2 = "golden retriever"
    def __init__(self, name, age):
        self.name = name
        self.age = age
spot = dog("Spot", 3)
buddy = dog("Buddy", 5)
print("Spot is a {} ".format(spot.species))
print("Buddy is a {} ".format(buddy.species2))
print("\n","{} is {} years old".format(spot.name, spot.age))
print("{} is {} years old".format(buddy.name, buddy.age))