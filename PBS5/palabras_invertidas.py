def invertir_palabras(frase):
    palabras = frase.split()
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    frase_invertida = ' '.join(palabras_invertidas)
    return frase_invertida
frase = input("Ingresa una frase: ")
frase_invertida = invertir_palabras(frase)
print(f"Frase con las letras de cada palabra invertidas: {frase_invertida}")