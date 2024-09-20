def capturar_matriz():
    matriz = []
    print("Introduce los elementos de la matriz 3x3:")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"Elemento [{i+1}, {j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    matriz_resultado = []
    for i in range(3):
        fila_resultado = []
        for j in range(3):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        matriz_resultado.append(fila_resultado)
    return matriz_resultado

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

print("Captura de la primera matriz:")
matriz1 = capturar_matriz()

print("\nCaptura de la segunda matriz:")
matriz2 = capturar_matriz()

resultado = sumar_matrices(matriz1, matriz2)

print("\nLa suma de las matrices es:")
imprimir_matriz(resultado)