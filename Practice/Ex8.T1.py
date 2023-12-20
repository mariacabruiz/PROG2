import random

def roll_dices():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

# Store the result of the function call
result = roll_dices()

# Access the values and print them
print(f"{result[0]}, {result[1]}")
