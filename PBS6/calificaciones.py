diccionario = {}
while True:
    alumno = input("Ingrese el nombre del estuduante (o escriba 'salir' para terminar): ").lower()
    if alumno == 'salir':
        break
    calificaciones = input(f"Ingrese las calificaciones del anumno '{alumno}' en un texto: ").split()
    diccionario[palabra] = sinonimos.lower()

for nombre, calificaciones in diccionario.items():
    print(f"{nombre}: {calificaciones}")