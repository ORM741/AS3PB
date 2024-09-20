def eliminar_impares(lista):
    return [num for num in lista if num % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(eliminar_impares(lista))