import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {
            "Apple": "red",
            "Banana": "yellow",
            "Grapes": "green",
            "Orange": "orange",
            "Blueberry": "blue"}
    def quiz(self):
        while (True):
            fruit, color= random.choice(list(self.fruits.items()))
            print(f"What is the color of {fruit}?")
            user_answer= input()
            if user_answer.lower() == color:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {color}.")

print("Welcome to the Fruit Quiz!")
fq = FruitQuiz()
fq.quiz()