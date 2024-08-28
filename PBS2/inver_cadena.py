#programa que invierte una dadena de texto
cadena = input("Ingresa una cadena de texto: ")
lista = cadena.split()
lista.reverse()
palabra = " ".join(lista)
print (palabra)