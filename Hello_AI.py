print("hello! i am AI bot, how can i help you?: ")
name = input()
print(f"hello {name}, nice to meet you!")
print("how are you feeling today? (good/bad): ")
mood = input().lower()
if mood == "good":
    print("that's great to hear! keep up the positive vibes!")
elif mood == "bad":
    print("i'm sorry to hear that. remember, it's okay to have bad days. if you want to talk about it, i'm here to listen.")
else:
    print("i see, sometimes it's hard to express our feelings!")
print("twas nice chatting with you, have a wonderful day!")