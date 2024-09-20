def contador (frase):
    vocal = 0
    consonate = 0
    vocales = "aeiouAEIOU"
    for i in frase:
        if i in vocales:
            vocal += 1
        else :
            consonate += 1
    return f"vocales : {vocal} , consonates: {consonate}"

frase = input("Ingresa una palabra: ")

print (contador(frase))