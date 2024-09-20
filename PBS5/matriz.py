def crear_matriz_ajedrez(n, m):
    matriz = []
    
    for i in range(n):
        fila = []
        for j in range(m):
            if (i + j) % 2 == 0:
                fila.append(0)
            else:
                fila.append(1)
        matriz.append(fila)
    
    return matriz

n = 5
m = 6
matriz = crear_matriz_ajedrez(n, m)

for fila in matriz:
    print(fila)