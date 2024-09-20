def transponer_matriz(matriz):
    matriz_transpuesta = []
    for i in range(3):
        fila_transpuesta = []
        for j in range(3):
            fila_transpuesta.append(matriz[j][i])
        matriz_transpuesta.append(fila_transpuesta)
    return matriz_transpuesta

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
imprimir_matriz(matriz)

matriz_transpuesta = transponer_matriz(matriz)

print("\nMatriz transpuesta:")
imprimir_matriz(matriz_transpuesta)

print("\nMatriz transpuesta:")
imprimir_matriz(matriz_transpuesta)