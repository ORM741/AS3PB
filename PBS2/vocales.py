#programa que cuenta las vocales en una cadena de texto
cadena = input("Ingresa una cadena de texto: ")
cant = 0
vocales = "aeiouAEIOU"
for i in cadena:
    if i in vocales:
        cant = cant + 1

print (cant)