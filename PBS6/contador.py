frecuencias = {}
frase = input("ingrese una frase ")
lista = frase.split()
for i in lista:
    if i in frecuencias:
        frecuencias[i] += 1
    else:
        frecuencias[i] = 1
for i, frecuencia in frecuencias.items():
        print(f"{i}: {frecuencia}")