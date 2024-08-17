import random

numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinar un número secreto! \n Tienes 5 intentos para acertar!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("GAME OVER! No lograste adivinar dentro de los 5 intentos permitidos :( ")
        break

    numero = int(input("Introduce un número del 0 al 99: "))

    if numero == numero_secreto:
        print("Felicitaciones, adivinaste el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("Pista: El número secreto es mayor al ingresado")
    else:
        print("Pista: El número secreto es menor al ingresado")

    cant_intentos += 1
