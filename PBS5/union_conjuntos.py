def unir_conjuntos(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)
    
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
union = unir_conjuntos(conjunto1, conjunto2)

print(f"La unión de {conjunto1} y {conjunto2} es: {union}")