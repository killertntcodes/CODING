import random
def password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    print("How long do you want your password to be?")
    length = int(input())
    for i in range(length):
        password += random.choice(characters)

    print("Your random password is: " + password)
password()