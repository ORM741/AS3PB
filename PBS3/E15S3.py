import random

def juego_adivinanza():
    numero_objetivo = random.randint(1, 100)
    adivinanza = None
    intentos = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100.")
    while adivinanza != numero_objetivo:
        try:
            adivinanza = int(input("Adivina el número: "))
            intentos += 1

            if adivinanza < numero_objetivo:
                print("El número es mayor.")
            elif adivinanza > numero_objetivo:
                print("El número es menor.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_objetivo} en {intentos} intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")

juego_adivinanza()