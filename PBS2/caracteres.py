#programa que cuenta cuantes veces aparece un caracter en una cadena de texto
cadena = str (input("escriba una cadena de texto: "))
caracter = str (input("ingrese el caracter que desea contar: "))
contador = 0
for i in cadena:
    if i == caracter:
        contador = contador + 1

print ("las veces que", caracter ,"aparece en la cadena es", contador)