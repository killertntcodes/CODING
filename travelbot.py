import re, random
from colorama import Fore, Style

init(autoreset=True)

destinations = {
    "cities": ["Paris", "Tokyo", "New York", "Sydney", "Rome"],
    "beaches": ["Bali", "Maldives", "Hawaii", "Phuket", "Santorini"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Atlas Mountains"]
}
jokes = [
    "why dont proggrammers like nature? It has too many bugs.",
    "why did the computer go to the doctor? It had a virus.",
    "why do travelers always feel warm? Because of all their hotspots.",
]
def normalize_input(text):
    return re.sub(r'[^\w\s]', '', text.strip().lower())
def recommend():
    print(f"{Fore.CYAN}+ travelbot: beaches, mountains or cities.")
    preference = input(f"{Fore.YELLOW}+ you: ")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"{Fore.CYAN}+ travelbot: I recommend visiting {suggestion}!")
        print(f"{Fore.CYAN}+ travelbot: Do u like it? (yes/no)")
        answer = input(f"{Fore.YELLOW}+ you: ")

        if answer == "yes":
            print(f"{Fore.CYAN}+ travelbot: Great! I hope you have an amazing trip to {suggestion}!")
        elif answer == "no":
            print(f"{Fore.CYAN}+ travelbot: No worries! I can suggest another destination if you'd like.")
            recommend()
        else:
            print(f"{Fore.CYAN}+ travelbot: Ill suggest another destination.")
            recommend()
    else:
        print(f"{Fore.CYAN}+ travelbot: Sorry, I didn't understand that. Please choose from beaches, mountains, or cities.")
        recommend()
        
def packin_tips():
    print(f"{Fore.CYAN}+ travelbot: Where to?: ")
    location = normalize_input(input(f"{Fore.YELLOW}+ you: "))
    print(f"{Fore.CYAN}+ travelbot: How many days?: ")
    days = input(f"{Fore.YELLOW}+ you: ")

    print (f"{Fore.CYAN}+ travelbot: For a trip to {location} lasting {days} days, I recommend packing:")
    print(f"{Fore.CYAN}+ travelbot: - Comfortable shoes")
    print(f"{Fore.CYAN}+ travelbot: - Weather-appropriate clothing")
    print(f"{Fore.CYAN}+ travelbot: - charger and adapters")
    print(f"{Fore.CYAN}+ travelbot: - Travel documents and ID")
    print(f"{Fore.CYAN}+ travelbot: - Toiletries and personal items")

def tell_joke():
    joke = random.choice(jokes)
    print(f"{Fore.CYAN}+ travelbot: Here's a travel joke for you: {joke}")

def show_help():
    print(f"{Fore.CYAN}+ travelbot: I can help you with travel recommendations, packing tips, and travel jokes!")
    print(f"{Fore.CYAN}+ travelbot: Just type 'recommend' for destination suggestions, 'pack' for packing tips, 'joke' for a travel joke, or 'help' to see this message again.")
def chat():
    print(f"{Fore.CYAN}+ travelbot: Hello! I'm your travel assistant. How can I help you today?")
    while True:
        command = input(f"{Fore.YELLOW}+ you: ").strip().lower()
        if command == "recommend":
            recommend()
        elif command == "pack":
            packin_tips()
        elif command == "joke":
            tell_joke()
        elif command == "help":
            show_help()
        else:
            print(f"{Fore.CYAN}+ travelbot: Sorry, I didn't understand that. Please type 'help' to see the available commands.")