diccionario = {}
while True:
    contacto = input("Ingrese un nombre para la agenda (o escriba 'salir' para terminar): ").lower()
    if contacto == 'salir':
        break
    numero = input(f"Ingrese el numero telefonico para '{nombre}': ")
    diccionario[contacto] = numero.lower()

while True:
    buscar = input("ingrese el contacto que desea buscar (o escriba 'salir' para salir)")
    if buscar.lower() == 'salir':
        break
    print(diccionario[buscar])