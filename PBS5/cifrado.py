def cifrar_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = 'A' if caracter.isupper() else 'a'
            texto_cifrado += chr((ord(caracter) - ord(base) + desplazamiento) % 26 + ord(base))
        else:
            texto_cifrado += caracter
    return texto_cifrado

# Ejemplo de uso
texto_original = "Hola Mundo"
desplazamiento = 3
print(cifrar_cesar(texto_original, desplazamiento))