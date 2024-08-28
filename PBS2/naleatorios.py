#programa que genera numeros aleatorios de 1 al 100 n veces
import random
n = int(input("Ingresa la cantidad de números aleatorios a generar: "))
n_al = [random.randint(1, 100) for _ in range(n)]
print("Lista de números aleatorios generada:")
print(n_al)