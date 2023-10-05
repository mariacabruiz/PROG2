# 3
#Guess the number: Develop a game where the computer chooses a random number, and
#the player must guess it within a limited number of attempts

import random
min= 1
max = 50
attemps= 3

secret_number= random.randint(min, max)

for attemp in range(1, attemps +1):
    guess= int(input(f"Guess the number between {min} and {max}"))
    if guess == secret_number:
        print("Congrats!")
    if guess < secret_number:
        print("Try a higher number")
    else:
        print("Try a lower")
else:
    print(f"You run the oportunities. The number was {secret_number}")
