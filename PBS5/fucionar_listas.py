def fusionar_listas_ordenadas(lista1, lista2):
    lista_fusionada = lista1 + lista2
    return sorted(lista_fusionada)

lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
print(fusionar_listas_ordenadas(lista1, lista2))