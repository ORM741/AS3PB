diccionario = {}
while True:
    nombres = input("ingrese el nombre del jugador: (o escriba 'salir' para salir) ")
    if nombres.lower() == 'salir':
        break
    puntajes = input ("ingrese el puntaje del jugador:")
    diccionario[nombres] = puntajes

for nombre, puntaje in diccionario.items():
    print(f"{nombre}: {puntaje}")