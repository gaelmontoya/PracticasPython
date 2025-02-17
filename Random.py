import random

numero_secreto = random.randint(1, 10)
intento = int(input("Adivina un número entre 1 y 10: "))

if intento == numero_secreto:
    print("¡Felicidades! Adivinaste el número.")
else:
    print(f"Fallaste. El número era {numero_secreto}.")
