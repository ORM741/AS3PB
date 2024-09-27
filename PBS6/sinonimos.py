diccionario_sinonimos = {}
while True:
    palabra = input("Ingrese una palabra (o escriba 'salir' para terminar): ").lower()
    if palabra.lower() == 'salir':
        break
    sinonimos = input(f"Ingrese los sinónimos de '{palabra}' en un texto: ").split()
    diccionario_sinonimos[palabra] = sinonimos.lower()

while True:
    buscar = input("ingrese la palabra que desea buscar (o escriba 'salir' para salir)")
    if buscar.lower() == 'salir':
        break
    print(diccionario_sinonimos[buscar])