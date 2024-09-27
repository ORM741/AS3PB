diccionario = {}
while True:
    alumno = input("Ingrese el nombre del alumno (o escriba 'salir' para terminar): ").lower()
    if alumno == 'salir':
        break
    info = input(f"Ingrese la informacion del alumno: '{alumno}' ")
    diccionario[alumno] = info

while True:
    buscar = input("ingrese el alumno (o escriba 'salir' para salir)")
    if buscar.lower() == 'salir':
        break
    print(diccionario[buscar])