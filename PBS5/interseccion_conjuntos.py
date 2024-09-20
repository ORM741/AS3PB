def interseccion_conjuntos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)


conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
interseccion = interseccion_conjuntos(conjunto1, conjunto2)

print(f"La intersección de {conjunto1} y {conjunto2} es: {interseccion}")