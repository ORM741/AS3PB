def eliminador (frase):
    palabras = frase.split()
    nueva_frase = ' '.join(palabras)
    return nueva_frase

frase = input ("ingrese una frase: ")

print (eliminador(frase))
