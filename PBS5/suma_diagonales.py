def suma_diagonales(matriz):
    suma_principal = 0
    suma_secundaria = 0
    
    for i in range(5):
        suma_principal += matriz[i][i]
        suma_secundaria += matriz[i][4-i]
    
    return suma_principal, suma_secundaria

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print("Matriz:")
imprimir_matriz(matriz)
suma_principal, suma_secundaria = suma_diagonales(matriz)

print(f"\nSuma de la diagonal principal: {suma_principal}")
print(f"Suma de la diagonal secundaria: {suma_secundaria}")
print(f"Suma total de ambas diagonales: {suma_principal + suma_secundaria}")