import base64
import pickle
import random

SPLASH = """
   _____ _                                  _____                          
  / ____| |                                / ____|                         
 | (___ | |__  _ __ ___   ___  _ __ ___   | (___   ___ _ ____   _____ _ __ 
  \___ \| '_ \| '__/ _ \ / _ \| '_ ` _ \   \___ \ / _ \ '__\ \ / / _ \ '__|
  ____) | | | | | | (_) | (_) | | | | | |  ____) |  __/ |   \ V /  __/ |   
 |_____/|_| |_|_|  \___/ \___/|_| |_| |_| |_____/ \___|_|    \_/ \___|_|                                                              
"""
CHOICE_MESSAGE = """Shroom Server v1.0
1. Farm shroom
2. Buy flag
3. Load Save
4. Save and Exit
5. Exit
"""
FLAG_REWARD_COST = 10**15

name = None
farmed = 0


def to_ordinal(n: int) -> str:
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]

    return str(n) + suffix


def ask_random_question() -> bool:
    operators = ["+", "-", "*"]

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)

    operator = random.choice(operators)

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2

    print(f"{num1} {operator} {num2} = ? ")

    try:
        user_answer = int(input("> "))
    except Exception:
        return False

    if answer == user_answer:
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False


class SaveState:
    def __init__(self, name: str, farmed: int):
        self.name = name
        self.farmed = farmed


def buy_flag():
    if farmed < FLAG_REWARD_COST:
        print("You don't have enough shrooms to buy a flag!")
    else:
        try:
            with open("flag.txt", "r") as f:
                print(f.read())
        except Exception:
            print(
                "Looks like we did an oopsy, if this is happening on the challenge server, please let us know."
            )
        exit()


def farm():
    global farmed
    if ask_random_question():
        farmed += 1
        print(f"{to_ordinal(farmed)} shroom farmed today!")


def save_state():
    state = SaveState(name, farmed)
    state_bytes = pickle.dumps(state)
    state_b64 = base64.b64encode(state_bytes).decode("utf-8")
    print("Save this magic string to reload your save: " + state_b64)
    print("Goodbye!")
    exit()


def load_state():
    state_b64 = input("Enter your magic string: ")
    state_bytes = base64.b64decode(state_b64.encode("utf-8"))
    state = pickle.loads(state_bytes)

    if state.name != name:
        print("You don't have permission to load this save!")
        exit()

    global farmed
    farmed = state.farmed

    print("Save loaded successfully!")


def main():
    global name
    print(SPLASH)
    name = input("What is your name? ")
    print("Welcome, " + name + "!")
    print("Farm shrooms until you have enough to buy a flag!\n")

    while True:
        print(f"Name: {name}")
        print(f"Shrooms farmed: {farmed}")
        print()

        print(CHOICE_MESSAGE)
        choice = input("> ")

        if choice == "1":
            farm()
        elif choice == "2":
            buy_flag()
        elif choice == "3":
            load_state()
        elif choice == "4":
            save_state()
        elif choice == "5":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input")
        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
