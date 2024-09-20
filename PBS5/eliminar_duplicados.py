def lista_a_conjunto(lista):
    return set(lista)

lista = [1, 2, 2, 3, 4, 4, 5]
conjunto = lista_a_conjunto(lista)

print(f"La lista original: {lista}")
print(f"El conjunto resultante (sin duplicados): {conjunto}")