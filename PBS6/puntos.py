def puntos(punto):
    distancia = []
    for i in punto:
        x, y = i
        distancia.append(abs(x**2 + y**2))
    return distancia

punto = [(1, 2), (3, 4), (0, 1), (-1, -1)]
print(puntos(punto))