def eliminar_elemento(conjunto, elemento):
    conjunto.discard(elemento)
    return conjunto

conjunto = {1, 2, 3, 4, 5}
elemento_a_eliminar = 3
conjunto_actualizado = eliminar_elemento(conjunto, elemento_a_eliminar)

print(f"Conjunto después de eliminar {elemento_a_eliminar}: {conjunto_actualizado}")