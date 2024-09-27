diccionario = {}
while True:
    producto = input("Ingrese un nombre del producto (o escriba 'salir' para terminar): ").lower()
    if producto == 'salir':
        break
    precio = input(f"Ingrese el precio para '{producto}': ")
    diccionario[producto] = precio.lower()

while True:
    buscar = input("ingrese el producto que desea conocer el precio (o escriba 'salir' para salir)")
    if buscar.lower() == 'salir':
        break
    print(diccionario[buscar])