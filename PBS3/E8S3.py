def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    return cadena == cadena[::-1]

cadena = input ("ingrese un texto")
if es_palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')