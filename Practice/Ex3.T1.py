import random
num = random.randint(1,100)
attempts = 1
while attempts <=3:
    guess_num = int(input("Introduzca un num del 1 al 100: "))
    if num < guess_num:
        print("El número que ha introducido es mayor") 
    elif num > guess_num:
        print("El número que ha introducido es menor") 
    else: 
        print("Enhorabuena! Ha acertado") 
        break   
    attempts+=1

if attempts > 3:
    print("Lo siento, ha agotado sus intentos. El número correcto era:", num)



