import random
x= True
num = random.randint(1,100)
print("guess a number between 1 and 100, you have 8 trys")
trys =  8
while x:
    guess = int(input("enter your guess: "))
    trys = trys - 1
    if trys == 0:
        print("you lose! The number was: ", num)
        x = False
    if guess < num:
        print("too low")
    elif guess > num:
        print("too high")
    else:
       print("you guessed it!,You win!")
       x = False 
    