def buscar_elemento(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == elemento:
                return (i, j)
    
    return None

def imprimir_resultado(posicion, elemento):
    if posicion:
        print(f"El elemento {elemento} se encuentra en la posición: fila {posicion[0] + 1}, columna {posicion[1] + 1}")
    else:
        print(f"El elemento {elemento} no se encuentra en la matriz.")

matriz = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

elemento = int(input("Introduce el elemento que deseas buscar: "))
posicion = buscar_elemento(matriz, elemento)
imprimir_resultado(posicion, elemento)