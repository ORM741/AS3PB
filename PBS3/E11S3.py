def determinante_3x3(matriz):
    if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
        raise ValueError("La matriz debe ser de 3x3")
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[0][2]
    d = matriz[1][0]
    e = matriz[1][1]
    f = matriz[1][2]
    g = matriz[2][0]
    h = matriz[2][1]
    i = matriz[2][2]
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    
    return det

matriz = [
    [2, 5, 3],
    [1, -2, 4],
    [3, 6, 1]
]

resultado = determinante_3x3(matriz)
print(f"El determinante es: {resultado}")