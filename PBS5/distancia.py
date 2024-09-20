import math
def distancia_euclidiana(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

punto1 = (1, 2)
punto2 = (4, 6)
distancia = distancia_euclidiana(punto1, punto2)

print(f"La distancia euclidiana entre {punto1} y {punto2} es {distancia}")