##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.
 # 2 variables: dado 1 y dado 2
import random

def roll_two_dice():
    die1 = random.randint(1, 6)
    die2= random.randint(1,6)
    return die1, die2

def main():
 
    die1, die2 = roll_two_dice()
    print(f"First dice:{die1}")
    print(f"Second dice:{die2}")
    print(f"Sum total: ",die1+die2)

def main():
    results = []  # Lista para almacenar los resultados de los dados
    
    for i in range(1, 1001):  # Repetir 1000 veces
        die1, die2 = roll_two_dice()
        total = die1 + die2
        results.append((i, die1, die2, total))  # Añadir el número de tirada, valores de los dados y su suma a la lista
        
    for result in results:
        print(f"Tirada {result[0]} - Primer dado: {result[1]}, Segundo dado: {result[2]}, Suma: {result[3]}")

if __name__ == "__main__":
    main()