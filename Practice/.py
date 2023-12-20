import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)
    
def simulation(num_rolls):
    dice1 = Dice()
    dice2 = Dice()

    for i in range(num_rolls):
        roll1 = dice1.roll()
        roll2 = dice2.roll()

        print(f"Roll 1: {roll1}, Roll 2: {roll2}")

simulation(5)
