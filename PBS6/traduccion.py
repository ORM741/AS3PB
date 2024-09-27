diccionario = {}
while True:
    palabra = input("Ingrese la palabra (o escriba 'salir' para terminar): ").lower()
    if palabra == 'salir':
        break
    traduccion = input(f"Ingrese la traduccion de '{palabra}': ")
    diccionario[palabra] = traduccion.lower()

while True:
    buscar = input("ingrese la palabra que desea conocer su traduccion (o escriba 'salir' para salir)")
    if buscar.lower() == 'salir':
        break
    print(diccionario[buscar])