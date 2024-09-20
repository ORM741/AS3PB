def diferencia_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

diferencia = diferencia_conjuntos(conjunto1, conjunto2)
print(f"La diferencia entre {conjunto1} y {conjunto2} es: {diferencia}")