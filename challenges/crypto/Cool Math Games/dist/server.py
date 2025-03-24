from string import ascii_lowercase, ascii_uppercase, digits
import os
import random

RAND_SEED = os.getenv("seed")
random.seed(int(RAND_SEED))

def generate_random_string():
    return "".join([random.choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(32)])

rounds = 160
print(f"Welcome to my game! Your user ID is \"{generate_random_string()}\"")
print("Complete all the rounds of this game, and you win the flag! Good luck!")
for i in range(rounds):
    print('*'*8, f"Round {i+1}", '*'*8)
    answer_string = generate_random_string()
    guess = str(input("Enter the string: "))
    if guess != answer_string:
        print("Sorry, but your response was wrong. Out!")
        exit()
    print()
    
print(f"Congratulations! Here is your flag: {os.getenv('FLAG')}")