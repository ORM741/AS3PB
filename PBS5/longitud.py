def ordenar_por_longitud(lista_palabras):
    return sorted(lista_palabras, key=len)
    
lista_palabras = ["manzana", "kiwi", "plátano", "pera", "uva"]
print(ordenar_por_longitud(lista_palabras))